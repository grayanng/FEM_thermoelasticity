import streamlit as st
import matplotlib.pyplot as plt
from numpy import *
import scipy
import scipy.interpolate


def spline_interpolation(xi, yi, x):
    n = xi.shape[0] - 1
    hi = xi[1:] - xi[:n]
    ai = yi[:n]

    A = zeros((n - 1, n - 1))

    for i in range(0, n - 1):
        if i > 0:
            A[i][i - 1] = hi[i]

        A[i][i] = 2 * (hi[i] + hi[i + 1])

        if i < n - 2:
            A[i][i + 1] = hi[i + 1]

    b = 6 * ((yi[2:] - yi[1:n]) / hi[1:] - (yi[1:n] - yi[:n - 1]) / hi[:n - 1])

    ci = linalg.solve(A, b)

    ci = append(ci, 0)
    ci = insert(ci, 0, 0)

    bi = (yi[1:] - yi[:n]) / hi - hi / 6 * (ci[1:] + 2 * ci[:n])

    di = (ci[1:] - ci[:n]) / hi

    s_xi = xi[:n]
    y = zeros(x.shape)

    f = lambda a, b, c, d, x0, x: a + b * (x - x0) + c / 2 * (x - x0) ** 2 + d / 6 * (x - x0) ** 3

    for i in range(x.shape[0]):
        index = where(s_xi <= x[i])[0][-1]
        y[i] = f(ai[index], bi[index], ci[index], di[index], xi[index], x[i])

    return y


"""
# Параметрические расчеты
"""

formula = st.text_input("Функция", "(1 + 25 * x ** 2) ** -1")
segment = st.slider("Отрезок интерполирования", -3., 3., (-1., 1.), 0.2)
n = st.slider("Количество узлов интерполирования", 2, 20, 7)

g = lambda x: eval(formula)

x = linspace(*segment, int((segment[1] - segment[0]) * 100))
y = g(x)

xi = linspace(*segment, n)
yi = g(xi)

my_y = spline_interpolation(xi, yi, x)

f = scipy.interpolate.CubicSpline(xi, yi, bc_type="natural")
sp_y = f(x)


fig, ax = plt.subplots(1, 1)

ax.plot(x, y)
ax.plot(x, my_y)
ax.plot(x, sp_y)
ax.plot(x, y - my_y)
ax.plot(x, y - sp_y)

ax.set_xlabel("$x$")
ax.set_ylabel(formula)
ax.legend(["f", "my_spline", "CubicSpline", "f - my_spline", "f - CubicSpline"])
ax.grid()

st.pyplot(fig)


fig, ax = plt.subplots(1, 1)

ax.plot(x, y)
ax.plot(x, my_y)
ax.plot(x, y - my_y)

ax.set_xlabel("$x$")
ax.set_ylabel(formula)
ax.legend(["f", "my_spline", "f - my_spline"])
ax.grid()

st.pyplot(fig)


fig, ax = plt.subplots(1, 1)

ax.plot(x, y)
ax.plot(x, sp_y)
ax.plot(x, y - sp_y)

ax.set_xlabel("$x$")
ax.set_ylabel(formula)
ax.legend(["f", "CubicSpline", "f - CubicSpline"])
ax.grid()

st.pyplot(fig)



