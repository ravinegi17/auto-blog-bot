import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_post(topic):
    prompt = f"Write a 1000-word SEO-friendly, human-readable blog post on '{topic}'. Use headings, short paragraphs, and a friendly tone. End with a call-to-action."

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    content = response['choices'][0]['message']['content']
    slug = topic.lower().replace(" ", "-")
    meta_description = f"Discover insights on {topic} in this blog post. Stay updated!"

    return {
        'title': topic,
        'html_body': content,
        'slug': slug,
        'meta_description': meta_description
    }
