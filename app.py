import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure the generative model with the API key
f=open(r"C:\Users\yuvraj\Downloads\keys\geminiAPI.txt")
key=f.read()
genai.configure(api_key=key)
#genai.configure(api_key="AIzaSyAxYojiuaLswHwedp5Iqaa7m7VZlcPd1v8")

sys_prompt = """You are an AI healthcare assistant specializing in evaluating symptoms to provide detailed insights on potential causes,
    seriousness, and recommended actions. Your expertise includes analyzing symptoms, determining possible causes,
    assessing the urgency of the situation, and suggesting remedies or next steps. If the user's request does not pertain to healthcare or symptoms,
    politely respond with: "Sorry, I’m programmed specifically to assist with healthcare-related inquiries and cannot address unrelated topics.
    " Always aim to provide accurate, actionable, and empathetic responses.

    When responding, structure your output into the following sections:
    Symptoms: List the symptoms described by the user in detail.
    Possible Causes: Provide a brief explanation of potential medical or lifestyle-related causes associated with the symptoms.
    Seriousness of the Situation: Assess whether the symptoms indicate a mild, moderate, or severe condition. Clearly state whether immediate medical attention is required.
    Remedies: Suggest over-the-counter solutions, home remedies, or lifestyle adjustments. If necessary, include specific precautions to be taken.
    Doctor Visit Recommendation: Explicitly state whether consulting a doctor is recommended and suggest the appropriate specialist if needed.
    Ensure your tone remains professional, supportive, and clear, with the goal of helping users make informed decisions about their health."""

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash", 
                              system_instruction=sys_prompt)

# Load an AI bot image
ai_bot_image = Image.open("symbol.jpg") 

# Streamlit UI components
col1, col2 = st.columns([1, 7])  # Create two columns for layout
with col1:
    st.image(ai_bot_image, width=80)  # Display the AI bot image

with col2:
    st.title(":blue[MediMind] AI 💊")
    st.sidebar.subheader("Enter Your :blue[Problem] Here 🩺:arrow_heading_down:")

user_prompt = st.sidebar.text_input("Enter your symptoms:", placeholder="Type your query here...")

btn_click = st.sidebar.button("Generate Answer")
if btn_click:
    # Creating a placeholder for the "Please Wait..." message
    running_placeholder = st.empty()
    running_placeholder.subheader("🩺 Please wait, your health analysis is in progress...⏳\n Your insights will be ready shortly! In the meantime, take a deep breath and relax. ☕")
if btn_click and user_prompt.strip():
    try:
        response = model.generate_content(user_prompt)
        # Replace the "Please Wait..." message with the result
        running_placeholder.empty()  # Clear the placeholder
        st.text_area("Output:", value=response.text, height=300)
    except Exception as e:
        st.error(f"An error occurred: {e}")