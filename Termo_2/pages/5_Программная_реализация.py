import streamlit as st

r"""
# Ключевые этапы в FEniCS

"""

r'''
## Граничные условия
'''

r'''
### Теплопроводность
'''

code = '''
mesh = Mesh(path)
fr = MeshFunction('size_t', mesh, cut_xml(path) + '_facet_region.xml')
pr = MeshFunction('size_t', mesh, cut_xml(path) + '_physical_region.xml')

F = FunctionSpace(mesh, polynom, eo) 

bc_tem_bottom = DirichletBC(F, THot, fr, 1)
bc_tem_top = DirichletBC(F, TAir, fr, 2)
bcs_tem = [bc_tem_bottom, bc_tem_top]

'''
st.code(code, language = 'python')

r'''
### Упругость
'''

code = '''


V = VectorFunctionSpace(mesh, polynom, eo)

l_fix_p = lambda x, on_boundary: near(x[0], 0.0) and near(x[1], L_z)
r_fix_p = lambda x, on_boundary: near(x[0], L_x) and near(x[1], L_z)

bc_u_lfp = DirichletBC(V, Constant((0, 0)), l_fix_p, method="pointwise")
bc_u_rfp = DirichletBC(V.sub(1), Constant(0), r_fix_p, method="pointwise")
bcs_u = [bc_u_lfp, bc_u_rfp]



'''
st.code(code, language='python')

r'''
## Решение краевой задачи
'''

r'''
### Тепло
'''

code = '''
F = FunctionSpace(mesh, polynom, eo)
tem = TrialFunction(F)
q = TestFunction(F)
F_T = k1 * inner(grad(tem), grad(q)) * dx(1) + 
      k2 * inner(grad(tem), grad(q)) * dx(2) + 
      alphaAir * (tem - TAir) * q * ds(4)

a_therm = lhs(eq_tem)
L_therm = rhs(eq_tem)
sol_settings = {'linear_solver': 'mumps'}

solve(a_therm == L_therm, tem, bcs_tem, solver_parameters=sol_settings)

'''
st.code(code, language = 'python')


r'''
### Упругость
'''

code = '''
V = VectorFunctionSpace(mesh, polynom, eo)
u = TrialFunction(V)
v = TestFunction(V)
d1 = v.geometric_dimension()  # space dimension
tem_el = Function(F)
I = Identity(d1)

eps = lambda v: 0.5 * (grad(v) + grad(v).T)
sigma = lambda v, mu, lmbda, T, beta: 2 * mu * eps(v) + lmbda * tr(eps(v)) * I
        -(beta * (lmbda + 2 * mu / 3)) * (T - T0) * I
 
F_u = inner(sigma(u, mu1, lambda1, tem_el, beta1), eps(v)) * dx(1)
     +inner(sigma(u, mu2, lambda2, tem_el, beta2), eps(v)) * dx(2)
a_elas = lhs(F_u)
L_elas = rhs(F_u)
solve(a_elas == L_elas, u, bcs_u, solver_parameters=sol_settings)

'''
st.code(code, language = 'python')

r'''
## Напряжение
'''

code = '''

Q = TensorFunctionSpace(mesh, polynom, eo)

stress = TrialFunction(Q)
w = TestFunction(Q)
disp = Function(V)
tem_str = Function(F)
F_s = inner(stress, w)*dx -inner(sigma(disp,mu1,lambda1,tem_str,beta1),w)*dx(1)
     -inner(sigma(disp,mu2,lambda2,tem_str,beta2),w)*dx(2)
a_str = lhs(F_s)
L_str = rhs(F_s)

solve(a_str == L_str, stress, solver_parameters=sol_settings)

'''
st.code(code, language = 'python')