import streamlit as st
import requests
import base64

# Set Streamlit page configuration
st.set_page_config(page_title="Multi-Modal Assistant (LLaVA via Ollama)", layout="centered")

# Custom title styling
st.markdown(
    """
    <h1 style='text-align: center; color: #4A90E2;'>
        Multi-Modal Assistant (LLaVA via Ollama)
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("Upload an image and ask a question about it. Everything runs locally with no API keys or cloud calls.")

# State to control image reset
if "reset_triggered" not in st.session_state:
    st.session_state.reset_triggered = False

uploaded_file = None
if not st.session_state.reset_triggered:
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # Input box - pressing Enter will trigger the query
    user_prompt = st.text_input(
        label="Ask your question here",
        label_visibility="collapsed",
        placeholder="Type your question and press Enter",
        key="prompt_input"
    )

    # Trigger only when Enter pressed (i.e., when user_prompt is not empty)
    if user_prompt:
        image_bytes = uploaded_file.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        payload = {
            "model": "llava",
            "prompt": user_prompt,
            "images": [image_base64],
            "stream": False
        }

        try:
            response = requests.post("http://localhost:11434/api/generate", json=payload)

            if response.status_code == 200:
                result = response.json()["response"]
                st.success("Assistant's Response")
                st.write(result)
                st.session_state.reset_triggered = True
            else:
                st.error(f"Ollama Error: {response.text}")
        except Exception as e:
            st.error(f"Connection Error: {e}")
            st.info("Make sure Ollama is running using: `ollama run llava`")

# Button to upload another image
if st.session_state.reset_triggered:
    if st.button("Upload Another Image"):
        st.session_state.reset_triggered = False
        st.rerun()

# Hide Streamlit footer
hide_footer = """
    <style>
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_footer, unsafe_allow_html=True)
