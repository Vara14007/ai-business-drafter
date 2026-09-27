import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(page_title="Nvidia AI Pitch Generator", page_icon="⚡", layout="centered")

st.title("⚡ AI-Powered Business Pitch Generator (Nvidia NIM)")
st.write("Aap apni aam bhasha ya raw text mein likhein, Nvidia AI ise ekdum professional message mein badal dega!")

# Sidebar for Nvidia API Key
st.sidebar.header("🔑 Nvidia API Configuration")
nvidia_api_key = st.sidebar.text_input("Enter your Nvidia API Key", type="password")
st.sidebar.info("Aap Nvidia NIM se apni free API key yahan daal sakte hain.")

# User inputs
user_input = st.text_area("Aapka message ya business detail yahan likhein (Jaise: 'me ak business krta hu jisme ai models ka use kr ke me app ya website banata hu...')", height=120)
message_type = st.selectbox("Message kahan bhejna hai?", ["WhatsApp Sales Pitch", "Professional Email Proposal", "Social Media Caption"])

if st.button("🚀 AI se Professional Message Banao"):
    if not nvidia_api_key:
        st.error("Kripya pehle sidebar mein apni Nvidia API Key dalein!")
    elif not user_input:
        st.error("Kripya kuch details toh dalein!")
    else:
        try:
            # Initialize Nvidia NIM client (OpenAI compatible)
            client = OpenAI(
                base_url="https://integrate.api.nvidia.com/v1",
                api_key=nvidia_api_key
            )
            
            system_prompt = "You are an expert corporate communications and business growth copywriter. Rewrite the user's raw, rough input into a polished, high-converting professional message based on the requested format."
            user_prompt = f"Convert the following raw text into a professional {message_type}. Keep it engaging, clear, and impactful.\n\nRaw Text: {user_input}"

            with st.spinner("Nvidia AI is generating your professional pitch..."):
                response = client.chat.completions.create(
                    model="meta/llama-3.3-70b-instruct",  # Nvidia NIM standard reliable model
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.7,
                    max_tokens=1024
                )
                
                final_output = response.choices[0].message.content

            st.success("Aapka AI-generated professional message tayaar hai:")
            st.markdown(final_output)

        except Exception as e:
            st.error(f"Kuch galti ho gayi: {e}")
