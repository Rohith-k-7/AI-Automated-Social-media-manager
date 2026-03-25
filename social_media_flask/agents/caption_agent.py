from utils.gemini_api import generate_from_image


def generate_caption(image_path):

    prompt = """
    Analyze the image and generate a catchy social media caption.
      Return in this format:
    - Hook line
    - Main caption
    - CTA (call to action)

    Keep each point on a new line.
    """

    return generate_from_image(prompt, image_path)