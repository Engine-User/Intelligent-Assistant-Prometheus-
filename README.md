# Prometheus — AI Chatbot Assistant
<img width="1912" height="845" alt="image" src="https://github.com/user-attachments/assets/716609a1-cf2b-4ad0-9356-c77e3f72ca86" />

**Prometheus** is a clean & lightweight **Streamlit** chatbot application powered by the **Dify AI API**. It features a neon-green cyberpunk UI, animated Lottie graphics, and a simple two-page navigation system for chatting and learning about the assistant.

---

## Features

### Chat Interface
- **AI-Powered Conversations** – Sends user messages to the Dify chat API and streams back assistant replies.
- **Conversation Memory** – Maintains `conversation_id` across messages in a session for contextual follow-ups.
- **Message History** – Displays the full user/assistant chat history using Streamlit's native chat components.
- **Fast Inference Speeds** – Probably the quickest AI API responses in terms of Chat replies.

### Sidebar Navigation
- Two custom buttons: **Chat** and **About**.
- Persistent page state via `st.session_state`.
- Sidebar branding: "Your Intelligent Assistant" / "Made by Engineer".
<img width="1456" height="665" alt="image" src="https://github.com/user-attachments/assets/6e13bc51-f4b6-401e-98f5-d455a5f703d2" />

---

## Tech Stack

| Layer | Libraries |
|-------|-----------|
| App Framework | [Streamlit](https://streamlit.io/) |
| AI Backend | [Dify API](https://docs.dify.ai/) |
| Environment Variables | [python-dotenv](https://pypi.org/project/python-dotenv/) |
| Animations | [streamlit-lottie](https://pypi.org/project/streamlit-lottie/), [LottieFiles](https://lottiefiles.com/) |
| HTTP Requests | [requests](https://requests.readthedocs.io/) |

---

> The snippet above assumes the chatbot file is saved as `chat_app.py`. Adjust the filename if you use a different name.

---

## ⚙️ Installation

1. **Navigate to the project root folder:**

   ```bash
   cd "Project-Folder"
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install streamlit streamlit-lottie requests python-dotenv
   ```

4. **Create a `.env` file** in the same directory as the chatbot script and add your Dify API key:

   ```env
   DIFY_API_KEY=your_dify_api_key_here
   ```

   > You can obtain a Dify API key from your Dify application settings.

---

## Usage

Run the Streamlit application from the project root:

```bash
streamlit run chat_app.py
```

Then open your browser at `http://localhost:8501`.

### Workflow
1. Click **Chat** in the sidebar to start a conversation.
2. Type your question in the input box at the bottom.
3. Prometheus will query the Dify API and display the response.
4. Click **About** in the sidebar to learn more about the assistant.

---

## 🔧 Configuration

| Variable | Description |
|----------|-------------|
| `DIFY_API_KEY` | Your Dify application API key (required) |
| Dify API URL | `https://api.dify.ai/v1/chat-messages` (hardcoded in the app) |
| Dify User ID | `aianytime` (hardcoded in the payload) |

To customise the user ID or API endpoint, edit the `payload` dictionary inside the `chat_interface()` function.

---
## Author

**Engineer**  
📧 contact: [ggengineerco@gmail.com](mailto:ggengineerco@gmail.com)

---

## 📜 License

This project is released for educational purposes. Use at your own risk.
