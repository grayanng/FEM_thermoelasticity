import streamlit as st

r"""
# Алгоритм расчета: упругость
- Уравнение Гука (упругости) в строгой форме:
$$
div\sigma = 0\\
\textcolor{red}{\sigma} = \lambda\thetasym I + 2\mu\varepsilon^{el}  \varepsilon = \varepsilon^{el}+\varepsilon^{th}\\
\textcolor{blue} {\varepsilon} = \frac{1}{2}\cdotp (\nabla{u} + (\nabla u)^{T})\\
\textcolor{violet} {\varepsilon^{th}} = [(3\lambda + 2\mu) \alpha(T-T_{ref})]I,
$$
где $$\lambda$$-первый коэффициент Ламе, $$\mu$$ - второй коэффициент Ламе, $$\varepsilon^{el}$$ - линейный тензор упругой деформации, 
$$\thetasym$$ = $$tr(\varepsilon^{el})$$ - первый инвариант линейного тензора упругой деформации (объемное расширение в линейном приближении)
I - единичная диагональная матрица, $$\alpha$$ - коэффициент теплового расширения,$$T_{ref}$$ - температура, при которой материал имеет свой нормальный объем
- Слабая форма (решается методом конечных элементов):
$$
\textcolor{green}{\int_{\varOmega} \sigma:\varepsilon dx} =\textcolor{yellow} {\int_{\delta\varOmega_T}Tvd(s)},
$$
где T-усилие, V-тестовая функция
- Программная реализация для решения дифференциального уравнения в FEniCS:
$$
\textcolor{red}{sigma\_=}lambda\_ *nabla\_div(u) *identity(d2) + mu *(nabla\_grad(u))+nabla\_grad(u).T\\
-(3 *lambda\_ + 2*mu)*alpha *(tem\_n - tem\_ref) *identity(d1)\\
\textcolor{blue}{epsilon\_} = 0.5 *(nabla\_grad(v) + nabla\_grad(v).T)\\
elastic\_eqn = \textcolor{green}{inner(sigma\_,epsilon\_)* dx} \textcolor{yellow}{- dot(Traction,v)* ds}\\
a\_elas = lhs(elastic\_eqn)\\
L\_elas = rhs (elastic\_eqn)
$$
"""