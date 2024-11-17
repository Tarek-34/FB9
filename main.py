import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import ttk
import openai

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("AI_API_KEY")
openai.api_key = api_key

# Check if the API key is loaded correctly
if api_key:
    print("API Key loaded successfully!")
else:
    print("Failed to load API Key. Check your .env file and setup.")

# Function to handle the API call and display output
def on_submit():
    user_input = prompt_entry.get()
    response = generate_response(user_input)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, response)

# Function to generate a response from OpenAI
def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Create the main window
root = tk.Tk()
root.title("Interactive AI Agent")

# Create and place the prompt entry
ttk.Label(root, text="Enter your prompt:").grid(column=0, row=0, padx=10, pady=10)
prompt_entry = ttk.Entry(root, width=50)
prompt_entry.grid(column=1, row=0, padx=10, pady=10)

# Create and place the submit button
submit_button = ttk.Button(root, text="Submit", command=on_submit)
submit_button.grid(column=2, row=0, padx=10, pady=10)

# Create and place the output text box
ttk.Label(root, text="Output:").grid(column=0, row=1, padx=10, pady=10)
output_text = tk.Text(root, height=10, width=60)
output_text.grid(column=0, row=2, columnspan=3, padx=10, pady=10)

# Run the application
root.mainloop()
