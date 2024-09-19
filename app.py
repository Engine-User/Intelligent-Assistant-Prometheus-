import requests
import streamlit as st
from streamlit_lottie import st_lottie
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

# Get the Dify API key from environment variables
dify_api_key = os.getenv("DIFY_API_KEY")

# Custom CSS for enhancing the UI
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Caesar+Dressing&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Caesar Dressing', cursive !important;
        color: #39FF14 !important;
        font-weight: bold;
    }
    
    .stButton > button {
        font-family: 'Caesar Dressing', cursive !important;
        background-color: #39FF14;
        color: black !important;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 12px;
        border: 2px solid #39FF14;
    }
    
    .stButton > button:hover {
        background-color: black;
        color: #39FF14 !important;
        border: 2px solid #39FF14;
        box-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14, 0 0 30px #39FF14;
    }
    
    .css-1d391kg {
        padding: 2rem 1rem;
    }
    
    .css-1v0mbdj {
        width: 100%;
        padding: 1.5rem;
        border-radius: 10px;
    }
    
    .css-1v0mbdj:hover {
        box-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14, 0 0 30px #39FF14;
        transition: 0.3s;
    }
    
    .particles-js-canvas-el {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }

    .title {
        font-family: 'Caesar Dressing', cursive !important;
        font-size: 48px;
        text-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14, 0 0 30px #39FF14;
        transition: all 0.3s ease;
    }

    .title:hover {
        transform: scale(1.1);
        text-shadow: 0 0 20px #39FF14, 0 0 40px #39FF14, 0 0 60px #39FF14;
    }

    .sidebar-block {
        background-color: rgba(57, 255, 20, 0.1);
        border-radius: 10px;
        padding: 10px;
        transition: all 0.3s ease;
    }

    .sidebar-block:hover {
        background-color: rgba(57, 255, 20, 0.2);
        box-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14, 0 0 30px #39FF14;
    }

    .sidebar-text {
        font-family: 'Caesar Dressing', cursive !important;
        font-size: 24px;
        color: #39FF14 !important;
        transition: all 0.3s ease;
    }

    .sidebar-text:hover {
        transform: scale(1.1);
        text-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14, 0 0 30px #39FF14;
    }

    .stTextInput > div > div > input {
        font-family: 'Caesar Dressing', cursive !important;
        color: #39FF14 !important;
    }

    .stTextInput > div > div > button {
        background-color: red !important;
    }

    .stRadio > div {
        font-family: 'Caesar Dressing', cursive !important;
        color: #39FF14 !important;
    }

    .stMarkdown {
        font-family: 'Caesar Dressing', cursive !important;
        color: #39FF14 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Add particles.js for background animation
    st.markdown("""
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
    particlesJS("particles-js", {
      "particles": {
        "number": {"value": 80, "density": {"enable": true, "value_area": 800}},
        "color": {"value": "#39FF14"},
        "shape": {"type": "circle", "stroke": {"width": 0, "color": "#000000"}, "polygon": {"nb_sides": 5}},
        "opacity": {"value": 0.5, "random": false, "anim": {"enable": false, "speed": 1, "opacity_min": 0.1, "sync": false}},
        "size": {"value": 3, "random": true, "anim": {"enable": false, "speed": 40, "size_min": 0.1, "sync": false}},
        "line_linked": {"enable": true, "distance": 150, "color": "#39FF14", "opacity": 0.4, "width": 1},
        "move": {"enable": true, "speed": 6, "direction": "none", "random": false, "straight": false, "out_mode": "out", "bounce": false, "attract": {"enable": false, "rotateX": 600, "rotateY": 1200}}
      },
      "interactivity": {
        "detect_on": "canvas",
        "events": {
          "onhover": {"enable": true, "mode": "repulse"},
          "onclick": {"enable": true, "mode": "push"},
          "resize": true
        },
        "modes": {
          "grab": {"distance": 400, "line_linked": {"opacity": 1}},
          "bubble": {"distance": 400, "size": 40, "duration": 2, "opacity": 8, "speed": 3},
          "repulse": {"distance": 200, "duration": 0.4},
          "push": {"particles_nb": 4},
          "remove": {"particles_nb": 2}
        }
      },
      "retina_detect": true
    });
    </script>
    """, unsafe_allow_html=True)

# Load Lottie animation from URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Main function
def main():
    load_css()  # Load custom CSS
    st.markdown('<div id="particles-js"></div>', unsafe_allow_html=True)  # Add particles.js div
    
    # Sidebar
    # Increase sidebar width
    st.markdown("""
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            width: 360px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            width: 360px;
            margin-left: -360px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Sidebar content
    st.sidebar.markdown("""
    <div class="sidebar-block">
        <h1 class="sidebar-text">Your Intelligent Assistant</h1>
        <h2 class="sidebar-text">Made by Engineer</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Create custom buttons for Chat and About
    col1, col2 = st.sidebar.columns(2)
    
    button_style = """
    <style>
    .stButton > button {
        border: 2px solid black !important;
        background-color: red !important;
        color: white !important;
        box-shadow: 0 0 10px #FF0000, 0 0 20px #FF0000, 0 0 30px #FF0000 !important;
    }
    </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)
    
    st.sidebar.markdown("<div style='height: 5px;'></div>", unsafe_allow_html=True)
    
    # Button actions
    if col1.button("Chat", key="chat_button", use_container_width=True):
        st.session_state.page = "Chat"
    if col2.button("About", key="about_button", use_container_width=True):
        st.session_state.page = "About"
    
    # Initialize page state if not exists
    if "page" not in st.session_state:
        st.session_state.page = "Chat"
    
    # Display the appropriate page based on button clicks
    if st.session_state.page == "Chat":
        chat_interface()
    else:
        about_page()

# Chat interface
def chat_interface():
    st.markdown('<h1 class="title">Prometheus is Home</h1>', unsafe_allow_html=True)
    
    url = "https://api.dify.ai/v1/chat-messages"

    # Initialize session state variables
    if "conversation_id" not in st.session_state:
        st.session_state.conversation_id = ""

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input for user prompt
    prompt = st.chat_input("Enter your question")

    if prompt:
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display assistant message
        with st.chat_message("assistant"):
            message_placeholder = st.empty()

            headers = {
                'Authorization': f'Bearer {dify_api_key}',
                'Content-Type': 'application/json'
            }

            payload = {
                "inputs": {},
                "query": prompt,
                "response_mode": "blocking",
                "conversation_id": st.session_state.conversation_id,
                "user": "aianytime",
                "files": []
            }

            try:
                with st.spinner("Thinking..."):
                    response = requests.post(url, headers=headers, json=payload)
                    response.raise_for_status()
                    response_data = response.json()

                    full_response = response_data.get('answer', '')
                    new_conversation_id = response_data.get('conversation_id', st.session_state.conversation_id)
                    st.session_state.conversation_id = new_conversation_id

            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")
                full_response = "An error occurred while fetching the response."

            message_placeholder.markdown(full_response)

            st.session_state.messages.append({"role": "assistant", "content": full_response})

    # Add a cool animation
    lottie_url = "https://lottie.host/858a8300-e80f-4050-8594-969789c9ac33/QYZ2BlUSes.json"
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, speed=1, height=300, key="lottie")

# About page
def about_page():
    st.markdown('<h1 class="title">About Prometheus</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family: 'Caesar Dressing', cursive; color: #39FF14;">
    Prometheus is an advanced AI chatbot designed to assist you with various tasks and answer your questions.
    
    Features:
    - Natural language processing
    - Contextual understanding
    - Wide range of knowledge
    
    When Prometheus is not answering your questions, he's probably playing video games.
    </div>
    """, unsafe_allow_html=True)
    
    # Add a cool animation for the About page
    lottie_url = "https://lottie.host/c968c5c3-0871-4db9-a710-573bbcb4de27/D0DtFLSTMI.json"
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, speed=1, height=300, key="about_lottie")

if __name__ == "__main__":
    main()