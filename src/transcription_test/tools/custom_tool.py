"""Module providing custom tools."""

from typing import Tuple
import json
import requests
from crewai_tools import BaseTool
from youtube_transcript_api import YouTubeTranscriptApi

QLLM_QUESTION_URL = "https://studio-api-dev.aisquare.com/api/v1/qllm/question/"
QLLM_LOGIN_URL = "https://studio-api-dev.aisquare.com/api/v1/token/"


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

        video_id = self.get_video_id_from_url(video_url)

        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text_list = [
            data["text"]
            for data in transcript_data
        ]
        transcript_text = " ".join(transcript_text_list)

        return transcript_text


class QuestionGenerationTool(BaseTool):
    name: str = "Question Generation Tool"
    description: str = (
        "This tool generates a multiple-choice quiz question from the text input provided"
    )

    def qllm_login(self) -> Tuple[str, str]:
        "Logs into QLLM API and returns refresh and access tokens"

        payload = json.dumps({
            "username": "jatin",
            "password": "jatin@123"
        })
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.request(
            "POST",
            QLLM_LOGIN_URL,
            headers=headers,
            data=payload,
            timeout=10,
        )
        response_json = response.json()

        return response_json["refresh"], response_json["access"]

    def qllm_generate_question(
        self,
        access_token: str,
        domain: str,
        subdomain: str,
        text: str,
    ) -> str:
        "Generates question with QLLM API"

        payload = json.dumps({
            "domain": domain,
            "subdomain": subdomain,
            "user_context": f"Ensure the question is based on the following transcription: {text}",
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.request(
            "POST",
            QLLM_QUESTION_URL,
            headers=headers,
            data=payload,
            timeout=10,
        )

        return response.text

    def _run(self, domain: str, subdomain: str, text: str) -> str:

        _, access_token = self.qllm_login()

        return self.qllm_generate_question(access_token, domain, subdomain, text)
