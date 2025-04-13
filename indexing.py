import os
import nest_asyncio
from decouple import config
from llama_cloud_services import LlamaParse
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex

os.environ['LLAMA_CLOUD_API_KEY'] = config('LLAMA_CLOUD_API_KEY')
os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

parser = LlamaParse(result_type='markdown')
index = None
file_extractor = {'.pdf': parser, '.docx': parser}

nest_asyncio.apply()

async def index_documents(uploaded_files):
    documents = SimpleDirectoryReader(
        input_files=uploaded_files, 
        file_extractor=file_extractor
    ).load_data()
    
    global index
    index = VectorStoreIndex.from_documents(documents)


async def search_by_index(body):
    try:
        query_engine = index.as_query_engine()
    except:
        return 'Load documents first'
    
    prompt = body.get('prompt', '')
    abstractive = body.get('abstractive', True)
    length = body.get('length', None)

    prompt = prompt + ' I need abstractive response' if abstractive else prompt + ' I need extractive response'
    prompt = prompt + f' limited to {length} characters' if length else prompt

    return query_engine.query(prompt)