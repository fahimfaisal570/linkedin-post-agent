# LinkedIn Post Generator AI Agent

An AI-powered LinkedIn post generator built with **LangChain**, **Google Gemini (free tier API)**, and **Streamlit**.

This agent takes a topic, language, and tone to generate structured, engaging, 2-4 paragraph professional LinkedIn posts.

## Repository Contents
- **`app.py`**: The main application code containing the Streamlit UI design, input forms, and LangChain orchestration.
- **`requirements.txt`**: List of dependencies (`langchain`, `langchain-google-genai`, `streamlit`, `python-dotenv`).
- **`.env.example`**: Template for setting up environment variables.
- **`.gitignore`**: Files ignored by Git (such as virtual environments and your private `.env` secrets file).
- **`demo_recording.mp4`**: Compressed demo video showing the application in action.

---

## How to Set Up and Run the App

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fahimfaisal570/linkedin-post-agent.git
   cd linkedin-post-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the API Key:**
   - Create a `.env` file in the root directory:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and add your Gemini API key:
     ```env
     GOOGLE_API_KEY=your_gemini_api_key_here
     ```

4. **Launch the Web App:**
   ```bash
   streamlit run app.py
   ```
   This will automatically open the app in your browser at `http://localhost:8501`.

---

## Demo Video
You can watch the demo video file `demo_recording.mp4` included directly inside the repository!
