import streamlit as st
import base64
from urllib.parse import urlencode
from core.engine import CareerAIEngine
from core.context_manager import DialogueManager

st.set_page_config(
    page_title="Career Strategy AI",
    page_icon="🚀",
    layout="centered"
)

# ---------------- INIT ----------------
if "engine" not in st.session_state:
    st.session_state.engine = CareerAIEngine()

if "dialogue" not in st.session_state:
    st.session_state.dialogue = DialogueManager()

# ---------------- LOAD BG ----------------
def load_bg(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image = load_bg("assets/ai_coach_image.jpg")

# ---------------- CSS ----------------
st.markdown(f"""
<style>
.stApp {{
    background:
        linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.90)),
        url("data:image/jpg;base64,{bg_image}");
    background-position: center;
    background-repeat: no-repeat;
    background-size: 85%;
}}

.block-container {{
    padding-top: 30px;
}}

.title {{
    text-align: center;
    margin-top: 20px;
    font-size: 40px;
    font-weight: 500;
    color: #1f2937;
}}

.subtitle {{
    text-align: center;
    font-size: 20px;
    color: #4b5563;
    margin-bottom: 25px;
}}

.suggestions {{
    display: flex;
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap;
    margin-top: 25px;
}}

.suggestions a {{
    text-decoration: none;
    background: rgba(255,255,255,0.65);
    padding: 10px 18px;
    border-radius: 20px;
    font-size: 14px;
    color: black;
}}

.suggestions a:hover {{
    background: rgba(255,255,255,0.85);
}}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown('<div class="title">🚀 Career Strategy AI Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered structured career planning & Interview preparation.</div>', unsafe_allow_html=True)

# ---------------- CHAT HISTORY ----------------
for role, message in st.session_state.dialogue.get_buffer():
    with st.chat_message(role.lower()):
        st.markdown(message)

# ---------------- INPUT ----------------
user_input = st.chat_input("Ask about your career growth...")

# ---------------- ICON LINKS ----------------
def make_link(text, prompt):
    params = urlencode({"action": prompt})
    return f'<a href="?{params}">{text}</a>'

st.markdown(f"""
<div class="suggestions">
    {make_link("📈 Build AI roadmap", "Build a structured AI career roadmap for me.")}
    {make_link("🎯 Interview preparation", "Help me prepare for interviews with structured strategy.")}
    {make_link("📄 Resume review", "Review my resume and suggest improvements.")}
    {make_link("🧠 Skill gap analysis", "Analyze my skill gaps and suggest improvements.")}
    {make_link("💼 Career switch strategy", "Create a career switch strategy for me.")}
</div>
""", unsafe_allow_html=True)

# ---------------- QUERY PARAMS ----------------
query_params = st.query_params
icon_input = query_params.get("action")

if icon_input:
    st.query_params.clear()

final_input = user_input or icon_input

# ---------------- PROCESS ----------------
if final_input:

    st.session_state.dialogue.record("User", final_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            result = st.session_state.engine.process(
                st.session_state.dialogue.get_buffer(),
                final_input
            )

            response = result.get("response") if isinstance(result, dict) else result

            st.markdown(response)

    st.session_state.dialogue.record("Assistant", response)