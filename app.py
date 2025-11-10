from dotenv import load_dotenv
load_dotenv()

import streamlit as st

st.title("【提出課題】LLM機能を搭載したWebアプリ")

st.write("LLMに専門家として振る舞ってもらう分野を選択し、質問に答えてもらうWebアプリです。")

selected_option = st.radio(
    "**分野を選択してください。**",
    ["映画", "音楽"]
)

st.divider()

input_message = st.text_input(label="**質問を入力してください。**")

# LangChainを使って回答を生成
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

message = [
    SystemMessage(content=f"あなたは{selected_option}の専門家です。"),
    HumanMessage(content=input_message)
]
result = llm(message)

# 実行ボタンが押されたら回答を表示
if st.button("実行"):
    st.divider()
    st.write("**回答**")
    st.write(result.content)
