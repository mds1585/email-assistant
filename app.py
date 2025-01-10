import openai
import streamlit as st

# Set up OpenAI API key
import os
openai.api_key = st.secrets["OPENAI"]["API_KEY"]

# Webpage title
st.title("Email Drafting Assistant")

# Input box for raw thoughts
raw_thoughts = st.text_area("Paste your raw thoughts here:")

# Button to trigger AI
if st.button("Draft My Email"):
    if raw_thoughts:
        # AI prompt
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert at quickly distilling key points from raw notes into concise, action-oriented emails while maintaining a professional, friendly demeanor necessary for an implementation manager of a software company to succeed. "
                    "Your goal is to draft a short to medium length, effective email based on the raw thoughts provided, stripping out nearly all fluff or bloat."
                ),
            },
            {
                "role": "user",
                "content": f"Context: {raw_thoughts}\n\n"
                           "Follow this process to draft the email:\n"
                           "Carefully read through the raw thoughts to identify the core objective and any specific requests or action items.\n"
                           "Organize the key points into a logical flow:\n"
                           "- Open with a clear statement of purpose.\n"
                           "- Concisely provide essential context or details.\n"
                           "- Explicitly state any asks, next steps, or deadlines.\n"
                           "- Edit the email down to the bare essentials, eliminating:\n"
                           "  * Unnecessary background or tangents.\n"
                           "  * Redundant statements or excessive explanations.\n"
                           "  * Assumed knowledge or unsupported claims.\n"
                           "  * Excessive pleasantries or apologies.\n"
                           "Close with a specific call-to-action that reinforces the desired outcome and respects the recipient's time.\n\n"
                           "Constraints:\n"
                           "- The entire email should ideally be 2-3 paragraphs or less.\n"
                           "- Avoid long greetings or signoffs. A simple 'Hi [Name],' and 'Thanks,' or 'Best,' works.\n"
                           "- The most fluff I want is to say that I hope they're doing well.\n"
                           "- Assume the recipient is busy. Get straight to the point.\n\n"
                           "Style guide:\n"
                           "- Use a polite but direct tone.\n"
                           "- Be personable but efficient.\n"
                           "- Write at an 8th grade reading level.\n"
                           "- Use simple words and sentence structures.\n"
                           "- Avoid jargon, acronyms or $10 words.\n"
                           "- Use plain, everyday language.\n"
                           "- Write in the active voice.\n"
                           "- Make requests clear and unambiguous.\n"
                           "- Double check for typos or errors.\n"
                           "- Keep it professional.\n\n"
                           "Output format:\n"
                           "Subject: [Specific, descriptive subject line]\n"
                           "Hi [Name],\n"
                           "[Opening sentences to describe purpose]\n"
                           "[Middle sentence describing context or necessary details]\n"
                           "[Specific request, ask or call-to-action]\n"
                           "[Signoff], [Your name]"
            }
        ]

        try:
            # Make the API call
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages
            )

            # Display the drafted email
            st.subheader("Drafted Email:")
            st.write(response['choices'][0]['message']['content'])

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please paste some raw thoughts to draft your email!")
