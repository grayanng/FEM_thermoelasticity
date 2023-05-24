import streamlit as st
from PIL import Image
import os.path
import sys
import matplotlib.pyplot as plt
from dolfin import *
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
def plot2dtem(alpha_coef):
    alpha_coef = float(alpha_coef)

    # Domain settings
    from ufl.coefficient import Coefficient
    L_x = 0.02  # [m] domain width (x, z)
    L_z = 0.012  # [m] domain height
    L_y = 0.01  # [m] domain depth
    resW = 50  # mesh resolution (x, z)-directions (number of points)
    resH = 50  # mesh y-resolution
    resD = resW

    # Consts
    mu1 = Constant(0.8e11)
    mu2 = Constant(0.5e11)
    lambda1 = Constant(1.25e11)
    lambda2 = Constant(0.65e11)
    k1 = Constant(200.)
    k2 = Constant(100.)
    beta1 = Constant(6.0e-6)
    beta2 = Constant(3.0e-6)
    alphaAir = Constant(alpha_coef)
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
    path = 'mesh/classic_meshing/2D/composite_fenics/composite.xml'

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

    print(0)
    #%%
    tol = 1E-13
    l_fix_p = lambda x, on_boundary: near(x[0], 0.0) and near(x[1], L_z)
    r_fix_p = lambda x, on_boundary: near(x[0], L_x) and near(x[1], L_z)

    # ГУ 1 рода для ур-я теплопроводности
    bc_tem_bottom = DirichletBC(F, THot, fr, 1)
    bc_tem_top = DirichletBC(F, TAir, fr, 2)
    bcs_tem = [bc_tem_bottom, bc_tem_top]
    # ГУ 1 рода для ур-я термоупругости
    bc_u_lfp = DirichletBC(V, Constant((0, 0)), l_fix_p, method="pointwise")
    bc_u_rfp = DirichletBC(V.sub(1), Constant(0), r_fix_p, method="pointwise")
    bcs_u = [bc_u_lfp, bc_u_rfp]

    # Переопределяем дифференциалы интегралов для доступных подобластей
    dx = Measure('dx', domain=mesh, subdomain_data=pr)
    ds = Measure('ds', domain=mesh, subdomain_data=fr)
    # Compose weak form of PDE(heat):
    F_T = k1 * inner(grad(tem), grad(q)) * dx(1) \
     +k2 * inner(grad(tem), grad(q)) * dx(2) + alphaAir * (tem - TAir) * q * ds(4)
    a_therm = lhs(F_T)
    L_therm = rhs(F_T)
    tem = Function(F)
    print(f'DOFs = {V.dim() + F.dim()}')
    sol_settings = {'linear_solver': 'lu'}
    # Compute HCE
    solve(a_therm == L_therm, tem, bcs_tem, solver_parameters=sol_settings)
    figure = plt.figure(figsize=(16, 6))
    plt.subplot(121)
    fig = plot(tem, mesh)
    fig.set_cmap(cm.rainbow)

    plt.colorbar(fig, shrink=0.67)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.subplot(122)
    tol = 1E-8  # avoid hitting points outside the domain
    x = np.linspace(0.0 + tol, 0.02 - tol, 101)
    y = np.linspace(0 + tol, 0.012 - tol, 101)
    points = [(0, y_) for y_ in y]  # 2D points
    xp = [(x_, 0.006) for x_ in x]
    # p_line = np.array([tem(point) for point in points])
    p_line = np.array([tem(xg) for xg in xp])
    plt.plot(x, p_line, label='T(Y)')  # magnify w
    # plt.plot(x, xp)
    plt.legend(loc='upper left')
    plt.xlabel('X');
    plt.ylabel('T')
    plt.tight_layout()
    return figure




menu = st.sidebar.radio('***',
    (   '2D',)
)

if menu == '2D':
    values = st.slider(
        'Select a range of values',
        50.0, 15000.0, 25.0)
    st.write('Values:', values)

    (st.pyplot(plot2dtem(values)))


    r'''
        ### Параметры образца
        '''

    code = '''
        Lx = 0.02 
        Ly = 0.012
        Lz = 0.01

        # Lamé's first parameter
        lambda1 = Constant(1.25e11) 
        lambda2 = Constant(0.65e11)

        # Lamé's second parameter
        mu1 = Constant(0.8e11) 
        mu2 = Constant(0.5e11)

        # [W/(m*K)] thermal conductivity
        k1 = Constant(200.) 
        k2 = Constant(100.)

        # [1/K] thermal expansion coefficient
        beta1 = Constant(6.0e-6) 
        beta2 = Constant(3.0e-6)

        alphaAir = Constant(50.) # convection coefficient
        TAir = Constant(300.) # [K] ambient temperature
        THot = Constant(450.) # [K] temperature of heating
        T0 = Constant(320.) # [K] initial temperature

        '''
    st.code(code, language='python')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/tem.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение температуры')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/s1.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение напряжений по xx')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/s4.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение напряжений по xy')


    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/ux.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений по x')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/uy.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений по y')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/um2.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений')



