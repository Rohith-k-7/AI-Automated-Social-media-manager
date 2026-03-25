from utils.gemini_api import generate_from_image


def generate_schedule(image_path):

    prompt = """
    Analyze the image and suggest the best time to post on social media.

    Provide:
    - Best day
    - Best time
    - Brief reason

    Keep the answer short and structured.
    """

    return generate_from_image(prompt, image_path)