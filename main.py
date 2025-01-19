import streamlit as st
import requests
import matplotlib.pyplot as plt
import random

# Constants for LangFlow API
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "badb4656-66c0-45f4-b943-79abcbb3ec30"
APPLICATION_TOKEN = "AstraCS:MBGHcCzoGHXPuPhUJAYMExEF:b4de9645f5e3e61c94cdcb6bbed7e81a4e829c403e5eded992fd3f191d32cf89"
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

# Birth Chart Visualization
def generate_birth_chart(coordinates, user_name):
    """
    Generate a visual birth chart based on coordinates.
    """
    latitudes = [coord[0] for coord in coordinates]
    longitudes = [coord[1] for coord in coordinates]
    
    # Create the birth chart as a scatter plot
    plt.figure(figsize=(8, 8))
    plt.scatter(longitudes, latitudes, c='blue', alpha=0.6, edgecolors='black')
    plt.title(f"Birth Chart for {user_name}", fontsize=14)
    plt.xlabel("Longitude", fontsize=12)
    plt.ylabel("Latitude", fontsize=12)
    plt.grid(alpha=0.4)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Equator
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Prime Meridian
    st.pyplot(plt)

# Streamlit Interface
st.set_page_config(page_title="Hackonauts Chatbot and Birth Chart", layout="centered")

st.title("Chat with Hackonauts & Generate Your Birth Chart")
st.markdown("Data-Driven Social Insights with Langflow and Birth Charts.")

# Input container
with st.container():
    name = st.text_input("Name:", placeholder="Enter your name")
    dob = st.date_input("Date of Birth:")
    time = st.time_input("Time of Birth:")
    gender = st.selectbox("Gender:", ["Select", "Male", "Female", "Other"])
    state = st.text_input("State:", placeholder="Enter your state")
    city = st.text_input("City:", placeholder="Enter your city")
    
    # Create user message by concatenating input values
    user_message = f"{name} {dob} {time} {gender} {state} {city} generate horoscope."

# Button and response container
if st.button("Send"):
    if not name.strip() or gender == "Select":
        st.error("⚠ Please fill in all the required fields.")
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
                    <div style="background-color:#f9f9f9; padding:10px; border-radius:5px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                        <p style="color:#333; font-size:16px; font-family:Arial, sans-serif;">{result}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Generate and display the birth chart
                birth_chart_coordinates = [(random.uniform(-90, 90), random.uniform(-180, 180)) for _ in range(100)]
                st.markdown(f"### Birth Chart for {name}")
                generate_birth_chart(birth_chart_coordinates, name)

            except requests.exceptions.RequestException as e:
                st.error(f"⚠ An error occurred: {e}")
            except Exception as e:
                st.error(f"⚠ Unexpected error: {e}")
