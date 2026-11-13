import os
import re
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load API key
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

if not API_KEY:
    raise ValueError("YouTube API key not found in .env file")

# Connect to YouTube API
youtube = build("youtube", "v3", developerKey=API_KEY)


# Read India dataset
df = pd.read_csv("youtube_data_india.csv")

# Extract channel ID or handle from NAME column
def extract_channel_ref(name):
    match = re.search(r"@([A-Za-z0-9._-]+)", str(name))
    return match.group(1) if match else None


df["channel_ref"] = df["NAME"].apply(extract_channel_ref)

channel_stats = []

# Fetch channel statistics
for ref in df["channel_ref"].dropna().unique():

    try:
        if ref.startswith("UC"):

            response = youtube.channels().list(
                part="snippet,statistics",
                id=ref
            ).execute()

        else:

            response = youtube.channels().list(
                part="snippet,statistics",
                forHandle=ref
            ).execute()

        for channel in response.get("items", []):

            stats = {
                "channel_ref": ref,
                "channel_name": channel["snippet"]["title"],
                "total_subscribers": channel["statistics"].get("subscriberCount"),
                "total_views": channel["statistics"].get("viewCount"),
                "total_videos": channel["statistics"].get("videoCount")
            }

            channel_stats.append(stats)

    except Exception as e:
        print(f"Error fetching {ref}: {e}")


# Convert statistics into DataFrame
stats_df = pd.DataFrame(channel_stats)

# Merge original data with YouTube statistics
combined_df = df.merge(
    stats_df,
    on="channel_ref",
    how="left"
)

# Save updated dataset
combined_df.to_csv(
    "updated_youtube_data_india.csv",
    index=False
)

# Display results
print("\nUpdated India YouTube Data:")
print(combined_df.head(10))

print("\nTotal channels:", len(combined_df))
print("Successfully fetched:", combined_df["channel_name"].notna().sum())

print("\nUpdated CSV saved successfully!")
