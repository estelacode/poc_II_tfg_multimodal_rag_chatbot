
#### TFG - Redesigning the User Experience with Artificial Intelligence: Fashion Industry Specialized Chatbot
## Poc II: Multimodal RAG Chatbot

## Overview 
A multimodal RAG (Retrieval-Augmented Generation) chatbot that processes text queries and returns responses combining text and images. The system retrieves semantically relevant visual content from a multimodal vector store built from a custom dataset of 3D footwear images. Image and text embeddings are generated using OpenCLIP and Cohere, while multimodal reasoning is performed using LLaVA 1.6 and Llama 3.2 Vision. The application is implemented with LlamaIndex and a Gradio-based web interface.
## Demo
![Demo_PoC_II_Multimodal RAG Chatbot 1](https://github.com/estelacode/poc_multimod_chatbot_chroma/blob/master/demo_interface/demo12_llama_3_2_vision_11B.jpg)
![Demo_PoC_II_Multimodal RAG Chatbot 2](https://github.com/estelacode/poc_multimod_chatbot_chroma/blob/master/demo_interface/demo14_llama_3_2_vision_11B.jpg)

## Features
- Multimodal chatbot: text input with text + image output
- Multimodal RAG architecture with unified text–image embeddings
- Semantic retrieval of images from text queries
- MultiModalVectorStoreIndex for multimodal vector storage
- Image embeddings using OpenCLIP
- Text embeddings using Cohere embed-multilingual-v3.0
- Large Multimodal Models: LLaVA 1.6 and Llama 3.2 Vision
- Interactive web UI built with Gradio

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
![3.12.9](https://img.shields.io/badge/3.12-CE6ACC?style=for-the-badge&logoColor=white)
![LlamaIndex](https://img.shields.io/badge/LlamaIndex-black?style=for-the-badge&logo=llamaindex&logoColor=white)
![0.11.23](https://img.shields.io/badge/0.11.23-CE6ACC?style=for-the-badge&logoColor=white)


`Multimodal / Embeddings`

![CLIP](https://img.shields.io/badge/CLIP-black?style=for-the-badge&logo=openai&logoColor=white)
![open--clip](https://img.shields.io/badge/open--clip-CE6ACC?style=for-the-badge&logoColor=white)
![Cohere-Embeddings](https://img.shields.io/badge/Cohere--Embeddings-black?style=for-the-badge&logo=cohere&logoColor=white)
![embed-multilingual-v3.0](https://img.shields.io/badge/embed--multilingual--v3.0-CE6ACC?style=for-the-badge&logoColor=white)

`Vector Database`

![ChromaDB](https://img.shields.io/badge/ChromaDB-black?style=for-the-badge&logoColor=white)
![0.5.18](https://img.shields.io/badge/0.5.18-CE6ACC?style=for-the-badge&logoColor=white)

`LLM`

![Ollama](https://img.shields.io/badge/Ollama-black?style=for-the-badge&logo=ollama&logoColor=white)
![LLaVA-13B](https://img.shields.io/badge/llava:13b-CE6ACC?style=for-the-badge&logoColor=white)
![Llama3.2-Vision](https://img.shields.io/badge/llama3.2--vision:11b-CE6ACC?style=for-the-badge&logoColor=white)


`Frontend`

![Gradio](https://img.shields.io/badge/Gradio-black?style=for-the-badge&logo=gradio&logoColor=white)

`Infrastructure | Dev Tools`

![Poetry](https://img.shields.io/badge/Poetry-black?style=for-the-badge&logo=python&logoColor=white)
![Dependency-Management](https://img.shields.io/badge/Dependency--Management-CE6ACC?style=for-the-badge&logoColor=white)

## Setup

```bash
# 1. Install Poetry (required) - https://python-poetry.org/docs/#installing-with-the-official-installer
# Windows (PowerShell):
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
poetry --version

# 2. Clone the repository
git clone https://github.com/estelacode/poc_II_tfg_multimodal_rag_chatbot
cd poc_II_tfg_multimodal_rag_chatbot

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
```bash
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
```
## Roadmap
- Support multimodal queries (text + image input)
- Expand dataset with more product images and descriptions
- Improve retrieval accuracy with alternative multimodal embeddings
- Implement reranking techniques for image retrieval
- Add structured metadata extraction (brand, color, materials)
- Apply prompt engineering techniques to improve response quality
- Introduce evaluation methods and metrics for multimodal retrieval and generation
- Replace in-memory vector store with scalable vector databases
- Deploy the application as a cloud service

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
