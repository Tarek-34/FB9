# Interactive AI Agent

This project is a simple graphical user interface (GUI) built using Python's `tkinter` library. It allows users to interact with the OpenAI API to generate responses from an AI model, such as `gpt-4`, by entering prompts and receiving output.

## Features

- **Environment Variable Handling**: The application uses `dotenv` to load the OpenAI API key from a `.env` file, ensuring secure and convenient configuration.
- **Graphical User Interface**: The GUI is created using `tkinter` and provides an easy-to-use interface for inputting prompts and viewing the generated responses.
- **Error Handling**: Basic error handling is implemented to manage issues such as API call failures.

## Prerequisites

- Python 0.28.0 installed on your system
- `openai`, `python-dotenv`, and `tkinter` libraries installed

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
*If needed this is the prompt to download the requried settings- pip install openai python-dotenv

You will need to replace api_key = os.getenv("AI_API_KEY") with api_key = "Your own api_key" and when you run it a messeage in the terminal will let you know if it was loaded successful or not.
