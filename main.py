from trend_fetcher import get_tech_trending_topic
from gpt_blog_generator import generate_blog_post
from image_generator import generate_blog_image
from wp_poster import post_to_wordpress

def auto_run_blog():
    topic = get_tech_trending_topic()
    print(f"🔥 Selected Topic: {topic}")
    blog = generate_blog_post(topic)
    image_path = generate_blog_image(topic, filename=blog['slug'] + ".jpg")
    post_to_wordpress(blog, image_path)

if __name__ == "__main__":
    auto_run_blog()
