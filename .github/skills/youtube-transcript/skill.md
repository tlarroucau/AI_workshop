name: YouTube Transcript Fetcher
description: A skill to fetch transcripts from YouTube videos using their URL or ID.

---

Use this skill when the user asks to get the transcript, text, or content of a YouTube video.

# Steps

1.  Identify the YouTube Video URL or ID from the user's prompt.
2.  Run the python script `scripts/fetch.py` with the video ID/URL as an argument.
3.  Output the retrieved transcript text.

# Tools

-   `scripts/fetch.py`: Python script to fetch the transcript using `youtube-transcript-api`.
