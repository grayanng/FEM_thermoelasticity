import streamlit as st

r'''
# Пример написания с помощью LATEX

$$
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right)
\\
x = \begin{cases}
   a &\text{if } b \\
   c &\text{if } d
\end{cases}
$$

## Решение интеграла сложной функции
$$
\int arctg (\sqrt[3] {6x-1})=\frac{1}{6}\left((6x-1)arctg (\sqrt[3] {6x-1})-\frac{arctg (\sqrt[3] {(6x-1)^2})}{2}+\frac{1}{2} ln(arctg (\sqrt[3] {(6x-1)^2})+1)+C
\right),  
$$
 где $$С= const$$)'''
expander = st.expander("Как писать на LATEX")
expander.write ( r""" ```Python
$$
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right)
\\
x = \begin{cases}
   a &\text{if } b \\
   c &\text{if } d
\end{cases}
$$
$$
\int arctg (\sqrt[3] {6x-1})=\frac{1}{6}\left((6x-1)arctg (\sqrt[3] {6x-1})-\frac{arctg (\sqrt[3] {(6x-1)^2})}{2}+\frac{1}{2} ln(arctg (\sqrt[3] {(6x-1)^2})+1)+C
\right),  
$$
""")

