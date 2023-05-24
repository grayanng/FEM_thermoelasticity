import streamlit as st
from PIL import Image
import os.path
import sys
import matplotlib.pyplot as plt
from dolfin import *
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

menu = st.sidebar.radio('***',
    (   '3D',)
)

if menu == "3D":

    r'''
    ### Параметры образца
    '''

    code = '''
    Lx = 1  
    Ly = 1.2  
    Lz = 1

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



    """
    # Результат численного моделирования

    """

    path_to_imag e= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/temv0.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение температуры')

    path_to_imag e= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/s1.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение напряжений по xx')

    path_to_imag e= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/s4.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение напряжений по xy')

    path_to_imag e= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/ux.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений по x')

    path_to_imag e= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/uy.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений по y')

    path_to_videos = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/um.mp4')
    video_file = open(path_to_videos, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

