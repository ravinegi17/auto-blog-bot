import openai
import requests
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_image(topic, filename="image.jpg"):
    prompt = f"Create a realistic, high-quality image about: {topic}. Suitable for a blog featured image."

    response = openai.Image.create(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        response_format="url",
        n=1
    )

    image_url = response['data'][0]['url']
    os.makedirs("images", exist_ok=True)
    path = os.path.join("images", filename)
    with open(path, 'wb') as f:
        f.write(requests.get(image_url).content)

    return path
