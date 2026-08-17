from google import genai
from google.genai import types 
from PIL import Image 

client = genai.Client()

image = Image.open("images/cat.jpg")

response = client.models.generate_content(
    model = "gemini-3.6-flash",
    contents= [image,"Tell me about this image"],
    config = types.GenerateContentConfig(
        system_instruction = "Response should be funny and of 10 words only" ,
        temperature = 1
    )
)

print("Gemini: ",response.text)