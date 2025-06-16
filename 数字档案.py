import streamlit as st  # 导入Streamlit并用st代表它
import pandas as pd
st.title("🥘庭悦餐馆-数字档案")#命名主题
st.markdown('***')#绘制分割线
st.header("🥟基础信息")#创造一个小标题

#创建普通文本完善信息
st.markdown("   餐馆编号：5201314")
st.markdown("注册时间：:green[2025-06-05]|营业状态：👌正常")
st.markdown("当前位置：:green[芝士院] | 安全等级：⭐⭐⭐⭐⭐")

st.header("🍱特色菜品")
st.subheader("🥰大众喜爱程度 ")
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="老友粉", value="90%")
c2.metric(label="饺子", value="88%")
c3.metric(label="隆江猪脚饭", value="92%")

st.subheader("👩‍🍳主厨推荐 ")
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="锅包肉",value="￥28")
c2.metric(label="避风塘虾",value="￥56")
c3.metric(label="剁椒鱼头",value="￥32")
#自定义一组数据
data = {
    '1号门店':[568, 868, 670, 884, 144],
    '2号门店':[820, 884, 768, 524, 709],
    '3号门店':[577, 532, 996, 929, 694],
}
#创建索引列
index = pd.Series(['01月', '02月', '03月', '04月', '05月'], name='月份')

#将普通数据转换成dataframe数据
df = pd.DataFrame(data, index=index)

st.subheader('🏧每月销售额')
st.dataframe(df)#绘制表格

st.markdown('***')#绘制分割线

st.markdown("餐馆营业执照编码：:green[31415926]")
st.markdown("TARGET：:green[餐饮行业管理系统]")
st.markdown("创建时间：:green[2025-06-05  10:57:53]")
st.markdown("系统状态：在线 连接状态：已加密")
