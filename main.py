import streamlit as st

# Page configuration
st.set_page_config(page_title="Smart Sales Pitch Generator", page_icon="🚀", layout="centered")

st.title("🚀 Smart Sales & Service Pitch Drafter")
st.write("Apni business details niche bhariye, aur ekdum professional message ya pitch tayaar kijiye—bina kisi AI key ke!")

# Form inputs for structured and clean professional output
service_name = st.text_input("Aap kya banate/bechte hain? (Jaise: AI Apps & Websites)", "AI Apps and Websites")
price_range = st.text_input("Price Range kya hai? (Jaise: ₹100 se ₹5000)", "₹100 to ₹5000")
features = st.text_area("Key Features kya hain? (Jaise: 3-5 variants, easy to use, fast delivery)", "3-5 variants, easy to use, highly customized")
contact_info = st.text_input("Contact karne ka tareeqa / Number", "DM or contact us to know more")

platform_type = st.selectbox("Message kahan bhejna hai?", ["WhatsApp Sales Pitch", "Professional Email Proposal", "Social Media Caption"])

if st.button("✨ Professional Pitch Generate Karo"):
    
    if platform_type == "WhatsApp Sales Pitch":
        final_output = f"""Hello Sir/Ma'am, 👋

Are you looking to grow your business digitally? I provide custom **{service_name}** built using advanced AI models.

🔹 **Key Highlights:**
- Affordable pricing starting from **{price_range}**
- Features: {features}
- Super easy to use and manage.

Let's connect to discuss how we can build the perfect solution for you. 
📞 {contact_info}

Looking forward to hearing from you!"""

    elif platform_type == "Professional Email Proposal":
        final_output = f"""Subject: Professional {service_name} Solutions at Affordable Rates

Dear Client,

I hope this email finds you well.

I run a specialized service developing custom **{service_name}** powered by cutting-edge AI models. Our solutions are designed to be user-friendly and highly efficient.

**Service Overview:**
- **Offerings:** {features}
- **Investment:** Starting from {price_range}

If you are interested in exploring how this can benefit your business, kindly reach out via {contact_info}.

Best regards,
Business Developer"""

    else: # Social Media Caption
        final_output = f"""🔥 Transform your business with custom **{service_name}**! 

Looking for a smart digital solution? We build powerful apps and websites using advanced AI models tailored to your needs.

✨ **Why Choose Us?**
✔️ Price range: {price_range}
✔️ Includes: {features}
✔️ User-friendly & high performance

📲 Interested? {contact_info} and let's get started today! #AI #TechSolutions #BusinessGrowth"""

    st.success("Aapka professional message tayaar hai:")
    st.code(final_output, language="text")
    st.info("💡 Tip: Ise copy karke seedha apne clients ko bhej sakte hain!")
