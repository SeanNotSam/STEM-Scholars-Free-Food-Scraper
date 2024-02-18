from openai import OpenAI
from KeyHackAi import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def read_text(text_path):
    with open(text_path, 'r') as file:
        lines = file.readlines()
    
    return lines

def chat_with_gpt3(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "user", "content": "If there is an event talking about free food return that there will be 'free food: yes', the type of food (if applicable), date (if applicable), time (if applicable), and location (if applicable) of the event. Keep the details very concise, only output what is asked. Else if there is not free food event found output 'No free food event'"},
        ]
    )
    return response.choices[0].message.content.strip()

text_path = 'email_subjects.txt'  
lines = read_text(text_path)
gpt3_responses = []

for line in lines:
    response = chat_with_gpt3(line)
    gpt3_responses.append(response)

file_path = "output.txt"

with open(file_path, "w") as file:
    for response in gpt3_responses:
        file.write(response + "\n")
        file.write("\n")  

        
