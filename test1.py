"""
Solve for heat conduction equation and
equations of linear elasticity in 2D rectangular domain:

-k * laplacian(u) + Q = 0
-nabla * sigma = f

with fixed top left and right edges and
heat all area
"""

# from mshr

from __future__ import print_function
from fenics import BoxMesh, Point, DirichletBC, FacetNormal, RectangleMesh
from fenics import FunctionSpace, VectorFunctionSpace
from fenics import TrialFunction, TestFunction
from fenics import Expression, Function, Constant
from fenics import dot, inner, Identity, sym
from fenics import grad, nabla_grad, tr
from ufl import nabla_div
from fenics import sqrt
from fenics import project
from fenics import dX, ds
from fenics import solve, interpolate
from fenics import plot
from fenics import File
from fenics import lhs, rhs, assemble
from dolfin import near, SubDomain
from dolfin import *

# Material settings
rho = 7800  # [kg/m3] density
k = 50  # [W/(m*K)] thermal conductivity
Cp = 525  # [J/(kg*K)] heat capacity
E = 2.0e011  # [Pa] Young modulus
nu = 0.3  # Poisson coefficient
lambda_ = (nu * E) / ((1 + nu) * (1 - 2 * nu))  # Lamé's first parameter
mu = E / (2 * (1 + nu))  # Lamé's second parameter
alpha = 2.0e-05  # [1/K] thermal expansion coefficient

# Domain settings
dW = 0.01  # [m] domain width (x, z)
dH = 0.002  # [m] domain height
dD = dW  # [m] domain depth
resW = 20  # mesh resolution (x, z)-directions (number of points)
resH = 4  # mesh y-resolution
resD = resW

print('Domain size:', dW, '[m] x', dH, '[m] y', dD, '[m] z')

# Finite element order
eo = 1

# Create a mesh
mesh = RectangleMesh(Point(0.0, 0.0), Point(dW, dH), resW, resH)

# Create functional space
F = FunctionSpace(mesh, 'P', eo)  # piecewise linear polynomials
V = VectorFunctionSpace(mesh, 'P', eo)

# Create 'trial function' (the unknown function to be approximated) over the space F
tem = TrialFunction(F)  # scalar temperature field, such that: tem(x,y) = Sum(tem_i* w(x,y))
d1 = tem.geometric_dimension()  # space dimension
u = TrialFunction(V)  # vector displacement field
d2 = u.geometric_dimension()  # space dimension

# Create scalar 'test function' (or 'shape function', or 'weighting function') over the space F
q = TestFunction(F)  # q -> tem
v = TestFunction(V)  # v -> u

t = 0
# Define expressions used in variational forms to prevent repeated code generation
n = FacetNormal(mesh)  # per-face normal vector
k_ = Constant(k / (rho * Cp))  # thermal conductivity
Traction = Constant((0, 0))  # traction

t_range = 2  # [s]

tem_surf = '(300 + ' \
           '500 * exp(-pow( (t-5)/dt, 2)) * ' \
           '( (( pow((x[0] - dW/2)/r, 2) + pow((x[2] - dD/2)/r, 2) ) <= 1.0) ? 1.0 : 0.0))'
tem_desired = Expression('2000', degree=eo)
fact_ = Constant(1.0e19)

# Problem settings
tem_0 = Constant(300)  # [K] initial temperature
tem_ref = tem_0  # [K] reference temperature


# Define strains and stress
def epsilon(u):
    return 0.5 * (nabla_grad(u) + nabla_grad(u).T)
    # return sym(nabla_grad(u))


def epsilon_therm(tem):
    return alpha * (tem - tem_ref) * Identity(d1)


def sigma(u):
    return lambda_ * nabla_div(u) * Identity(d2) + 2 * mu * epsilon(u) \
        - (3 * lambda_ + 2 * mu) * epsilon_therm(tem)


# Compute boundary surfaces of the mesh (via C++ wrapper)

tol = 1E-14


# https://fenicsproject.org/olddocs/dolfin/1.3.0/python/demo/documented/subdomains-poisson/python/documentation.html
class Bottom(SubDomain):
    def inside(self, x, on_boundary):
        return near(x[1], 0.0)


