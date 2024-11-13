# TranscriptionTest Crew

Welcome to the TranscriptionTest Crew project, powered by [crewAI](https://crewai.com).

This project takes a URL for a YouTube video, fetches the video transcript and generates a quiz question from the video content using the QLLM API.
Currently the youtube_transcript_api is used to get the video transcript, which gets the transcripts/subtitles for a given YouTube video.

Possible next steps:

- Find a tool that actually generates the transcripts from video that can be used in enterprise applications.
- Make calls to the QLLM API to update the domain context with the video transcript and call the QLLM API to generate questions with the updated context.
- Create a condensed version of the transcript before adding it to the QLLM domain context (to reduce the amount of data we need to store)
- Scrape YouTube for each existing domain (or even new domains), then have an agent make calls to the QLLM API to update the domain context.
- Use videos from a reputable source like Coursera, EdX, Udemy, KhanAcademy, etc. so that we can ensure data quality, otherwise have some way of validating the information before updating the QLLM domain.
- Have a way to make sure that we aren't duplicating data we are already storing in the QLLM domain context.
- Return multiple questions on the given input instead of a single question.
- Allow for audio file input (Generate quiz questions from audio files that would be transcribed)
- Allow for upload of pdf or hand-written notes.
- Allow for mulitple inputs (Multiple YouTube or other videos)

This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Testing

Update the inputs in main.py with any of the following URLs then run the following command
in the terminal in the root directory transcription_test

```bash
crewai run
```

Example Videos:

- Top 6 Coding Interview Concepts (Data Structures & Algorithms): https://www.youtube.com/watch?v=ft0owvS5tQA
- Lambda Functions/ Anonymous Functions In Python | Python Interview Question #1: https://www.youtube.com/watch?v=7PlA7Seax78
- 10 Important Python Concepts In 20 Minutes: https://www.youtube.com/watch?v=Gx5qb1uHss4
- Python in 100 Seconds: https://www.youtube.com/watch?v=x7X9w_GIm1s
- Python Tutorial: https://www.youtube.com/watch?v=Sg4GMVMdOPo
- Differential Equation Introduction: https://www.youtube.com/watch?v=6o7b9yyhH7k

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/transcription_test/config/agents.yaml` to define your agents
- Modify `src/transcription_test/config/tasks.yaml` to define your tasks
- Modify `src/transcription_test/crew.py` to add your own logic, tools and specific args
- Modify `src/transcription_test/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the transcription-test Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The transcription-test Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the TranscriptionTest Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
