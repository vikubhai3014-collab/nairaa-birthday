import streamlit as st

# Page Config
st.set_page_config(page_title="Happy Birthday Hardik!", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        color: white;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 60px;
        font-weight: bold;
        margin-top: 50px;
        animation: glow 1.5s infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 0 10px #fff, 0 0 20px #ff1177; }
        to { text-shadow: 0 0 20px #ff1177, 0 0 30px #ff1177; }
    }
    .hidden-message {
        font-size: 30px;
        font-weight: bold;
        color: #ff4444;
        animation: blink 1s infinite;
        margin-top: 30px;
    }
    @keyframes blink {
        0% {opacity: 1;}
        50% {opacity: 0;}
        100% {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown('<div class="title">🎉 Happy Birthday Hardik 🎉</div>', unsafe_allow_html=True)

# Button for Secret Message
if st.button("Click for Secret Wish"):
    st.markdown('<div class="hidden-message">🙏 Bhagwan tera bhala kare, chota lulli bada kare 🙏</div>', unsafe_allow_html=True) 
