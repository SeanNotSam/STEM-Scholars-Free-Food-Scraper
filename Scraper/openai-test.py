from openai import OpenAI
from KeyHackAi import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)

filePath = 'scraperMac.py'

with open(filePath, 'r') as file:
    # Read the entire contents of the file into a string variable
    text = file.read()


completion =  client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content":text },
    {"role": "user", "content": "If there is an event talking about free food return the date, time and location of the event. If there is nothing related to free food, PLEASE ouput this ' '  and nothing else  "}
  ]
)

# Path to the output text file
fileOutput = 'scraperMac.py'

# Open the file in write mode
with open(fileOutput, "w") as file:
    # Write the text to the file
    file.write(completion.choices[0].message.content.strip())

