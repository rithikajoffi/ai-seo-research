from youtube_transcript_api import YouTubeTranscriptApi
import os

videos = {
    "kyle_roof_seo_testing": "VFLV4wWOSUE",
    "kevin_indig_seo_strategy": "p3_P0dDspBI",
    "aleyda_solis_seo": "THzBTNk9DEc",
    "gael_breton_ai_content": "zET_MTrITeI",
    "cyrus_shepard_google_seo": "tT1rPtBmGi4",
    "bernard_huang_content_optimization": "jSewQFKsqOU",
    "ross_hudgens_content_marketing": "1tr7nNrEYHk",
    "eli_schwartz_product_led_seo": "-z_w8aFqCE8",
    "authority_hacker_ai_seo": "RxwMMROFWPc",
    "ahrefs_ai_seo_content": "tiW6xRYSXmM",
}

os.makedirs("research/youtube-transcripts", exist_ok=True)

ytt = YouTubeTranscriptApi()

for name, vid_id in videos.items():
    try:
        fetched = ytt.fetch(vid_id)
        text = " ".join([t.text for t in fetched])
        with open(f"research/youtube-transcripts/{name}.md", "w", encoding="utf-8") as f:
            f.write(f"# {name}\n\n")
            f.write(f"Video ID: {vid_id}\n\n")
            f.write(f"URL: https://www.youtube.com/watch?v={vid_id}\n\n")
            f.write("## Transcript\n\n")
            f.write(text)
        print(f"✅ {name}")
    except Exception as e:
        print(f"❌ {name}: {e}")

print("\nDone!")