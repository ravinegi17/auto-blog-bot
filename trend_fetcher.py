import feedparser
import random
import sys

def get_tech_trending_topic():
    feed_url = "https://news.google.com/rss/headlines/section/topic/TECHNOLOGY?hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(feed_url)

    if not feed.entries:
        print("❌ No tech news topics found.")
        sys.exit(1)

    topics = [entry.title for entry in feed.entries]
    print("✅ Tech topics:", topics[:5])
    return random.choice(topics)

if __name__ == "__main__":
    selected_topic = get_tech_trending_topic()
    print("🔥 Selected Tech Topic:", selected_topic)
