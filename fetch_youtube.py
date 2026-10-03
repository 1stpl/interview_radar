import sys

from youtube_transcript_api import YouTubeTranscriptApi
from hello_llm import summarise_interview
def get_transcript(video_id):
    ytt_api = YouTubeTranscriptApi()
    fetched = ytt_api.fetch(video_id, languages=["en"])

    text = ""
    for snippet in fetched:
        text = text + snippet.text + " "

    return text


if __name__ == "__main__":


    my_text = get_transcript("leXRiJ5TuQo")
    print(my_text)
    print(len(my_text))

    with open("D:\\interview_radar\\youtube_1st_transcript.txt", "w" , encoding="utf-8") as f:
        f.write(my_text)

    print(summarise_interview(my_text))