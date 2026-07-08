import os
import sys
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from streamlit.runtime import exists as streamlit_exists

# Load environment variables (local .env)
load_dotenv()

# Set up standard generation function so it's clean and testable
# ponytail: keep logic separate from UI for clean structure
def generate_linkedin_post(api_key, topic, language, tone):
    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "You are an expert content creator and social media manager. "
            "Your task is to write a highly professional, engaging, and structured LinkedIn post based on the user's prompt.\n\n"
            "Rules:\n"
            "- The post must be written in {language}.\n"
            "- The tone must be {tone}.\n"
            "- The length must be strictly between 2 to 4 paragraphs.\n"
            "- Make the post highly engaging, include bullet points where appropriate, and end with relevant hashtags and a call-to-action.\n"
            "- Do not use any introductory conversational filler like 'Here is your post:'."
        )),
        ("user", "Create a LinkedIn post about: {topic}")
    ])

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",
        google_api_key=api_key,
        temperature=0.7
    )
    
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({
        "language": language,
        "tone": tone,
        "topic": topic
    })

# If running as Streamlit UI
if streamlit_exists():
    st.set_page_config(
        page_title="LinkedIn Post AI Agent",
        page_icon="🤖",
        layout="centered"
    )

    # Premium Custom CSS for aesthetics (glassmorphism, gradient buttons, fonts)
    # ponytail: simple css styling to satisfy the visual requirements without bloated external CSS framework
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
        }
        
        .stApp {
            background: radial-gradient(circle at top left, #1e1b4b, #0f172a, #020617);
            color: #f8fafc;
        }
        
        /* Input adjustments */
        div[data-baseweb="input"] {
            background-color: rgba(30, 41, 59, 0.5) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 12px !important;
            backdrop-filter: blur(10px);
        }
        
        /* Selectbox adjustments */
        div[data-baseweb="select"] {
            background-color: rgba(30, 41, 59, 0.5) !important;
            border-radius: 12px !important;
        }
        
        /* Card design for generated post */
        .post-container {
            background: rgba(30, 41, 59, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            backdrop-filter: blur(12px);
            margin-top: 20px;
            border-left: 5px solid #6366f1;
            transition: all 0.3s ease;
        }
        
        .post-container:hover {
            transform: translateY(-2px);
            border-left: 5px solid #818cf8;
            box-shadow: 0 12px 40px 0 rgba(99, 102, 241, 0.15);
        }
    </style>
    """, unsafe_allow_html=True)

    # Title & Description
    st.write(
        """
        <div style="text-align: center; padding: 20px 0 10px 0;">
            <h1 style="font-weight: 800; font-size: 3rem; background: linear-gradient(135deg, #a5b4fc, #6366f1, #4338ca); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                🤖 LinkedIn Post AI Agent
            </h1>
            <p style="color: #94a3b8; font-size: 1.1rem; margin-top: -10px;">
                Generate highly engaging, professional LinkedIn posts with LangChain and Google Gemini
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # API Key Validation / Input
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        try:
            if "GOOGLE_API_KEY" in st.secrets:
                api_key = st.secrets["GOOGLE_API_KEY"]
        except Exception:
            pass

    if not api_key:
        st.sidebar.warning("🔑 Google API Key not found in Environment or Secrets.")
        api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")
        if api_key:
            os.environ["GOOGLE_API_KEY"] = api_key

    # Form Layout
    with st.container():
        st.markdown('<div style="background: rgba(30, 41, 59, 0.3); padding: 20px; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.05); margin-bottom: 25px;">', unsafe_allow_html=True)
        
        topic = st.text_input("📝 What is the topic of the post?", placeholder="e.g., AI in Healthcare, Remote Work Productivity")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            language = st.selectbox(
                "🌐 Language",
                ["English", "Bengali", "Spanish", "French", "German", "Hindi", "Japanese"]
            )
        with col2:
            tone = st.selectbox(
                "🎭 Tone",
                ["Professional", "Casual", "Inspiring", "Informative", "Humorous"]
            )
            
        generate_btn = st.button("🚀 Generate Post", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Post Generation Logic
    if generate_btn:
        if not api_key:
            st.error("❌ Please provide a Google API Key in the sidebar or setup a `.env` file.")
        elif not topic.strip():
            st.warning("⚠️ Please enter a topic first.")
        else:
            with st.spinner("🧠 Agent is thinking & writing..."):
                try:
                    response = generate_linkedin_post(api_key, topic, language, tone)
                    st.success("✅ Post generated successfully!")
                    
                    st.markdown(f"""
                    <div class="post-container">
                        <div style="font-weight: 600; font-size: 0.85rem; color: #818cf8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 12px;">Generated Post</div>
                        <div style="white-space: pre-wrap; line-height: 1.6; font-size: 1.05rem; color: #e2e8f0;">{response}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.code(response, language="text")
                    
                except Exception as e:
                    st.error(f"💥 An error occurred: {str(e)}")

# Self-check CLI utility
if __name__ == "__main__" and not streamlit_exists():
    if len(sys.argv) > 1 and sys.argv[1] == "--self-check":
        print("Running self-check...")
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            print("ERROR: GOOGLE_API_KEY is not set.")
            sys.exit(1)
        
        try:
            result = generate_linkedin_post(api_key, "AI Agent Verification Test", "English", "Professional")
            print(f"Self-check SUCCESS! Result:\n{result}")
            sys.exit(0)
        except Exception as err:
            print(f"Self-check FAILED: {err}")
            sys.exit(1)
