import streamlit as st

st.set_page_config(page_title="계산기", page_icon="🧮")

st.title("🧮 간단한 계산기")

num1 = st.number_input("첫 번째 숫자")
num2 = st.number_input("두 번째 숫자")

op = st.selectbox("연산 선택", ["+", "-", "*", "/"])

if st.button("계산하기"):
    if op == "+":
        result = num1 + num2
        st.success(f"결과: {result}")

    elif op == "-":
        result = num1 - num2
        st.success(f"결과: {result}")

    elif op == "*":
        result = num1 * num2
        st.success(f"결과: {result}")

    elif op == "/":
        if num2 == 0:
            st.error("0으로 나눌 수 없습니다 ❌")
        else:
            result = num1 / num2
            st.success(f"결과: {result}")
