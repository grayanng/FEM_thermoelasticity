import streamlit as st
from PIL import Image
import numpy as np
import os.path
r"""
# Передача видео в Streamlit
"""

path_to_audio = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'audio', 'music.mp3')
path_to_videos= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos', 'sample-5s.mp4')
video_file = open(path_to_videos, 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
expander = st.expander("Как вывести видео в Streamlit")
expander.write ( r"""
```python

path_to_audio = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'audio', 'music.mp3')
path_to_videos= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos', 'sample-5s.mp4')
video_file = open(path_to_videos, 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
```
""")

r"""
# Передача аудио в Streamlit
"""

audio_file = open(path_to_audio, 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')

expander = st.expander("Как вывести аудио в Streamlit")
expander.write ("""
    ```python
    audio_file = open(path_to_audio, 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')
                """)