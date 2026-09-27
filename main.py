import streamlit as st

# Page configuration
st.set_page_config(page_title="Smart Message Drafter", page_icon="💼", layout="centered")

st.title("💼 Smart Business Message Drafter")
st.write("Apni aam bhasha ya Hinglish mein likho, aur ek professional message taiyar karo—bina kisi AI key ke!")

# Professional & GenZ Corporate Dictionary (Words Mapping)
translation_dict = {
    "jaldi": "ASAP / on priority",
    "paisa": "payment / invoice amount",
    "nahi hua": "delayed due to a bottleneck",
    "sorry": "apologies for the oversight / inconvenience",
    "kal dunga": "will share by tomorrow EOD",
    "theek hai": "noted and acknowledged",
    "bhej do": "please share at your earliest",
    "kaam chal raha hai": "currently in progress",
    "phone uthao": "kindly connect over a quick call",
    "baad mein baat karte hain": "let's sync up on this later",
    "samajh gaya": "understood the context",
    "galti ho gayi": "regret the discrepancy"
}

# User Inputs
user_input = st.text_area("Yahan apni aam bhasha ya Hinglish mein likhein (Jaise: 'Bhai paisa jaldi bhej do, kaam ruk gaya hai')")
message_type = st.selectbox("Message kahan bhejna hai?", ["WhatsApp Message", "Professional Email", "Formal Notice"])

if st.button("🚀 Message Generate Karo"):
    if not user_input:
        st.error("Kripya message ki details toh dalein!")
    else:
        # Smart dictionary replacement logic
        processed_text = user_input.lower()
        for key, value in translation_dict.items():
            if key in processed_text:
                processed_text = processed_text.replace(key, value)
        
        # Formatting based on message type
        if message_type == "WhatsApp Message":
            final_output = f"Hi,\n\nRegarding the update: {processed_text}.\n\nLet's keep this on priority. Thanks!"
            
        elif message_type == "Professional Email":
            final_output = f"Subject: Update regarding current action items\n\nDear Team,\n\nI hope this email finds you well.\n\nThis is to bring to your attention that {processed_text}.\n\nKindly look into this at your earliest convenience.\n\nBest regards,\nProfessional Team"
            
        else: # Formal Notice
            final_output = f"NOTICE:\n\nIt has been observed that {processed_text}.\n\nStrict adherence to timelines is expected henceforth.\n\nManagement"
        
        st.success("Aapka professional message tayaar hai:")
        st.code(final_output, language="text")
        st.info("💡 Tip: Aap is text ko seedha copy karke use kar sakte hain!")
