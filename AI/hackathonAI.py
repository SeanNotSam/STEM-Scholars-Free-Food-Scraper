from openai import OpenAI
import PyPDF2

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

pdf_path = "/Users/nathanaelgospodinov/Downloads/lard.pdf"

text = read_pdf(pdf_path)

# Path to your PDF file

# Extract text from the PDF


# Now you can use the extracted text as input for GPT-3
# For example:

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": text},
        {"role": "user", "content": "If there is an event talking about free food return that there will be free food, the type of food, date, time and location of the event. Keep the details very concise, only ouput what is asked, if one of the items is not present in file ouput unknown. Else output 'No free food events'"},
    ]
)


# Path to the output text file
file_path = "free_food_and_dominos_coupons.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Write the text to the file
    file.write(response.choices[0].message.content.strip())

