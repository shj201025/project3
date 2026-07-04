import streamlit as st

st.set_page_config(page_title="계산기", page_icon="🧮")

st.title("🧮 간단 계산기")

# 입력
num1 = st.number_input("첫 번째 숫자", value=0.0)
num2 = st.number_input("두 번째 숫자", value=0.0)

# 연산 선택
op = st.selectbox("연산 선택", ["+", "-", "*", "/"])

# 버튼
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
