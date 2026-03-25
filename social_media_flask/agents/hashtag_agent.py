from utils.gemini_api import generate_from_image


def generate_hashtags(image_path):

    prompt = """
    Analyze this image and generate 10 trending social media hashtags.
     Return ONLY hashtags in this format:
    - #hashtag1
    - #hashtag2
    - #hashtag3
    """

    return generate_from_image(prompt, image_path)


   
    