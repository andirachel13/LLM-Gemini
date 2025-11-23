# -*- coding: utf-8 -*-
"""Chatbot_Gemini.py
"""

!pip install -U -q google-generativeai langchain langchain-google-genai langchain_community pypdf chromadb



"""### Set up Google API Key

To use the Gemini API, you'll need an API key. If you don't already have one, create a key in Google AI Studio.

In Colab, add the key to the secrets manager under the "🔑" in the left panel. Give it the name `GOOGLE_API_KEY`. Then, the following code will retrieve it securely.
"""

import google.generativeai as genai
from google.colab import userdata

# Configure the Gemini API with your API key
GOOGLE_API_KEY=userdata.get('G-API')
genai.configure(api_key=GOOGLE_API_KEY)

"""### Streamlit Application for Creative Brief Generator

This code sets up a basic Streamlit application where you can input details for a creative brief, and a chatbot will generate the brief and marketing ideas.

**To run this Streamlit app:**
1.  Make sure you have `streamlit` installed (`!pip install streamlit`).
2.  Save the content of the following Python cell to a file named `app.py`.
3.  Run the app from your terminal using `streamlit run app.py` (you might need to forward the port if running in a remote environment like Colab via `!streamlit run app.py & npx localtunnel --port 8501`).
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# 
# import streamlit as st
# import google.generativeai as genai
# import os
# 
# # Configure Gemini API (ensure GOOGLE_API_KEY is set in environment variables or hardcoded for local testing)
# # In a deployed Streamlit app, you would typically set this as a secret.
# if 'GOOGLE_API_KEY' not in os.environ:
#     # For local development or Colab, you might load it differently
#     # For simplicity, if running directly in Colab without `userdata.get`,
#     # you'd need to provide it here or ensure `userdata.get` works from `app.py`
#     # For now, let's assume it's set in the environment or by `userdata.get` previously.
#     try:
#         from google.colab import userdata
#         genai.configure(api_key=userdata.get('G-API'))
#     except: # Fallback if not in Colab or userdata not available
#         st.error("Google API Key not found. Please set 'GOOGLE_API_KEY' in your environment or Colab secrets.")
#         st.stop()
# else:
#     genai.configure(api_key=os.environ['G-API'])
# 
# # Initialize the Generative Model
# model = genai.GenerativeModel('gemini-pro')
# 
# def generate_creative_brief(product, target_audience, key_message, desired_tone, call_to_action):
#     prompt = f"""Generate a creative brief and marketing ideas for the following product:
# 
# Product/Service: {product}
# Target Audience: {target_audience}
# Key Message: {key_message}
# Desired Tone: {desired_tone}
# Call to Action: {call_to_action}
# 
# The output should include:
# 
# ### Creative Brief:
# - **Project Title:** [Generated Title]
# - **Background:** [Short description]
# - **Objective:** [What the campaign aims to achieve]
# - **Target Audience:** [Detailed description]
# - **Key Message:** [Core idea]
# - **Desired Tone/Style:** [How it should feel]
# - **Call to Action:** [What do we want the audience to do]
# - **Key Deliverables:** [Example deliverables like social media posts, email, etc.]
# 
# ### Marketing Ideas:
# - **Social Media:** [Specific post ideas, platforms]
# - **Email Campaign:** [Subject lines, content ideas]
# - **Blog/Content Marketing:** [Topic ideas]
# - **Visuals/Imagery:** [Suggestions for creative direction]
# 
# """
#     try:
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         return f"An error occurred: {e}"
# 
# st.set_page_config(page_title="Creative Brief Generator & Marketer Chatbot", layout="wide")
# st.title("🧠 Creative Brief Generator & Marketer Chatbot")
# st.subheader("Generate comprehensive creative briefs and marketing ideas using AI.")
# 
# st.markdown("--- ")
# 
# with st.sidebar:
#     st.header("Input Details")
#     product = st.text_input("Product/Service Name", "AI-powered Content Creation Tool")
#     target_audience = st.text_area("Target Audience", "Small business owners, marketers, and content creators looking for efficient content generation.")
#     key_message = st.text_area("Key Message", "Save time and produce high-quality content effortlessly.")
#     desired_tone = st.text_input("Desired Tone (e.g., professional, witty, inspiring)", "Informative, modern, empowering")
#     call_to_action = st.text_input("Call to Action", "Sign up for a free trial today!")
# 
#     generate_button = st.button("Generate Brief & Ideas")
# 
# st.markdown("## Generated Output")
# 
# if generate_button:
#     if not product or not target_audience or not key_message or not desired_tone or not call_to_action:
#         st.warning("Please fill in all the input fields to generate the brief.")
#     else:
#         with st.spinner("Generating creative brief and marketing ideas..."):
#             output = generate_creative_brief(product, target_audience, key_message, desired_tone, call_to_action)
#             st.markdown(output)
#





