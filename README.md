# LinkedIn Post Generator AI Agent

An AI-powered LinkedIn post generator built with **LangChain**, **Google Gemini (free tier API)**, and **Streamlit**.

This agent helps you generate highly engaging, structured LinkedIn-style posts (2-4 paragraphs) on any topic and in your selected language.

## Features
- **Topic Input:** Provide any topic (e.g., "AI in Healthcare", "Remote Work Productivity").
- **Language Selection:** Generate posts in English, Bengali, Spanish, Hindi, and more.
- **Modern UI:** Clean, beautiful Streamlit interface with responsive status updates and quick-copy output.
- **LangChain Integration:** Uses a structured LLM chain for prompt management, LLM interfacing, and output parsing.
- **Powered by Gemini:** Uses `gemini-2.0-flash` through Google AI Studio (free API key).

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd linkedin-post-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API Key:**
   - Create a `.env` file in the root directory:
     ```bash
     cp .env.example .env
     ```
   - Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).
   - Paste your key into the `.env` file:
     ```env
     GOOGLE_API_KEY=your_actual_api_key_here
     ```

4. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

## Tech Stack
- **Framework:** Streamlit (UI)
- **AI Orchestration:** LangChain
- **LLM Provider:** Google Generative AI (`gemini-2.0-flash`)
- **Environment Management:** python-dotenv
