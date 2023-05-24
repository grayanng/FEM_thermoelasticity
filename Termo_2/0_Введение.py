import streamlit as st
from PIL import Image
import os.path

menu = st.sidebar.radio('***',
    (
    'Решение совместной задачи термоупругости',
     'Мотивация')
)
if (menu=='Решение совместной задачи термоупругости'):
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        path_to_image_2 = os.path.join(os.path.dirname((__file__)), 'images', 'MSU.png')
        image = Image.open(path_to_image_2)
        st.image(image, caption='',output_format=('auto'))
    r"""
    # Образовательны проект на тему
    ### Решение совместной задачи термоупругости образца, подверженному  стационарному нагреву 
    
    ## Проект команды №3
    
    Выполнили студенты группы ВМ-122
    - Харин Александр Николаевич
    - Муллин Георгий Денисович
    - Пономаренко Дмитрий Сергеевич
    - Сизая Анжелика  Владимировна
    """
if (menu=='Мотивация'):
    path_to_image= os.path.join(os.path.dirname(__file__), 'images','Task_3.png')
    image = Image.open(path_to_image)
    r"""
    # Мотивация
   При механических и тепловых воздействиях в упругом теле возникают поля перемещений u, деформаций ε и напряжений σ, 
   что приводит к изменению распределения температуры в отдельных элементах конструкций зданий и сооружений. 
   Эти изменения вызывают температурные воздействия на конструкции зданий, которые необходимо учитывать при их проектировании.
    """
    st.image(image,use_column_width='Auto',caption='Конструкция здания')