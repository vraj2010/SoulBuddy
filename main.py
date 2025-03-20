import streamlit as st
import requests
import datetime

# Constants
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "badb4656-66c0-45f4-b943-79abcbb3ec30"
APPLICATION_TOKEN = "AstraCS:ndZtkjnXQHyplsIOnYkbTsit:61d2c6e27a71621874a4af3d952a7c67463131bf0d2c46d90b362c504d35397c"
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

st.title("SoulBuddy")
st.subheader("Your personalized spiritual guide")
st.markdown("Interact with Hackonauts to generate insights.")

min_date = datetime.date(1900, 1, 1)
max_date = datetime.date.today()

# Input container
with st.container():
    name = st.text_input("Name:", placeholder="Enter your name")
    dob = st.date_input("Date of Birth", min_value=min_date, max_value=max_date)
    time = st.time_input("Time", step=datetime.timedelta(minutes=1))
    gender = st.selectbox("Gender:", ["Select", "Male", "Female", "Other"])
    state = st.text_input("State:", placeholder="Enter your state")
    city = st.text_input("City:", placeholder="Enter your city")
    
    # Create user message by concatenating input values
    user_message = f"{name} {dob} {time} {gender} {state} {city} generate horoscope."

# Button and response container
if st.button("Generate Horoscope"):
    if not user_message.strip():
        st.error("⚠ Please enter a valid message.")
    else:
        with st.spinner("Waiting for response..."):
            try:
                # Call LangFlow API with the user message
                response = run_flow(user_message)
                
                # Extract the result
                result = response.get("outputs", [{}])[0].get("outputs", [{}])[0].get(
                    "results", {}).get("message", {}).get("text", "No response.")
                
                # Display the result
                st.success("Response Received:")
                st.markdown(f"""
                    <div style="padding:10px; border-radius:5px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                        <p style="color:#333; font-size:16px; font-family:Arial, sans-serif;">{result}</p>
                    </div>
                """, unsafe_allow_html=True)
            except requests.exceptions.RequestException as e:
                st.error(f"⚠ An error occurred: {e}")
            except Exception as e:
                st.error(f"⚠ Unexpected error: {e}")
