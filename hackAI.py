from openai import OpenAI
from KeyHackAi import OPENAI_API_KEY

# Initialize OpenAI client with API key
client = OpenAI(api_key=OPENAI_API_KEY)

# Define a function to read the content of a text file
def read_text(text_path):
    # Open the text file in read mode
    with open(text_path, 'r') as file:
        # Read the entire content of the file and split it into lines
        lines = file.readlines()
    
    return lines

# Define a function to interact with GPT-3
def chat_with_gpt3(prompt):
    # Send the prompt to GPT-3
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "user", "content": "If there is an event talking about free food return that there will be 'free food: yes', the type of food (if applicable), date (if applicable), time (if applicable), and location (if applicable) of the event. Keep the details very concise, only output what is asked. Else if there is not free food event found output 'No free food event'"},
        ]
    )
    return response.choices[0].message.content.strip()

# Path to the input text file
text_path = 'email_subjects.txt'  
lines = read_text(text_path)

# List to store GPT-3 responses
gpt3_responses = []

# Iterate over each line in the input text file
for line in lines:
    # Get GPT-3 response for the current line
    response = chat_with_gpt3(line)
    # Append the response to the list
    gpt3_responses.append(response)

# Path to the output text file
file_path = "output.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Write the GPT-3 responses to the file
    for response in gpt3_responses:
        file.write(response + "\n")
        file.write("\n")  # Add a full blank line after each response

        
