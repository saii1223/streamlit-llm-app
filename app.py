from dotenv import load_dotenv
load_dotenv()



import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate   
st.title("専門家アシスタントアプリ")
st.write("このアプリは、選択した専門家の視点から質問に回答します。以下の手順で操作してください。")
st.write("1. 専門家の種類をラジオボタンで選択します。")
st.write("2. 入力フォームに質問を入力します。")
st.write("3. 「実行」ボタンを押すと、選択した専門家の視点からの回答が表示されます。")
def get_expert_response(expert_type: str, user_input: str) -> str:
    if expert_type == "医療専門家":
        system_message = SystemMessage(content="あなたは医療の専門家です。健康に関する質問に対して、正確で信頼できる情報を提供してください。")
    else:
        system_message = SystemMessage(content="あなたは法律の専門家です。法律に関する質問に対して、正確で信頼できる情報を提供してください。")
    
    chat = ChatOpenAI(temperature=0)
    messages = [
        system_message,
        HumanMessage(content=user_input)
    ]
    response = chat(messages)
    return response.content
selected_expert = st.radio(
    "専門家の種類を選択してください。",
    ["医療専門家", "法律専門家"]
)
user_question = st.text_input(label="質問を入力してください。")
if st.button("実行"):
    st.divider()
    if user_question:
        answer = get_expert_response(selected_expert, user_question)
        st.write(f"**回答:** {answer}")
    else:
        st.error("質問を入力してから「実行」ボタンを押してください。")
