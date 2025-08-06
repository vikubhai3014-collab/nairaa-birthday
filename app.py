import streamlit as st
import time

st.set_page_config(page_title="Happy Birthday Naira ❤️", layout="centered")

# Custom CSS for gradient background and animations
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        color: #ff4081;
        animation: glow 2s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 0 10px #ff80ab, 0 0 20px #ff80ab; }
        to { text-shadow: 0 0 20px #ff4081, 0 0 30px #ff4081; }
    }
    # Butterfly Animation (using GIF link)
st.markdown('<img src="https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif" class="butterfly" />', unsafe_allow_html=True)
        animation: float 6s ease-in-out infinite;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    .secret {
        text-align: center;
        font-size: 1.5em;
        font-weight: bold;
        color: #ffffff;
        background-color: #ff80ab;
        padding: 10px;
        border-radius: 10px;
        display: inline-block;
        animation: blink 1s infinite;
    }
    @keyframes blink {
        0%, 50%, 100% { opacity: 1; }
        25%, 75% { opacity: 0; }
    }
    </style>
    """, unsafe_allow_html=True
)

# Title
st.markdown('<div class="title">🎉 Happy Birthday Naira! 🎉</div>', unsafe_allow_html=True)

# Butterfly Animation (using GIF link)
st.markdown('<img src="https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif" class="butterfly" />', unsafe_allow_html=True)

# Blinking secret message
time.sleep(1)
st.markdown('<div style="text-align:center; margin-top:20px;"><div class="secret">You are truly special! 💖</div></div>', unsafe_allow_html=True)

# Play Music Option
st.markdown("### 🎵 Want to hear something special?")
if st.button("Play Music"):
    st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav")
