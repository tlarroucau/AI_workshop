import sys
import re
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url_or_id):
    """
    Extract video ID from various YouTube URL formats or return the ID if it's already one.
    """
    # If it looks like a simple ID (alphanumeric + -_), just return it
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url_or_id):
        return url_or_id

    parsed = urlparse(url_or_id)
    if parsed.hostname in {"www.youtube.com", "youtube.com"}:
        qs = parse_qs(parsed.query)
        if "v" in qs:
            return qs["v"][0]
    elif parsed.hostname == "youtu.be":
        return parsed.path.lstrip("/")
    
    return url_or_id

def fetch_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        # Combine the text parts using .text attribute
        full_text = " ".join([entry.text for entry in transcript])
        return full_text
    except Exception as e:
        return f"Error fetching transcript: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch.py <youtube_url_or_id>")
        sys.exit(1)
            
    video_input = sys.argv[1]
    video_id = extract_video_id(video_input)
    print(fetch_transcript(video_id))
