import streamlit as st
import requests

# Constants
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "badb4656-66c0-45f4-b943-79abcbb3ec30"
APPLICATION_TOKEN = "AstraCS:mNZmDmZFukpoBtcosohgECRY:078cc67eb7541f1db01128ab9d21525e7a9e027b06888b3ed6fd5adca3b081ec"
ENDPOINT = "ab785155-9fc7-44a6-b1c5-c10393b2cb8f?stream=false"

def run_flow(message: str) -> dict:
    """
    Call the LangFlow API to process the message.
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {
        "Authorization": "Bearer " + APPLICATION_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.post(api_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()

# Streamlit Interface
st.set_page_config(page_title="Hackonauts Chatbot", layout="centered")

# App Title and Description
st.title("SoulBuddy")
st.subheader("Your personalized spiritual guide")
st.markdown("Interact with Hackonauts to generate insights.")

# Input Section
st.header("Enter Your Details")
with st.form("user_inputs"):
    name = st.text_input("Name", placeholder="Enter your name")
    dob = st.date_input("Date of Birth")
    time = st.time_input("Time")
    gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])
    state = st.text_input("State", placeholder="Enter your state")
    city = st.text_input("City", placeholder="Enter your city")
    
    submitted = st.form_submit_button("Generate Horoscope")

if submitted:
    if not name or gender == "Select" or not state or not city:
        st.error("⚠️ Please fill out all fields correctly.")
    else:
        user_message = f"{name} {dob} {time} {gender} {state} {city} generate horoscope."
        with st.spinner("Fetching response..."):
            try:
                # Call LangFlow API with the user message
                response = run_flow(user_message)
                
                # Extract the result
                result = response.get("outputs", [{}])[0].get("outputs", [{}])[0].get(
                    "results", {}).get("message", {}).get("text", "No response.")
                
                # Display the result
                st.header("Chatbot Response")
                st.success(result)
            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ An error occurred: {e}")
            except Exception as e:
                st.error(f"⚠️ Unexpected error: {e}")
