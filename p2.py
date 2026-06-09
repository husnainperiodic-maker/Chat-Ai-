from groq import Groq
import streamlit as st

st.set_page_config(page_title="Chat AI", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: black;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    background: #111;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 35px;
    font-weight: bold;
    color: #00ffcc;
    border: 2px solid #00ffcc;
    box-shadow: 0px 0px 20px #00ffcc50;
">
Welcome Chat With AI 🤖
</div>
""", unsafe_allow_html=True)
client = Groq(api_key="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")

st.markdown("""
<style>
.custom-write {
    font-size: 18px;
    color: white;
    background: #111;
    padding: 10px;
    border-radius: 10px;
    border-left: 4px solid #00ffcc;
    border-right: 4px solid #00ffcc;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-write">Enjoy Chat with AI 🚀</div>', unsafe_allow_html=True)
st.markdown("""
<style>
.custom-write {
    font-size: 18px;
    color: white;
    background: #111;
    padding: 10px;
    border-radius: 10px;
    border-left: 4px solid #00ffcc;
    border-right: 4px solid #00ffcc;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-write">Type Exit to stop 🚀</div>', unsafe_allow_html=True)
st.markdown("""
<style>
.custom-write {
    font-size: 18px;
    color: white;
    background: #111;
    padding: 10px;
    border-radius: 10px;
    border-left: 4px solid #00ffcc;
    border-right: 4px solid #00ffcc;
    margin-bottom: 1px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="Ask Any Question 🚀</div>', unsafe_allow_html=True)
if "history" not in st.session_state:
    st.session_state.history = []

st.markdown("""
<style>
.stTextInput > div > div > input {
    font-size: 18px;
    color: white;
    background: #111;
    padding: 10px;
    border-radius: 10px;
    border-left: 4px solid #00ffcc;
    border-right: 4px solid #00ffcc;
    margin-bottom: 1px;
}

.stTextInput > label {
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

user = st.text_input("Ask your question:")

if user.strip():

    if user.lower() == "exit":
        st.write("Chat Over")
        st.stop()

    st.session_state.history.append({"role": "user", "content": user})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.history
    )

    reply = response.choices[0].message.content

    st.session_state.history.append({"role": "assistant", "content": reply})

    st.success("AI:")
    st.success(reply)