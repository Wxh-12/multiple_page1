#首先导入所需函数库
import streamlit as st
from PIL import Image
import io
#网络页面设置
st.set_page_config(page_title='个人简历生成器', page_icon='🎨',layout='wide')
st.title("🎨个人简历生成器")#设置标题
c1, c2 = st.columns([1,2])#将页面分为两列
#第一列的内容
with c1:   
    st.subheader('个人信息表单')
    st.markdown('***')#分割线
    #单行输入文本框
    st.text_input('姓名：', autocomplete='name')
    st.text_input('职位', autocomplete='name')
    st.text_input('电话',"" )
    st.text_input('邮箱', value='')
    st.date_input("出生日期", value=None)
    st.write('性别')
    sex = st.radio(
    "你的性别是",
    ['男', '女', '其他'],
    horizontal=True,
    label_visibility='hidden'
    )#设置性别选择按钮
    st.write('学历')
    xl = st.selectbox(
    '学历',
    ['高职', '本科', '硕士','博士'],
    label_visibility='collapsed'
)#设置下拉按钮
    st.write('语言能力')
    yy = st.selectbox(
    '语言能力',
    ['汉语', '英语', '韩语','俄语','其他'],
    label_visibility='collapsed'
)
    #自定义功能函数
    def my_format_func(option):
         return f'{option}'
    st.write('技能(可多选)')
    #设置下拉多选按钮
    options_1 = st.multiselect(
    '技能',
    ['C语言', 'JAVA语言', 'Python', '数据库'],
    ['C语言', 'JAVA语言'],
    format_func=my_format_func,
    label_visibility='collapsed'
    )
    #设置滑块组件
    st.write('工作经验(年)')
    ex = st.slider('经验', 0, 30,label_visibility='collapsed')
 
    st.write('期望薪资范围(元)')
    values = st.slider(
    '选择范围',
    5000,50000,(10000,20000),label_visibility='collapsed' )
#设置文本输入框，图片上传器
    st.text_area(label='个人简介', placeholder='请简要介绍你的专业背景、职业目标和个人特点')
    st.write('每日最佳联系时间段')
    w1 = st.time_input("时间1",label_visibility='collapsed')
    uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png", "gif"])
#第二列内容
with c2:    
    st.subheader("简历实时预览")
    st.markdown('***')
    c3,c4=st.columns(2)#在第二列中重新分出两列
    with c3:
        zw = st.text_input('职位：')
        numbers = st.text_input('电话', autocomplete='numbers')
        st.text_input('邮箱', placeholder='这是一个邮箱')
        date1 = st.date_input("出生年月", value=None)
    with c4:
        st.text_input('性别：', autocomplete='sex')
        st.text_input('学历', autocomplete='name')
        st.text_input('期望薪资',"" )
        st.time_input("最佳联系时间")
        st.text_input('语言能力',"" )
    st.markdown('***')#分割线
    st.text_area(label='个人简介：', placeholder='这个人很神秘，没有留下任何介绍....')
    st.markdown('***')
    st.caption('<center>代码改变世界，你改变代码</center>',unsafe_allow_html=True)

