# Voice-Activated AI Assistant with GPT-3.5 and Web Search Capabilities

This project implements a voice-activated AI assistant using Python, OpenAI's GPT-3.5 model, and various other libraries like `pyttsx3` (text-to-speech), `speech_recognition` (speech-to-text), and `webbrowser` (web search). The assistant listens to voice commands, interacts with the OpenAI GPT-3.5 model to generate responses, and can also perform web searches.

# Features

- **Voice Command Recognition**: Listens to user input using the microphone and converts it into text.
- **Text-to-Speech**: Responds with voice using the `pyttsx3` library.
- **AI Chatbot Integration**: Interacts with OpenAI's GPT-3.5 model to generate meaningful responses to user queries.
- **Web Browsing Capabilities**: Opens websites like Google and YouTube based on voice commands and can perform searches on these platforms.
- **Continuous Listening**: The assistant runs in a loop until the user explicitly says 'bye'.

# Libraries Used

- **[OpenAI](https://beta.openai.com/docs/)**: For generating chatbot responses using GPT-3.5.
- **[pyttsx3](https://pyttsx3.readthedocs.io/)**: For converting text responses into speech.
- **[speech_recognition](https://pypi.org/project/SpeechRecognition/)**: For converting voice input into text using the microphone.
- **[webbrowser](https://docs.python.org/3/library/webbrowser.html)**: To open web pages based on voice commands.

# Requirements

1. **Python 3.7+**
2. **OpenAI API Key**: You need an API key from OpenAI to interact with the GPT-3.5 model.
3. **Python Libraries**:
   - `openai`
   - `pyttsx3`
   - `speech_recognition`
   - `webbrowser`

You can install the required Python libraries using `pip`:

```bash
pip install openai pyttsx3 SpeechRecognition
```

# Setup Instructions

1. **Get an OpenAI API Key**:
   - Sign up at [OpenAI](https://openai.com/api/) and create an API key.
   - Store the API key in a separate file named `apikey.py` with the following format:

```python
# apikey.py
api_data = "your_openai_api_key"
```

2. **Clone or Download the Repository**:
   - Clone this repository or download the code files.

3. **Run the Python Script**:
   - Run the assistant by executing the script. Make sure your microphone is properly set up.
   - Use the command:

```bash
python assistant.py
```

4. **Interact with the Assistant**:
   - Once the assistant is running, you can start giving voice commands.
   - Example commands:
     - "Open Google"
     - "Open YouTube"
     - "Search on Google about Python programming"
     - "Search on YouTube about machine learning"
     - You can also ask questions like, "What is the capital of France?"

## Usage

After launching the script, the assistant will listen for voice commands. Depending on the input, it can:

1. **Respond to Queries**: 
   - If you ask a question or make a general statement, it will generate a response using OpenAI's GPT-3.5.
2. **Open Websites**:
   - Commands like "Open Google" or "Open YouTube" will open those websites in your default browser.
3. **Perform Searches**:
   - Commands like "Search on Google about..." or "Search on YouTube about..." will perform the relevant searches in the browser.
4. **Speak Responses**:
   - The assistant will speak the response back to you using the `pyttsx3` text-to-speech engine.

# Example Interaction

```
User: "Open Google"
Assistant: (opens Google in the browser)
User: "Search on YouTube about AI"
Assistant: (opens YouTube search for AI in the browser)
User: "What is the capital of Japan?"
Assistant: "The capital of Japan is Tokyo."
User: "Bye"
Assistant: (exits the program)
```

# Troubleshooting

1. **Microphone Not Detected**: Ensure that your microphone is set up correctly and that the `speech_recognition` library can access it.
2. **API Errors**: If there are issues connecting to OpenAI, check that your API key is valid and your network connection is stable.
3. **Speech Recognition Issues**: If the assistant isn't recognizing your voice properly, ensure that there is minimal background noise and speak clearly.

# License

This project is open-source under the MIT License.

# Future Enhancements

- Implementing support for more complex tasks like sending emails, setting reminders, or integrating with smart home devices.
- Adding error handling for API calls and microphone issues.
- Improving natural language understanding for a wider range of queries and voice commands.

---

This project demonstrates a basic voice-activated AI assistant using OpenAI's GPT-3.5 and Python libraries for speech recognition and web browsing. Feel free to customize it further and expand its capabilities.
