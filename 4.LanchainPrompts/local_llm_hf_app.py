import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# Load environment variables
load_dotenv()
os.environ["HF_TOKEN"] = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

app = FastAPI(title="LangChain TinyLlama API")

# Initialize your exact model setup globally
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.7,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

# Request schema for validation
class QueryRequest(BaseModel):
    prompt: str

@app.post("/v1/chat")
async def chat_endpoint(request: QueryRequest):
    # Invoke the LangChain model
    result = model.invoke(request.prompt)
    return {"response": result.content}

if __name__ == "__main__":
    import uvicorn
    # Bind to 0.0.0.0 so external networks/VM components can access it
    uvicorn.run(app, host="0.0.0.0", port=8000)