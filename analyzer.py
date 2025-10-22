"""
YouTube Trending Topics Analyzer
Author: Waqas
Description:
Fetches trending videos from YouTube using YouTube Data API v3,
analyzes trending keywords, and categorizes topics.
"""

from googleapiclient.discovery import build
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

# -------------------------------
# STEP 1: API SETUP
# -------------------------------
API_KEY = "AIzaSyClXjGzb2xDj0eZGGkKM4N_IcsMf53MGh8"  # 🔑 Replace with your own API key
REGION = "US"  # You can change to 'PK', 'IN', etc.

# Initialize YouTube API client
youtube = build("youtube", "v3", developerKey=API_KEY)

# -------------------------------
# STEP 2: FETCH TRENDING VIDEOS
# -------------------------------
print("Fetching trending videos...")

request = youtube.videos().list(
    part="snippet,statistics",
    chart="mostPopular",
    regionCode=REGION,
    maxResults=100
)
response = request.execute()

videos = []
for item in response["items"]:
    video = {
        "title": item["snippet"]["title"],
        "channel": item["snippet"]["channelTitle"],
        "categoryId": item["snippet"]["categoryId"],
        "views": int(item["statistics"].get("viewCount", 0)),
        "publishedAt": item["snippet"]["publishedAt"],
        "description": item["snippet"]["description"]
    }
    videos.append(video)
pd.set_option('display.max_columns', 30)
df = pd.DataFrame(videos)
print(f"\n✅ Fetched {len(df)} trending videos from region: {REGION}\n")

# -------------------------------
# STEP 3: KEYWORD ANALYSIS
# -------------------------------
print("Analyzing trending keywords...")

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

text = " ".join(df["title"].tolist())
tokens = word_tokenize(text.lower())
words = [w for w in tokens if w.isalpha() and w not in stopwords.words("english")]

freq = nltk.FreqDist(words)
common_words = freq.most_common(20)

print("\n🔥 Top 50 Trending Keywords:")
for word, count in common_words:
    print(f"{word}: {count}")

# -------------------------------
# STEP 4: CATEGORY CLASSIFICATION
# -------------------------------
print("\nCategorizing topics...")

topic_map = {
    "ai": "Technology",
    "tech": "Technology",
    "robot": "Technology",
    "football": "Sports",
    "cricket": "Sports",
    "goal": "Sports",
    "recipe": "Food",
    "cooking": "Food",
    "song": "Entertainment",
    "music": "Entertainment",
    "movie": "Entertainment",
    "game": "Gaming",
    "gaming": "Gaming",
    "crypto": "Finance",
    "stock": "Finance",
    "market": "Finance",
    "news": "News",
    "politics": "News",

}

def categorize(title):
    for word, category in topic_map.items():
        if word in title.lower():
            return category
    return "Other"

df["category"] = df["title"].apply(categorize)

# -------------------------------
# STEP 5: DISPLAY RESULTS
# -------------------------------
print("\n📊 Trending Topics Summary:")
print(df[["title", "views", "category"]].head(10))

# -------------------------------
# STEP 6: VISUALIZE DATA
# -------------------------------
print("\nGenerating category chart...")

plt.figure(figsize=(8, 5))
df["category"].value_counts().plot(kind="bar", color="#00B894", edgecolor="black")
plt.title(f"Trending Categories on YouTube ({REGION})")
plt.xlabel("Category")
plt.ylabel("Number of Videos")
plt.tight_layout()
plt.show()

# -------------------------------
# STEP 7: SAVE RESULTS
# -------------------------------
output_file = "youtube_trending_topics.csv"
df.to_csv(output_file, index=False)
# save in my system
df.to_csv()
print(f"\n💾 Results saved to '{output_file}'")

print("\n✅ Analysis complete! Use this data to create videos on trending topics 🚀")
