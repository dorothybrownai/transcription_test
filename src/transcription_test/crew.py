"""Module defining the TranscriptionTestCrew."""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
from transcription_test.tools.custom_tool import QuestionGenerationTool, VideoToTextTool
from pydantic import BaseModel

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool, WebsiteSearchTool


class TranscriptionProperties(BaseModel):
    """Transcription properties model"""
    domain: str
    subdomain: str
    text: str


@CrewBase
class TranscriptionTestCrew():
    """TranscriptionTest crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def transcriber(self) -> Agent:
        return Agent(
            config=self.agents_config['transcriber'],
            tools=[VideoToTextTool()],
            verbose=True
        )

    @agent
    def domain_parser(self) -> Agent:
        return Agent(
            config=self.agents_config['domain_parser'],
            verbose=True
        )

    @agent
    def quiz_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['quiz_generator'],
            tools=[QuestionGenerationTool()],
            verbose=True
        )

    @task
    def transcription_task(self) -> Task:
        return Task(
            config=self.tasks_config['transcription_task'],
        )

    @task
    def domain_parsing_task(self) -> Task:
        response_json = Task(
            config=self.tasks_config['domain_parsing_task'],
            output_json=TranscriptionProperties,
        )

        print("Response: ", response_json)

        return response_json

    @task
    def quiz_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['quiz_generation_task'],
            output_file='output/report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TranscriptionTest crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
