from google import genai

client = genai.Client()
stream = client.interactions.create()