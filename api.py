from run import storing_to_vdb
from src.main import query_data
from fastapi import FastAPI

vdb = storing_to_vdb

# initializing FastAPI
app = FastAPI()


@app.get("/query")
async def find_similar_movie(movie:str):
    result = query_data(vdb=vdb,movie_name=movie)
    return {"output": result}
