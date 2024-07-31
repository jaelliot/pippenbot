# Pippenbot

Welcome to Pippenbot, a cutting-edge chatbot assistant that combines multiple agents, language models, and advanced AI capabilities. In this README file, I'll provide an in-depth overview of the system's architecture and functionality, as well as installation and usage instructions.

## Purpose

Pippenbot aims to provide an advanced conversational agent that recruiters can interact with to learn more about you. By leveraging multiple agents and language models, Pippenbot delivers insightful, relevant, and accurate responses.

## Architecture Overview

Pippenbot consists of several primary components:

1. **Multiple Agents**: Utilizes a mixture of agents with access to vector databases, APIs, and the internet for enhanced search capabilities.
2. **Language Models**: Employs the Llama and Mistral LLMs hosted on Groq for powerful language understanding and inference.
3. **Task-Specific Agents**: Includes agents dedicated to tasks such as analyzing, critiquing, debating, synthesizing information, and providing contextual responses.
4. **Agentic RAG System**: Integrates retrieval-augmented generation to improve response accuracy and relevance.

## Functionality

Here's how Pippenbot's retrieval-augmented generation (RAG) works:

1. **User Query Processing**: Users enter a query, which is processed into search keywords and paraphrased requests.
2. **Augmented Search**: Executes searches using vector databases, APIs, and internet sources.
3. **Contextual Analysis**: Analyzes and filters results based on relevance to the user's query.
4. **Vector Similarity Ranking**: Ranks results by similarity to the user's prompt.
5. **Context Generation**: Extracts and synthesizes relevant data from sources to generate a response.
6. **Response Generation**: Provides answers using the synthesized context and user preferences.

## Key Features

Pippenbot offers several key advantages:

- **Domain-specific knowledge**: Enhances responses with domain-specific information without additional training or fine-tuning.
- **Control over context**: Allows users to specify the amount of context provided to the LLM.
- **Rolling context window**: Maintains conversation history for continuous dialogue.
- **Query-answer matching**: Ensures relevance of results before providing context.
- **Minimal dependencies**: Requires minimal Python dependencies and leverages Groq for heavy computation.

## Installation

### Prerequisites

- A machine with Docker installed.

- A GROQ API key.

### Setup Steps

1. Clone the repository:

```
git clone https://github.com/username/pippenbot.git
```

2. Navigate to the project directory:

```
cd pippenbot
```

3. Create a `secrets.toml` file and add your GROQ API key:

```
echo "GROQ_API_KEY='your_api_key_here'" > secrets.toml
```

4. Build the Docker container:

```
docker build -t pippenbot .
```

5. Run the Docker container:

```
docker run -d -p 7860:7860 --env-file=secrets.toml pippenbot
```

## Usage

Once the Docker container is running, open a web browser and navigate to `http://localhost:7860` to start interacting with Pippenbot. The interface will allow you to enter queries and receive responses based on the integrated agents and language models.

## Managing agent contexts

Agent contexts allow Pippenbot to adjust its responses based on specific topics or lines of thinking. Users can define and manage agent contexts to tailor the chatbot's behavior and improve response accuracy.

## Downloading models

Pippenbot utilizes the Llama and Mistral models hosted on Groq. The necessary models will be automatically accessed via the provided GROQ API key.

## Performance

Pippenbot's performance is optimized through the use of Groq for heavy computations, ensuring fast and accurate responses. Users may notice variations in response times based on the complexity of queries and the amount of context processed.

## Saving Settings

Changes made during a session will persist until the container is stopped. To ensure settings are saved between sessions, update the relevant configuration files before restarting the container.

# FAQ

- **Can I use Pippenbot for other purposes?**
  - Yes, while Pippenbot is designed as a mock persona for recruiters, it can be adapted for other conversational AI applications.
- **What if I encounter issues with the Docker container?**
  - Ensure you have the latest version of Docker installed and that your GROQ API key is correctly set in the `secrets.toml` file.
- **How do I update the models used by Pippenbot?**
  - Models are managed through Groq. Ensure your API key has the necessary permissions to access updated models.

# Credits

Thanks to the Groq team for providing powerful AI capabilities and to the broader machine learning community for their contributions to advanced language models and tools.

# TO DO

# integrate this: <https://blog.streamlit.io/land-your-dream-job-build-your-portfolio-with-streamlit/>

# And this: <https://blog.streamlit.io/land-your-dream-job-build-your-portfolio-with-streamlit/>

# And This: <https://blog.streamlit.io/how-to-improve-streamlit-app-loading-speed/>

# Add stuff from this too: <https://docs.llamaindex.ai/en/stable/>

# maybe add this too: <https://www.youtube.com/watch?v=JLVsFIXtvKE>

# Remove the embed_rss and the endorsements

# Fix the CSS
