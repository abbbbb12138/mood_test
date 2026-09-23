import streamlit as st

st.title("今日心情小测试")

with st.form("mood_form"):
    mood_index = st.number_input(
        "请输入您今天的心情：",
        min_value=0.0,
        max_value=100.0,
        value=None,
        placeholder="请输入0-100之间的数字"
    )

    at_home = st.selectbox(
        "您今天是否在家：",
        ["yes", "no"]
    )

    confirmed = st.form_submit_button("确认")

if confirmed:
    if mood_index is not None:
        if mood_index >= 50 and at_home == "yes":
            st.write("我来找你玩啦！")
        elif mood_index < 50 and at_home == "yes":
            st.write("我马上来安慰你！")
        elif mood_index >= 50 and at_home == "no":
            st.write("好吧，我下次再来找你")
        else:
            st.write("那好吧")
    else:
        st.write("请先输入您的心情指数哦！")