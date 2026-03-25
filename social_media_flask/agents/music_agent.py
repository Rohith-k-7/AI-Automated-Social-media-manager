from utils.gemini_api import generate_from_image


def suggest_music(image_path):

    prompt = """
    Based on the mood of this image, suggest 5 trending Instagram or spotify songs.
     Return ONLY in this format:
    - Song Name - Artist
    - Song Name - Artist
    """

    return generate_from_image(prompt, image_path)