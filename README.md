# AI Agent for Documents Summarization
AI agent for summarizing uploaded documents made as a home work for the Gilat job interview by Alexei Isac. Made with FastAPI and LlamaIndex.


## Requirements
- Docker
- `.env` file with 2 vars, check `.env.example` for reference
    - `LLAMA_CLOUD_API_KEY` can be obtained from [Llama Cloud](https://cloud.llamaindex.ai/)
    - `OPENAI_API_KEY` can be obtained from [OpenAI](https://platform.openai.com/)
- Postman. You can import the requests collection from `gilat-hw.postman_collection.json`


## Build and run with Docker
- `docker build -t gilat-hw .` then `docker run -p 8000:8000 gilat-hw`


## Use the app
- First thing you want to do is upload your documents using `/load-documents` endpoint. At this stage application work with only .pdf & .docx files. Response will contain list of loaded files and list of not supported files if you try load something else.
- Then you can use the `/search_documents` endpoint to get the summary. As you noticed, this endpoint requires you to provide a body with three fields: 
    1. `prompt`- your question as a string
    2. `abstractive` - boolean value, true if you want abstractive response, false if you want extractive response
    3. `length` - integer value, the approximate length of summary in response.