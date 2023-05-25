'''
КОД НЕ РАБОТАЕТ ЕСЛИ НЕ ДАТЬ ЕМУ АРГУМЕНТЫ КОМАНДНОЙ СТРОКИ!
Программа принимает 1 аргумент - путь до основного файла с сеткой
в формате XML
'''
from __future__ import print_function
import sys
from dolfin import *
'''
    Parameters
'''

# Domain settings
from ufl.coefficient import Coefficient
L_x = 1  # [m] domain width (x, z)
L_z = 1.2  # [m] domain height
L_y = 1  # [m] domain depth

# Consts 
mu1 = Constant(0.8e11)
mu2 = Constant(0.5e11)
lambda1 = Constant(1.25e11)
lambda2 = Constant(0.65e11)
k1 = Constant(200.)
k2 = Constant(100.)
beta1 = Constant(6.0e-6)
beta2 = Constant(3.0e-6)
alphaAir = Constant(50.)
TAir = Constant(300.)
THot = Constant(450.)
T0 = Constant(320.)

# Material settings
rho = 7800  # [kg/m3] density
# k = 50  # [W/(m*K)] thermal conductivity
Cp = 525  # [J/(kg*K)] heat capacity
E = 2.0e011  # [Pa] Young modulus
nu = 0.3  # Poisson coefficient
lambda_ = (nu * E) / ((1 + nu) * (1 - 2 * nu))  # Lamé's first parameter
mu = E / (2 * (1 + nu))  # Lamé's second parameter
# alpha = 2.0e-05  # [1/K] thermal expansion coefficient

print('Domain size:', L_x, '[m] x', L_y, '[m] y', L_z, '[m] z')

# Закачка сетки в задачу
# path = sys.argv[1]
path = 'mesh/3d/composite.xml'
cut_xml = lambda path: path.partition('.xml')[0]
mesh = Mesh(path)
fr = MeshFunction('size_t', mesh, cut_xml(path) + '_facet_region.xml')
pr = MeshFunction('size_t', mesh, cut_xml(path) + '_physical_region.xml')
# Finite element order
eo = 1
polynom = 'CG'
# Create functional space
F = FunctionSpace(mesh, polynom, eo)  # piecewise linear polynomials
V = VectorFunctionSpace(mesh, polynom, eo)
Q = TensorFunctionSpace(mesh, polynom, eo)

# Пробные функции для ур-я теплопроводности
tem = TrialFunction(F)  # scalar temperature field, such that: tem(x,y) = Sum(tem_i* w(x,y))
u = TrialFunction(V)  # vector displacement field

# Create scalar 'test function' (or 'shape function', or 'weighting function') over the space F
q = TestFunction(F)  # q -> tem
v = TestFunction(V)

# Compose weak form of PDE(heat):(V)  # v -> u

t = 0
# Define expressions used in variational forms to prevent repeated code generation
n = FacetNormal(mesh)  # per-face normal vector

# Compute boundary surfaces of the mesh (via C++ wrapper)

tol = 1E-13
lb_fix_p = lambda x, on_boundary: near(x[0], 0.0) and near(x[1], 0.) and near(x[2], L_z)
rb_fix_p = lambda x, on_boundary: near(x[0], L_x) and near(x[1], 0.) and near(x[2], L_z)
lt_fix_p = lambda x, on_boundary: near(x[0], 0.0) and near(x[1], L_y) and near(x[2], L_z)
rt_fix_p = lambda x, on_boundary: near(x[0], L_x) and near(x[1], L_y) and near(x[2], L_z)

# ГУ 1 рода для ур-я теплопроводности
bc_tem_bottom = DirichletBC(F, THot, fr, 1)
bc_tem_top = DirichletBC(F, TAir, fr, 2)
bcs_tem = [bc_tem_bottom, bc_tem_top]
# ГУ 1 рода для ур-я термоупругости
bc_u_lbfp = DirichletBC(V, Constant((0, 0, 0)), lb_fix_p, method="pointwise")
bc_u_rbfp = DirichletBC(V.sub(1), Constant(0), rb_fix_p, method="pointwise")
bc_u_ltfp = DirichletBC(V, Constant((0, 0, 0)), lt_fix_p, method="pointwise")
bc_u_rtfp = DirichletBC(V.sub(1), Constant(0), rt_fix_p, method="pointwise")
bcs_u = [bc_u_lbfp, bc_u_rbfp, bc_u_ltfp, bc_u_rtfp]

# Переопределяем дифференциалы интегралов для доступных подобластей
dx = Measure('dx', domain=mesh, subdomain_data=pr)
ds = Measure('ds', domain=mesh, subdomain_data=fr)
# Compose weak form of PDE(heat):
F_T = k1 * inner(grad(tem), grad(q)) * dx(1) \
 +k2 * inner(grad(tem), grad(q)) * dx(2) + alphaAir * (tem - TAir) * q * ds(4)
a_therm = lhs(F_T)
L_therm = rhs(F_T)

# Compose weak form of PDE(elasticity):
# Split the equation into right-hand-side (RHS) and left-hand-side (LHS) parts:
u = TrialFunction(V)
v = TestFunction(V)
d1 = v.geometric_dimension()  # space dimension
tem_el = Function(F)
I = Identity(d1)

eps = lambda v: 0.5 * (grad(v) + grad(v).T)
sigma = lambda v, mu, lmbda, T, beta: 2 * mu * eps(v) + lmbda * tr(eps(v)) \
 * I - (beta * (lmbda + 2 * mu / 3)) * (T - T0) * I
 
F_u = inner(sigma(u, mu1, lambda1, tem_el, beta1), eps(v)) * dx(1)\
 + inner(sigma(u, mu2, lambda2, tem_el, beta2), eps(v)) * dx(2)
a_elas = lhs(F_u)
L_elas = rhs(F_u)
# Слабая форма ур-я термоупругость для тензоров напряжений и деформаций
stress = TrialFunction(Q)
w = TestFunction(Q)
disp = Function(V)
tem_str = Function(F)
F_s = inner(stress, w)*dx \
    -inner(sigma(disp,mu1,lambda1,tem_str,beta1),w)*dx(1)\
    -inner(sigma(disp,mu2,lambda2,tem_str,beta2),w)*dx(2)
a_str = lhs(F_s)
L_str = rhs(F_s)
# Time loop
tem = Function(F)
u = Function(V)
stress = Function(Q)

print(f'DOFs = {V.dim() + F.dim()}')
sol_settings = {'linear_solver': 'lu'}

# Compute HCE
solve(a_therm == L_therm, tem, bcs_tem, solver_parameters=sol_settings)

# Compute elasticity
tem_el.assign(tem) # Присваем решение уравнения 1 для уравнения 2
solve(a_elas == L_elas, u, bcs_u, solver_parameters=sol_settings)

# Compute stress
tem_el.assign(tem) # Присваем решение уравнения 1 для уравнения 2
disp.assign(u)
solve(a_str == L_str, stress, solver_parameters=sol_settings)


# Save solution
path = 'results3D/3d/'
tem.rename('T [K]', 'label')
tem_file = File(f'{path}tem.pvd')
tem_file << (tem, t)
u_file = File(f'{path}u.pvd')
u.rename('U [m]', 'label')
u_file << (u)
stress.rename('Sigma [Pa]', 'label')
s_file = File(f'{path}stress.pvd')
s_file << (stress)
