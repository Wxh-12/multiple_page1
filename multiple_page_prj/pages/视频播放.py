import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title='视频播放器', page_icon='📺')
st.title("📽Seamlit视频播放器")

st.header("视频库")

video_obj =[{'动画': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4'},
{'自然动物': 'https://www.w3schools.com/html/movie.mp4'},
{'动漫': 'https://media.w3.org/2010/05/sintel/trailer.mp4'}]


# 自定义format_func函数
def my_format_func(option):
    return f'{option}视频'

st.header('视频播放')
video = st.selectbox('点击选择你要播放的视频：', ['动画', '自然动物', '动漫'], format_func=my_format_func, index=2)
# 根据返回值不同，选择不同的特色回答
# 同时应注意返回值不受自定义my_format_func
if video == '动画':
    st.video(video_obj[0]["动画"])
elif video == '自然动物':
    st.video(video_obj[1]["自然动物"])
else:
    st.video(video_obj[2]["动漫"])
