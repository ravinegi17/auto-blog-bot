import os
import requests
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_blog_image(topic, filename="image.jpg"):
    prompt = f"Create a high-quality blog-style image about: {topic}. It should be professional, visually engaging, and suitable as a featured blog image."

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )

    image_url = response.data[0].url

    os.makedirs("images", exist_ok=True)
    path = os.path.join("images", filename)
    img_data = requests.get(image_url).content

    with open(path, "wb") as f:
        f.write(img_data)

    return path
