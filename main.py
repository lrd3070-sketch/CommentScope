from fileinput import filename
import os
import requests
from dotenv import load_dotenv
import pandas as pd
import re
def extract_youtube_video_id(url):
    """
    Extracts the YouTube video ID from a given URL.
    """
    pattern = r"(?:v=|youtu\.be/|shorts/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern,url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")
    
def save_comments(comments):
    rows = []
    for comment in comments:
        rows.append({
            "type": "top_level",
            "comment_id": comment["comment_id"],
            "text": comment["text"],
            "likes": comment["likes"],
            "published_at": comment["published_at"]
        })
        for reply in comment["replies"]:
            rows.append({
                "type": "reply",
                "comment_id": reply["reply_id"],
                "text": reply["text"],
                "likes": reply["likes"],
                "published_at": reply["published_at"]
            })
    df = pd.DataFrame(rows)
    df.to_csv("YouTube_comments.csv", index = False)
load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")
if not api_key:
    raise ValueError("YOUTUBE_API_KEY is not set in the environment variables.")
video_url = input("Enter YouTube video URL: ")
video_id = extract_youtube_video_id(video_url)

url = "https://www.googleapis.com/youtube/v3/commentThreads"
while True:
    try:
        max_comments = int(input("Enter the maximum number of comments to fetch: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

comments = []
page_token = None

while len(comments) < max_comments:

    params = {
        "part": "snippet",
        "videoId": video_id,
        "maxResults": min(max_comments - len(comments), 100),
        "key": api_key,
        "textFormat": "plainText"
    }
    if page_token:
        params["pageToken"] = page_token
    responses = requests.get(url, params=params)
    data = responses.json()

    for num, item in enumerate(data["items"],start =1):
        top_comment = item["snippet"]["topLevelComment"]
        info = top_comment["snippet"]
        comments.append({
            "number": len(comments)+1,
            "comment_id": top_comment["id"],
            "text": info["textDisplay"],
            "likes": info["likeCount"],
            "published_at": info["publishedAt"],
            "replies": []
        })
        if item["snippet"]["totalReplyCount"] > 0:
            reply_url = "https://www.googleapis.com/youtube/v3/comments"
            reply_params = {
                "part": "snippet",
                "parentId": top_comment["id"],
                "maxResults": 100,
                "key": api_key,
                "textFormat": "plainText"
            }
            reply_responses = requests.get(reply_url, params=reply_params)
            reply_data = reply_responses.json()
            for reply in reply_data["items"]:
                reply_info = reply["snippet"]
                comments[-1]["replies"].append({
                    "reply_id": reply["id"],
                    "text": reply_info["textDisplay"],
                    "likes": reply_info["likeCount"],
                    "published_at": reply_info["publishedAt"]
                })
    page_token = data.get("nextPageToken")

    if not page_token:
        break

save_comments(comments)
print(f"Saved {len(comments)} top_level comments to file")
print(f"Saved {sum(len(comment['replies']) for comment in comments)} replies to file")


    
                              
