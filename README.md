
#### TFG - Redesigning the User Experience with Artificial Intelligence: Fashion Industry Specialized Chatbot
## Poc II: Multimodal RAG Chatbot

## Overview 

## Demo
![Demo_PoC_II_Multimodal RAG Chatbot]([https://github.com/estelacode/poc_tfg_chatbot_texto/blob/master/demo/Demo_0_PoC_I_Chatbot_Rag_Unimodal.jpg](https://github.com/estelacode/poc_multimod_chatbot_chroma/blob/master/demo_interface/demo6_llama_3_2_vision_11B.jpg))

## Features

## Architecture
High-level structure of the application:
![PoC_II_High_level_Architecture_Diagram](https://github.com/estelacode/poc_multimod_chatbot_chroma/blob/master/docs/diagrams/Poc_II_High_Level_Architecture_Diagram.jpg)

### `Sequence Diagram`
![PoC_II_Sequence_Diagram](https://github.com/estelacode/poc_multimod_chatbot_chroma/blob/master/docs/diagrams/PoC_II_Sequence_Diagram.png)

#### Sequence Flow:

1. User submits a query (text) via the Frontend.
2. Frontend sends the query to the Backend.
3. Backend retrieves the most relevant documents and images from the Multimodal Vector Store using semantic search (Cohere embeddings for text + CLIP embeddings for images).
4. Backend sends the query along with the retrieved context to the Ollama Multimodal LLM (llava:13b or llama3.2-vision:11b).
5. LLM generates a multimodal response (text and/or image) based on the provided context.
6. Backend returns the generated response to the Frontend.
7. Frontend displays the generated response (text and image) to the user.

## Tech Stack

`Backend`

![Python](https://img.shields.io/badge/Python-black?style=for-the-badge&logo=python&logoColor=white)
![3.12.9](https://img.shields.io/badge/3.12-9370DB?style=for-the-badge&logoColor=white)
![LlamaIndex](https://img.shields.io/badge/LlamaIndex-black?style=for-the-badge&logo=llamaindex&logoColor=white)
![0.11.23](https://img.shields.io/badge/0.11.23-9370DB?style=for-the-badge&logoColor=white)


`Multimodal / Embeddings`

![CLIP](https://img.shields.io/badge/CLIP-black?style=for-the-badge&logo=openai&logoColor=white)
![open--clip](https://img.shields.io/badge/open--clip-9370DB?style=for-the-badge&logoColor=white)
![Cohere-Embeddings](https://img.shields.io/badge/Cohere--Embeddings-black?style=for-the-badge&logo=cohere&logoColor=white)
![embed-multilingual-v3.0](https://img.shields.io/badge/embed--multilingual--v3.0-9370DB?style=for-the-badge&logoColor=white)

`Vector Database`

![ChromaDB](https://img.shields.io/badge/ChromaDB-black?style=for-the-badge&logoColor=white)
![0.5.18](https://img.shields.io/badge/0.5.18-9370DB?style=for-the-badge&logoColor=white)

`LLM`

![Ollama](https://img.shields.io/badge/Ollama-black?style=for-the-badge&logo=ollama&logoColor=white)
![LLaVA-13B](https://img.shields.io/badge/llava:13b-9370DB?style=for-the-badge&logoColor=white)
![Llama3.2-Vision](https://img.shields.io/badge/llama3.2--vision:11b-9370DB?style=for-the-badge&logoColor=white)


`Frontend`

![Gradio](https://img.shields.io/badge/Gradio-black?style=for-the-badge&logo=gradio&logoColor=white)

`Infrastructure | Dev Tools`

![Poetry](https://img.shields.io/badge/Poetry-black?style=for-the-badge&logo=python&logoColor=white)
![Dependency-Management](https://img.shields.io/badge/Dependency--Management-9370DB?style=for-the-badge&logoColor=white)

## Setup

```bash
# 1. Install Poetry (required) - https://python-poetry.org/docs/#installing-with-the-official-installer
# Windows (PowerShell):
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
poetry --version

# 2. Clone the repository
git clone https://github.com/estelacode/poc_tfg_chatbot_texto.git
cd poc_multimod_chatbot_chroma

# 3. Select the Python interpreter for this project
poetry env use /full/path/to/python
# Example for Windows:
# poetry env use C:\Users\emada\AppData\Local\Programs\Python\Python312


# 4. Install dependencies
poetry install

# Check where the virtual environment is located (optional)
poetry env info
```

## Usage
```bash
# Run the project
poetry run python src/poc_multimod_chatbot_chroma/main.py
```
## Project Structure
POC_MULTIMOD_CHATBOT_CHROMA/
├── data/                     # Data files
├── datasets_chatbot/         # Chatbot datasets
├── demo_interface/           # Demo interface or media
├── notebooks/                # Jupyter notebooks for experiments
├── src/                      # Source code 
├── tests/                    # Test images used to evaluate multimodal capabilities
├── vectorstore/              # Vector database storage 
├── .env                      # Environment variables (keep secret)
├── .gitignore                # Git ignore rules
├── poetry.lock               # Poetry dependency lock file
├── pyproject.toml            # Poetry configuration and dependencies
└── README.md                 # Project README file

## Roadmap

## References
- [Poetry Documentation](https://python-poetry.org/docs/)
- [LlamaIndex](https://www.llamaindex.ai/)
- [LlamaIndex RAG](https://developers.llamaindex.ai/python/framework/understanding/rag/)
- [Cohere](https://cohere.com/)
- [Cohere Docs](https://docs.cohere.com/)
- [Cohere LLM University](https://cohere.com/llmu)
- [Ollama](https://ollama.com/)
- [Gradio](https://www.gradio.app/guides/quickstart)

### 👋 Author
Estela Madariaga
