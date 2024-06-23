from src.main import *
from fastapi import FastAPI

data = load_data("data/movie_dataset.csv")
split_data_to_store = split_data(data)
storing_to_vdb = store_data(split_data_to_store)

# initializing FastAPI
app = FastAPI()


@app.get("/query")
async def find_similar_movie(movie:str):
    result = query_data(vdb=storing_to_vdb,movie_name=movie)
    return {"output": result}