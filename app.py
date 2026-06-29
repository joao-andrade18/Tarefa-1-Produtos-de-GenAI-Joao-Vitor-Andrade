import streamlit as st

from services.llm import gerar_resposta


st.set_page_config(
    page_title="Chatbot NVIDIA",
    page_icon="🤖",
    layout="centered",
)


st.title("🤖 Chatbot com IA Generativa NVIDIA")
st.write(
    "Aplicação desenvolvida em Python com Streamlit utilizando um modelo "
    "open source disponibilizado pela NVIDIA."
)


if "messages" not in st.session_state:
    st.session_state.messages = []


with st.sidebar:
    st.header("Configurações")
    st.write("Modelo utilizado:")
    st.code("meta/llama-3.1-8b-instruct")

    if st.button("Limpar conversa"):
        st.session_state.messages = []
        st.rerun()


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


pergunta = st.chat_input("Digite sua pergunta...")

if pergunta:
    st.session_state.messages.append(
        {"role": "user", "content": pergunta}
    )

    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                resposta = gerar_resposta(st.session_state.messages)
                st.markdown(resposta)

                st.session_state.messages.append(
                    {"role": "assistant", "content": resposta}
                )

            except Exception as erro:
                mensagem_erro = (
                    "Ocorreu um erro ao consultar o modelo. "
                    "Verifique sua chave da NVIDIA e sua conexão com a internet."
                )
                st.error(mensagem_erro)
                st.exception(erro)