class Top(SubDomain):
    def inside(self, x, on_boundary):
        return near(x[1], dH)


# bottom surfcae
# bs_bottom_wall = 'near(x[1], 0.0)'
# bs_bottom_wall = near(x[1],0.0)
bs_bottom_wall = Bottom()
# bs_top_wall = 'near(x[1],dH)'
# bs_top_wall = near(x[1],dH)
bs_top_wall = Top()

bs_top_edges = [Point(0.0, dH), Point(dW, dH)]


# bs_top_edges = Point(0.0, dH)

def lower_boundary_fixed_point(x, on_boundary):
    tol = 1E-15
    return (near(x[0], 0.0) and near(x[1],dH))

# def lower_boundary_fixed_point(x, on_boundary):
#     tol = 1E-15
#     return Point(0.0, dH)


def top_boundary_fixed_point(x, on_boundary):
    tol = 1E-15
    return (near(x[0], dW) and near(x[1],dH))


# BC at the bottom
bc_tem_bottom = DirichletBC(F, Constant(300), bs_bottom_wall)
bc_tem_top = DirichletBC(F, Constant(300), bs_top_wall)
bcs_tem = [bc_tem_bottom, bc_tem_top]
# bc_u_bottom = DirichletBC(V.sub(0), Constant((0,0)), bs_top_edges)
#
bc_top_fixed_point = DirichletBC(V.sub(0), Constant(0), top_boundary_fixed_point, method='pointwise')

bc_lower_fixed_point = DirichletBC(V.sub(0), Constant(0), lower_boundary_fixed_point, method='pointwise')
#
bcs_u = [bc_lower_fixed_point, bc_top_fixed_point]
# bcs_u = [bc_u_bottom]

# Compose weak form of PDE(heat):
tem_0 = Expression('300', degree=eo)
tem_n = project(tem_0, F, solver_type="cg", preconditioner_type="amg")
tem = TrialFunction(F)
q = TestFunction(F)

eq_tem = (k_ * inner(nabla_grad(tem), nabla_grad(q)) * dX - (tem_desired - tem) * fact_ * q * dX)
a_therm = lhs(eq_tem)
L_therm = rhs(eq_tem)

# Compose weak form of PDE(elasticity):
# Split the equation into right-hand-side (RHS) and left-hand-side (LHS) parts:
u = TrialFunction(V)
v = TestFunction(V)
sigma_ = lambda_ * nabla_div(u) * Identity(d2) + mu * (nabla_grad(u) + nabla_grad(u).T) \
         - (3 * lambda_ + 2 * mu) * alpha * (tem_n - tem_ref) * Identity(d1)
epsilon_ = 0.5 * (nabla_grad(v) + nabla_grad(v).T)
elastic_eqn = inner(sigma_, epsilon_) * dX - dot(Traction, v) * ds
# LHS, bilinear form
a_elas = lhs(elastic_eqn)
# RHS, Linear form
L_elas = rhs(elastic_eqn)

# Prepare export to file
path = 'results/'
tem_file = File(f'{path}tem.pvd')
u_file = File(f'{path}u.pvd')
vms_file = File(f'{path}vms.pvd')

# Time loop
tem = Function(F)
u = Function(V)

print(f'DOFs = {V.dim() + F.dim()}')

# Update time value in expression
# tem_desired.t = t

sol_settings = {'linear_solver': 'mumps'}

# Compute HCE
solve(a_therm == L_therm, tem, bcs_tem, solver_parameters=sol_settings)

# Update previous solution
tem_n.assign(tem)

# Compute elasticity
solve(a_elas == L_elas, u, bcs_u, solver_parameters=sol_settings)

# Update previous solution
#  u.assign(u)

# t += dt

# Compute stress
s = sigma(u) - (1. / 3) * tr(sigma(u)) * Identity(d2)  # deviatoric stress
von_Mises = sqrt(3. / 2 * inner(s, s))
von_Mises = project(von_Mises, F)

# Save solution
tem.rename('T [K]', 'label')
tem_file << (tem, t)
u.rename('U [m]', 'label')
u_file << (u, t)
von_Mises.rename('VMS [Pa]', 'label')
vms_file << (von_Mises, t)

print(f'{t}')
# print(f'{t} / {dt*num_steps}')
