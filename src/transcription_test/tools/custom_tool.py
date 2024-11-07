from crewai_tools import BaseTool
from youtube_transcript_api import YouTubeTranscriptApi


class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."


class VideoToTextTool(BaseTool):
    name: str = "Video to text tool"
    description: str = (
        "This tool takes url of youtube video and returns the video transcript."
    )

    def get_video_id_from_url(self, video_url: str) -> str:
        """Parses video id from video url"""

        return video_url.split('youtube.com/watch?v=')[-1]

    def _run(self, video_url: str) -> str:
        # Implementation goes here

        video_id = self.get_video_id_from_url(video_url)

        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text_list = [
            data["text"]
            for data in transcript_data
        ]
        transcript_text = " ".join(transcript_text_list)

        return transcript_text
