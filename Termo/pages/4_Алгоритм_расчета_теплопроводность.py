import streamlit as st

r"""
## Алгортм расчета: теплопроводность
- #### Стационарное уравнение теплопроводности (строгое)
$$
-(\vec{\nabla}\cdotp \vec{q})+Q = 0 \\ \vec{q} = -k\overrightarrow{\nabla u},
$$
где $$T$$- поле температуры, $$k$$- коэффициент теплопроводности, $$Q$$- объемный источник тепла , $$\vec{q}$$- тепловой поток;
- ### Слабая форма: 
$$
\textcolor{green} {\int_\varOmega k\cdotp (\vec{\nabla} w \cdotp \vec{\nabla} T )d\varOmega =} \textcolor{blue} {\int_\varOmega w\cdotp Q d\varOmega},  
$$
где $$w$$-тестовая функция;
- #### Решается данное уравнение методом конечных элементов
- #### FEniCS решает задачу в канонической форме вида:
$$a(u,w)=L(w),$$ где $$a(u,w)$$-  билинейная форма, $$L(w)$$- линейная форма.
- #### Программная реализация для решения дифференциального уравнения в FEniCS:
eq_tem = $$ \textcolor{green}{(k\_ *inner (nabla\_grad(tem), nabla\_grad(q))* dx} - \textcolor{blue}{heat\_source *q *dx} $$\
a\_therm = lhs(eq\_tem)\
L\_therm= rhs(eq\_tem)
"""