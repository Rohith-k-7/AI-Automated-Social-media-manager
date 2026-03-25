import os
from google import genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_from_image(prompt, image_path):

    image = Image.open(image_path)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt, image]
    )

    return response.text