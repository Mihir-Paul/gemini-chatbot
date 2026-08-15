from google import genai

client = genai.Client()

while True:
    question = input("Prompt: ")
    
    if question.lower() == "exit":
        break
    
    response = client.models.generate_content(
        model = "gemini-3.6-flash",
        contents=question 
    )
    
    print("Gemini:",response.text)