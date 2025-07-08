from pytrends.request import TrendReq
import random

def get_trending_topic(region='IN'):
    pytrends = TrendReq(hl='en-US', tz=330)
    try:
        df = pytrends.trending_searches(pn=region)
        topics = df[0].tolist()
    except:
        topics = ["Top AI Tools in 2025", "Latest Fitness Trends", "Plant-Based Diet Benefits"]
    return random.choice(topics)
