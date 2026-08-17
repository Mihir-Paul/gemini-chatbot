from google import genai 

from google.genai import types

client = genai.Client()

while True:

    question = input("Prompt: ")

    if question.lower() == "exit":
        break 

    response = client.models._generate_content(
        model= "gemini-3.6-flash",
        contents= question,
        config= types.GenerateContentConfig(
            system_instruction= "Before responding, identify the user's actual goal and answer only what is necessary to accomplish it. Remove anything that does not directly help.",
            temperature= 1
            
        )
    )

    print("Gemini:",response.text)