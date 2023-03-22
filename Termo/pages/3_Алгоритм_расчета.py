import streamlit as st


menu = st.sidebar.radio('***',
    (
        'Теплопроводность','Упругость',)
)

if menu == 'Теплопроводность':

    r"""
    ## Алгоритм расчета теплопроводности
    - #### Стационарное уравнение теплопроводности (строгое)
    $$
    -(\vec{\nabla}\cdotp \vec{q})+Q = 0 \\ \vec{q} = -k\overrightarrow{\nabla u}
    $$"""
    expander = st.expander(" Используемые переменные ")
    expander.write (r""" $$T$$- поле температуры  $$\\ k$$- коэффициент теплопроводности$$  \\ Q$$- объемный источник тепла  $$\\ \vec{q}$$- тепловой поток """)
    r"""
    - ### Слабая форма 
    $$
    \textcolor{green} {\int_\varOmega k\cdotp (\vec{\nabla} w \cdotp \vec{\nabla} T )d\varOmega =} \textcolor{blue} {\int_\varOmega w\cdotp Q d\varOmega}  
    $$"""
    expander = st.expander(" Используемые переменные ")
    expander.write ( r"""$$w-$$тестовая функция""")
    r"""
    - #### Решается данное уравнение методом конечных элементов
    - #### FEniCS решает задачу в канонической форме вида
    $$\quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad$$ $$a(u,w)=L(w) $$"""
    expander = st.expander(" Используемые переменные ")
    expander.write(r"""  $$a(u,w)$$-  билинейная форма $$\\$$ $$L(w)$$- линейная форма""")
    """- #### Программная реализация для решения дифференциального уравнения в FEniCS
    eq_tem = $$ \textcolor{green}{(k\_ *inner (nabla\_grad(tem), nabla\_grad(q))* dx} - \textcolor{blue}{heat\_source *q *dx} $$\
    a\_therm = lhs(eq\_tem)\
    L\_therm= rhs(eq\_tem)
    """

if menu == 'Упругость':
    r"""
    # Алгоритм расчета упругости
    - #### Уравнение Гука (упругости) в строгой форме
    $$
    div\sigma = 0\\
    \textcolor{red}{\sigma} = \lambda\thetasym I + 2\mu\varepsilon^{el} \\ \varepsilon = \varepsilon^{el}+\textcolor{violet}{\varepsilon^{th}}\\
    \textcolor{blue} {\varepsilon} = \frac{1}{2}\cdotp (\nabla{u} + (\nabla u)^{T})\\
    \textcolor{violet} {\varepsilon^{th}} = [(3\lambda + 2\mu) \alpha(T-T_{ref})]I
    """
    expander = st.expander(" Используемые переменные ")
    expander.write (
    r""" 
    $$\lambda$$ -первый коэффициент Ламе \
    $$\mu$$ - второй коэффициент Ламе\
    $$\varepsilon^{el}$$ - линейный тензор упругой деформации \
    $$\thetasym$$ = $$tr(\varepsilon^{el})$$ - первый инвариант линейного тензора упругой деформации (объемное расширение в линейном приближении)\
    I - единичная диагональная матрица$$\\$$ $$\alpha$$ - коэффициент теплового расширения\
    $$T_{ref}$$ - температура, при которой материал имеет свой нормальный объем
    
    """)
    r"""
    - #### Слабая форма (решается методом конечных элементов)
    $$
    \textcolor{green}{\int_{\varOmega} \sigma:\varepsilon dx} =\textcolor{yellow} {\int_{\delta\varOmega_T}Tvd(s)},
    $$"""
    expander = st.expander(" Используемые переменные ")
    expander.write ( r""" $$ T-$$ усилие\
    $$V-$$ тестовая функция """)
    r"""  - #### Программная реализация для решения дифференциального уравнения в FEniCS
    $$
    \textcolor{red}{sigma\_=}lambda\_ *nabla\_div(u) *identity(d2) + mu *(nabla\_grad(u))+nabla\_grad(u).T\\
    -(3 *lambda\_ + 2*mu)*alpha *(tem\_n - tem\_ref) *identity(d1)\\
    \textcolor{blue}{epsilon\_} = 0.5 *(nabla\_grad(v) + nabla\_grad(v).T)\\
    elastic\_eqn = \textcolor{green}{inner(sigma\_,epsilon\_)* dx} \textcolor{yellow}{- dot(Traction,v)* ds}\\
    a\_elas = lhs(elastic\_eqn)\\
    L\_elas = rhs (elastic\_eqn)
    $$
    """