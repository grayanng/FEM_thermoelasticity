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

audio_file = open(path_to_audio, 'rb')
audio_bytes = audio_file.read()
r"""
# Передача аудио в Streamlit
"""
st.audio(audio_bytes, format='audio/mp3')
