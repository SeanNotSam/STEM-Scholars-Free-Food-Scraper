from openai import Client 
from openai import OpenAI
import PyPDF2
import openai

OPENAI_API_KEY = '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'

# Initialize OpenAI client with API key
client = OpenAI(api_key=OPENAI_API_KEY)


            
def read_pdf(pdf_path):
    # Open the PDF file in binary mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)
        
        # Initialize an empty string to store the extracted text
        text = ''
        
        # Iterate through each page of the PDF
        for page_num in range(len(reader.pages)):
            # Extract text from the current page
            page = reader.pages[page_num]
            text += page.extract_text()
    
    return text

pdf_path = "/Users/nathanaelgospodinov/Downloads/Untitled document (4).pdf"

text = read_pdf(pdf_path)

# Path to your PDF file

# Extract text from the PDF


# Now you can use the extracted text as input for GPT-3
# For example:

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": text},
        {"role": "user", "content": "If there is an event talking about free food return the date, time and location of the event. If there is nothing related to free food, PLEASE ouput this ' '  and nothing else  "}
    ]
)


# Path to the output text file
file_path = "free_food_and_dominos_coupons.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Write the text to the file
    file.write(response.choices[0].message.content.strip())

