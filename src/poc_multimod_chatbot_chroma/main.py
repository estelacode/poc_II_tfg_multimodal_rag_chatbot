from llama_index.core.indices.multi_modal.base import MultiModalVectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import SimpleDirectoryReader, StorageContext
from llama_index.embeddings.clip import ClipEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.cohere import CohereEmbedding
from dotenv import load_dotenv
import os 

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
    # Create Cohere embedding 
    embed_model = CohereEmbedding(api_key=os.getenv('COHERE_API_KEY'))

    # cretate image embed model
    image_embed_model = ClipEmbedding()

    # Define the sentence splitter
    node_parser = SentenceSplitter.from_defaults()
    image_nodes = node_parser.get_nodes_from_documents(image_documents)
    text_nodes = node_parser.get_nodes_from_documents(text_documents)

    # Create multimodal index
    index = MultiModalVectorStoreIndex(
    nodes = image_nodes + text_nodes,
    image_embed_model=image_embed_model,
    embed_model = embed_model
    )

    return index


def ingestion():

    # Load the context images and text
    image_documents, text_documents = load_documents()

    # Create index
    index = create_multimodal_index(image_documents, text_documents)





if __name__ == "__main__":
   print('Hello World')
   