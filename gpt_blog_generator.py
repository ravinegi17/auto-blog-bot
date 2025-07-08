import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_blog_post(topic):
    prompt = f"""
You are a professional blog writer.

Write a long-form blog post (~1000 words) on the topic: **{topic}**

📝 Follow this structure:

1. Start with a featured image placeholder: `<img src="IMAGE_URL_HERE" alt="{topic}">`
2. A short intro paragraph (50–75 words).
3. Add a `<h2>Table of Contents</h2>` with anchor-linked bullets like:
   - <a href="#section1">Section 1 Title</a>
   - <a href="#section2">Section 2 Title</a>
4. Use clear, numbered or bullet-style `<h2>` and `<h3>` headings
5. Include lists like `<ul><li>...</li></ul>` and `<ol>...</ol>`
6. Conclude with a helpful wrap-up and call to action.
7. Use proper HTML tags: `<h2>`, `<h3>`, `<p>`, `<ul>`, `<strong>`, etc.
8. Keep tone friendly, informative, and slightly casual.
9. Inject light SEO keywords naturally (e.g. best tools, tips, smart tech, etc.)
10. Ensure it’s human-readable, avoids fluff, and feels real.

Output in **pure HTML** format — no markdown or code blocks.
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a professional SEO blog writer and HTML expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content
    slug = topic.lower().replace(" ", "-")
    meta_description = f"Discover the top insights on {topic}. Smart tips, tools, and techniques for curious readers."

    return {
        'title': topic,
        'html_body': content,
        'slug': slug,
        'meta_description': meta_description
    }
