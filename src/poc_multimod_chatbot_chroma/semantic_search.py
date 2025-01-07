from llama_index.core.indices.multi_modal.base import MultiModalVectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import SimpleDirectoryReader, StorageContext
from llama_index.embeddings.clip import ClipEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import PromptTemplate
from llama_index.multi_modal_llms.ollama import OllamaMultiModal
from llama_index.llms.ollama import Ollama
from dotenv import load_dotenv
import os 
import gradio as gr

_ = load_dotenv(".env")


def load_documents():
    """Load the context images and text into ImageDocument and Documents"""
    # context images
    image_path = "../../datasets_chatbot/images"
    image_documents = SimpleDirectoryReader(image_path).load_data()
    

    # context text
    text_path = "../../datasets_chatbot/descriptions"
    text_documents = SimpleDirectoryReader(text_path).load_data()

    return image_documents, text_documents

def create_multimodal_index(image_documents, text_documents):

    # cretate multimodal embed model
    embeded_model = ClipEmbedding()

    # Define the sentence splitter
    node_parser = SentenceSplitter.from_defaults()
    image_nodes = node_parser.get_nodes_from_documents(image_documents)
    text_nodes = node_parser.get_nodes_from_documents(text_documents)

    # Create multimodal index
    index = MultiModalVectorStoreIndex(
    nodes = image_nodes + text_nodes,
    image_embed_model=embeded_model,
    embed_model = embeded_model
    )

    return index


def multimodal_rag(index: MultiModalVectorStoreIndex, llm:str ='llava:13b',k:int=1):

    # Define the prompt
    prompt_template = (
    "Images of shoes are provided.\n"
    "---------------------\n"
    "{context}\n"
    "---------------------\n"
    "If the images provided cannot help in answering the query\n"
    "then respond that you are unable to answer the query. Otherwise,\n"
    "using only the context provided, and not prior knowledge,\n"
    "provide an answer to the query."
    "Query: {query}\n"
    "Answer: "
    )

    prompt = PromptTemplate(prompt_template)

    # Instantiate the Ollama MultiModal LLM
    mm_model = OllamaMultiModal(model=llm, request_timeout=60.0)

    # Define rag query engine (Motor de Búsqueda)
    rag_engine = index.as_query_engine(
    llm = mm_model,
    prompt = prompt
    )

    # Retrieve settings. Finde the most relevant document
    rag_engine.retriever.image_similarity_top_k = 1
    rag_engine.retriever.similarity_top_k = k

    return rag_engine


def ingestion():

    # Load the context images and text
    image_documents, text_documents = load_documents()

    # Create index
    index = create_multimodal_index(image_documents, text_documents)

    return index


def rag_respond(query):
    global index
    global rag_engine
    response = rag_engine.query(query)
    return  gr.Image(response.metadata['image_nodes'][0].metadata['file_path']), response.response

def interface_chatbot():
    demo = gr.Interface(
    fn=rag_respond, 
    title="Multimodal Search Chatbot with Chroma and llamaIndex",
    inputs=[gr.Textbox()],   
    outputs=[gr.Image(), gr.Textbox()])
    demo.launch()


if __name__ == "__main__":
   print('Hello World')
   index = ingestion()
   rag_engine = multimodal_rag(index, llm='llama3.2-vision:11b')
   interface_chatbot()
   
   