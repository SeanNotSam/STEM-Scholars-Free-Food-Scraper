from openai import OpenAI
from KeyHackAi import OPENAI_API_KEY
import PyPDF2


# Initialize OpenAI client with API key
client = OpenAI(api_key=OPENAI_API_KEY)

# Define a function to read the content of a text file
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()   # Add a line break after each page
    return text

# Path to the text file
pdf_path = '/Users/nathanaelgospodinov/Downloads/Untitled document (4).pdf'  
text = extract_text_from_pdf(pdf_path)

# Path to your PDF file

# Extract text from the PDF


# Now you can use the extracted text as input for GPT-3
# For example:

# Define the input text
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": text},
        {"role": "user", "content": "If there is an event talking about free food return that there will be 'free food: yes', the type of food (if applicable) , date (if applicable) , time (if applicable) and location (if applicable) of the event. Keep the details very concise, only ouput what is asked. Else if there is not free food event found output 'No free food event'"},
    ]
)


# Path to the output text file
file_path = "free_food_and_dominos_coupons.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Write the text to the file
    file.write(response.choices[0].message.content.strip())

