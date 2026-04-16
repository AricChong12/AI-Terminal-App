from google import genai
import dotenv
import os

# loads the .env file into working memory
dotenv.load_dotenv()

# Initialize the native Gemini client with your key
client = genai.Client(api_key = os.environ["api_key"])

conv_history = []

while True : 
    query = input("user: \t")
    conv_history.append({"role" : "user", "parts": [ {"text" : query} ]})
    # Make the chat completion call
    response = client.models.generate_content(
        model = "gemma-3-27b-it",
        contents = conv_history,
        config = {
            "temperature": 0.0
        }
    )
    conv_history.append({"role" : "model", "parts": [ {"text" : response.text} ]})
    # Print the response
    print(response.text)
