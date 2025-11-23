import streamlit as st

# Configure Gemini API
# Ensure 'G-API' is set in Colab secrets or 'GOOGLE_API_KEY' in environment variables for deployment
if 'G-API' not in os.environ and 'GOOGLE_API_KEY' not in os.environ:
    try:
        from google.colab import userdata
        # Use 'G-API' as per the provided setup in the notebook
        api_key = userdata.get('G-API')
        genai.configure(api_key=api_key)
    except Exception:
        st.error("Google API Key not found. Please set 'G-API' in your Colab secrets or 'GOOGLE_API_KEY' in environment variables.")
        st.stop()
elif 'G-API' in os.environ:
    genai.configure(api_key=os.environ['G-API'])
else:
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Initialize the Generative Model and chat session
# Using 'gemini-2.5-flash' as per the original notebook's model suggestion
if "chat_session" not in st.session_state:
    st.session_state.chat_session = genai.GenerativeModel('gemini-2.5-flash').start_chat(history=[])

st.set_page_config(page_title="Creative Brief Generator & Marketer Chatbot", layout="wide")
st.title("🧠 Creative Brief Generator & Marketer Chatbot")
st.subheader("Generate comprehensive creative briefs and marketing ideas using AI.")

st.markdown("--- ")

with st.sidebar:
    st.header("Input Details")
    product = st.text_input("Product/Service Name", "AI-powered Content Creation Tool")
    target_audience = st.text_area("Target Audience", "Small business owners, marketers, and content creators looking for efficient content generation.")
    key_message = st.text_area("Key Message", "Save time and produce high-quality content effortlessly.")
    desired_tone = st.text_input("Desired Tone (e.g., professional, witty, inspiring)", "Informative, modern, empowering")
    call_to_action = st.text_input("Call to Action", "Sign up for a free trial today!")

    generate_button = st.button("Generate Brief & Ideas")
    clear_chat_button = st.button("Clear Chat", help="Clear the current conversation and start anew.")

# Clear chat logic
if clear_chat_button:
    st.session_state.chat_session = genai.GenerativeModel('gemini-2.5-flash').start_chat(history=[])
    st.rerun()

st.markdown("## Chat Output")

# Display chat messages from history
for message in st.session_state.chat_session.history:
    role = "assistant" if message.role == "model" else message.role
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# Initial brief generation logic
if generate_button:
    if not product or not target_audience or not key_message or not desired_tone or not call_to_action:
        st.warning("Please fill in all the input fields to generate the brief.")
    else:
        # Clear previous chat history if new brief is generated
        st.session_state.chat_session = genai.GenerativeModel('gemini-2.5-flash').start_chat(history=[]) # Start a new chat session
        
        brief_prompt = f"""Generate a creative brief and marketing ideas for the following product:

Product/Service: {product}
Target Audience: {target_audience}
Key Message: {key_message}
Desired Tone: {desired_tone}
Call to Action: {call_to_action}

The output should include:

### Creative Brief:
- **Project Title:** [Generated Title]
- **Background:** [Short description]
- **Objective:** [What the campaign aims to achieve]
- **Target Audience:** [Detailed description]
- **Key Message:** [Core idea]
- **Desired Tone/Style:** [How it should feel]
- **Call to Action:** [What do we want the audience to do]
- **Key Deliverables:** [Example deliverables like social media posts, email, etc.]

### Marketing Ideas:
- **Social Media:** [Specific post ideas, platforms]
- **Email Campaign:** [Subject lines, content ideas]
- **Blog/Content Marketing:** [Topic ideas]
- **Visuals/Imagery:** [Suggestions for creative direction]

"""
        # Manually add user's implied prompt to history for display
        # Summarize the user's detailed input for cleaner display in chat
        user_display_prompt = (
            f"**Brief Request:**\n" 
            f"- **Product:** {product}\n" 
            f"- **Audience:** {target_audience[:100]}...\n" 
            f"- **Key Message:** {key_message[:100]}...\n" 
            f"- **Tone:** {desired_tone}\n" 
            f"- **CTA:** {call_to_action}"
        )
        with st.chat_message("user"):
            st.markdown(user_display_prompt)
        
        # Send the actual full brief prompt to the model and get response
        with st.spinner("Generating creative brief and marketing ideas..."):
            try:
                response = st.session_state.chat_session.send_message(brief_prompt)
                brief_output = response.text
            except Exception as e:
                brief_output = f"An error occurred during brief generation: {e}"
        
        with st.chat_message("assistant"):
            st.markdown(brief_output)
        st.rerun() # Rerun to display the new messages

# Chat input for follow-up questions
if prompt := st.chat_input("Ask a follow-up question about the brief or marketing ideas..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from the model based on the chat history
    with st.spinner("Thinking..."):
        try:
            response = st.session_state.chat_session.send_message(prompt)
            ai_response = response.text
        except Exception as e:
            ai_response = f"An error occurred: {e}"

    with st.chat_message("assistant"):
        st.markdown(ai_response)
    st.rerun() # Rerun to display the new messages
