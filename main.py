import streamlit as st
from google import genai

st.set_page_config(page_title="Business Message Drafter", page_icon="💼", layout="centered")

st.title("💼 AI Business Message Drafter")
st.write("Aam bhasha mein likho, aur ek professional WhatsApp message ya Email tayaar karo!")

st.sidebar.header("🔑 AI Settings")
api_key = st.sidebar.text_input("Enter your Google Gemini API Key", type="password")
st.sidebar.info("Free Gemini API key aap Google AI Studio se bilkul free mein le sakte hain.")

user_input = st.text_area("Aapko kis baare mein message likhna hai? (Jaise: Customer ko bolo ki payment late hai, thoda politely samjhao)")
message_type = st.selectbox("Message kahan bhejna hai?", ["WhatsApp Message", "Professional Email", "Formal Notice"])

if st.button("🚀 Message Generate Karo"):
    if not api_key:
        st.error("Kripya pehle sidebar mein apni Gemini API Key dalein!")
    elif not user_input:
        st.error("Kripya message ki details toh dalein!")
    else:
        try:
            client = genai.Client(api_key=api_key)
            prompt = f"Tum ek professional business communication expert ho. Niche diye gaye input ko ek behtareen aur clear {message_type} mein badal do. Input: {user_input}"

            response = client.models.generate_content(
                model='gemini-3.8-flash',
                contents=prompt,
            )

            st.success("Aapka message tayaar hai:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Kuch galti ho gayi: {e}")
