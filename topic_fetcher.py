from pytrends.request import TrendReq
import random
import sys

def get_trending_topic(region='india'):
    pytrends = TrendReq(hl='en-US', tz=330)
    try:
        df = pytrends.trending_searches(pn=region)
        if df.empty:
            print("❌ No trending topics found. Exiting.")
            sys.exit(1)
        topics = df[0].tolist()
        print("✅ Fetched trending topics:", topics[:5])
        return random.choice(topics)
    except Exception as e:
        print("❌ Error fetching trending topics:", str(e))
        sys.exit(1)
