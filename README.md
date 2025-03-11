# SoulBuddy

**SoulBuddy** is a spiritual chatbot project designed to offer personalized horoscopes and insights based on user inputs. This application integrates **Langflow** for natural language processing and **Streamlit** for a user-friendly interface. The chatbot leverages **DataStax Astra** for secure data handling and conversational flow execution.

## 🌐 Website  

Access the live project at:  
[https://soulbuddy-hackonauts.streamlit.app/](https://soulbuddy-hackonauts.streamlit.app/)

---

## 📖 Features

- **Personalized Horoscopes:** Generate spiritual insights based on user details.  
- **Interactive Interface:** Intuitive and user-friendly interaction through Streamlit.  
- **Langflow Integration:** AI-powered backend to process user queries.  
- **Scalable Database:** Powered by **DataStax Astra** for efficient and secure data processing.  

---

## 🚀 Tech Stack

- **Langflow**: Workflow engine for natural language processing.  
- **Python**: Core programming language for backend processes.  
- **Streamlit**: Interactive web interface for user inputs and outputs.  
- **DataStax Astra**: Scalable database solution for storing and handling API tokens and configurations.  

---

## 📂 Dataset

The chatbot uses user-provided inputs to generate horoscopes, such as:

1. **Name:** User's full name.  
2. **Date of Birth:** User's date of birth for astrological analysis.  
3. **Time of Birth:** Specific time for accurate insights.  
4. **Gender:** Male, Female, or Other.  
5. **State:** User's state of residence.  
6. **City:** User's city of residence.  

---

## 🖥 Screenshots

### User Input Section  
![User Input](https://github.com/vraj2010/SoulBuddy/Input.jpg)

### Horoscope Output  
![Horoscope Output](https://github.com/vraj2010/SoulBuddy/Output.jpg)

---

## 📜 Installation and Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/vraj2010/SoulBuddy.git
   cd SoulBuddy
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Tokens**  
   - Set up your **Langflow API Token** in the environment variables:  
     ```bash
     export APPLICATION_TOKEN="your_langflow_api_token"
     ```

4. **Run the Streamlit App**  
   ```bash
   streamlit run app.py
   ```

5. **Access the app** at [http://localhost:8501](http://localhost:8501).

---

## 🎯 How to Use

1. Enter your details such as name, date of birth, time, and location.  
2. Click on **Generate Horoscope** to receive insights.  
3. View your horoscope in the response section.  

---

## 🤝 Contributing

We welcome contributions! To contribute:  
1. Fork the repository.  
2. Create a new branch for your feature or fix.  
3. Submit a pull request with detailed descriptions.  

---

## 🛠️ Future Enhancements

- Add advanced astrological features such as natal charts.  
- Support additional languages for wider accessibility.  
- Integrate voice-based interaction for enhanced user experience.  

---

## 📧 Contact

For any queries or suggestions, please contact:  
**Email:** vraj20102005@gmail.com  
**GitHub:** [vraj2010](https://github.com/vraj2010)  

---

## 💡 Acknowledgements

Special thanks to the **SoulBuddy** team for their contributions to this project!
