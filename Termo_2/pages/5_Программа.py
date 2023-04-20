import streamlit as st



r'''
### Условия для вверхней и нижней граней
'''

code = '''
class Bottom(SubDomain):
    def inside(self, x, on_boundary):
        return near(x[1], 0.0)

class Top(SubDomain):
    def inside(self, x, on_boundary):
        return near(x[1], dH)
    
bs_bottom_wall = Bottom()
bs_top_wall = Top()

bc_tem_bottom = DirichletBC(F, TAir, bs_bottom_wall)
bc_tem_top = DirichletBC(F, THot, bs_top_wall)

bcs_tem = [bc_tem_bottom, bc_tem_top]

'''
st.code(code, language = 'python')

r'''
### Условия для вверхних точек
'''

code = '''

def left_top_fixed_point(x, on_boundary):
    tol = 1E-15
    return (near(x[0], 0.0) and near(x[1],dH))

def right_top_fixed_point(x, on_boundary):
    tol = 1E-15
    return (near(x[0], dW) and near(x[1],dH))

rt_y_fixed_point = DirichletBC(V.sub(1), Constant(0), right_top_fixed_point, method='pointwise')

lt_x_fixed_point = DirichletBC(V.sub(0), Constant(0), left_top_fixed_point, method='pointwise')
lt_y_fixed_point = DirichletBC(V.sub(1), Constant(0), left_top_fixed_point, method='pointwise')

bcs_u = [lt_x_fixed_point, lt_y_fixed_point, rt_y_fixed_point]


'''
st.code(code, language='python')


r'''
### Запись для тепла
'''

code = '''
F = FunctionSpace(mesh, polynom, eo)
tem = TrialFunction(F)
q = TestFunction(F)
eq_tem = (k_ * inner(nabla_grad(tem), nabla_grad(q)) * dX + alphaAir * (tem - TAir) * q * dX)
a_therm = lhs(eq_tem)
L_therm = rhs(eq_tem)
sol_settings = {'linear_solver': 'mumps'}

# Compute HCE
solve(a_therm == L_therm, tem, bcs_tem, solver_parameters=sol_settings)

'''
st.code(code, language = 'python')


r'''
### Запись для упругости
'''

code = '''
V = VectorFunctionSpace(mesh, polynom, eo)
# Compose weak form of PDE(elasticity):
# Split the equation into right-hand-side (RHS) and left-hand-side (LHS) parts:
u = TrialFunction(V)
v = TestFunction(V)
sigma_ = lambda_ * nabla_div(u) * Identity(d2) + mu * (nabla_grad(u) + nabla_grad(u).T) \
         - (3 * lambda_ + 2 * mu) * alpha * (tem_n - tem_ref) * Identity(d1)
epsilon_ = 0.5 * (nabla_grad(v) + nabla_grad(v).T)
elastic_eqn = inner(sigma_, epsilon_) * dX
# LHS, bilinear form
a_elas = lhs(elastic_eqn)
# RHS, Linear form
L_elas = rhs(elastic_eqn)
solve(a_elas == L_elas, u, bcs_u, solver_parameters=sol_settings)

'''
st.code(code, language = 'python')

r'''
### Запись для напряжения
'''

code = '''
# Compute stress
s = sigma(u) - (1. / 3) * tr(sigma(u)) * Identity(d2)  # deviatoric stress
von_Mises = sqrt(3. / 2 * inner(s, s))
von_Mises = project(von_Mises, F)
'''
st.code(code, language = 'python')