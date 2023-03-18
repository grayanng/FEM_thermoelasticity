import streamlit as st

r"""
## Алгортм расчета: теплопроводность
- #### Стационарное уравнение теплопроводности (строгое)
$$
-(\vec{\nabla}\cdotp \vec{q})+Q = 0 \vec{q} = -k\overrightarrow{\nabla u},
$$
где T- поле температуры, k- коэффициент теплопроводности, Q- объемный источник тепла , $$\vec{q}$$- тепловой поток;
- Слабая форма: 
$$
\int_\varOmega k\cdotp (\vec{\nabla} w \cdotp \vec{\nabla} T )d\varOmega = \int_\varOmega w\cdotp Q d\varOmega,  
$$
где w-тестовая функция;
- #### Решается данное уравнение методом конечных элементов
- #### FEniCS решает задачу в канонической форме вида:
a(u,w)=L(w), где a(u,w)-  билинейная форма, L(w)- линейная форма.
- #### Программная реализация для решения дифференциального уравнения в FEniCS:
eq_tem = $$ \textcolor{red} {q*(tem-tem_n)/dt* dx} + \textcolor{green}{(k_ *inner (nabla_grad(tem), nabla_grad(q))* dx} - \textcolor{blue}{heat_source *q *dx} $$\
a_therm = lhs(eq_tem)\
L_therm= rhs(eq_tem)
"""