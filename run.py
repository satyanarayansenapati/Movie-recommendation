from src.main import *

data = load_data("data/movie_dataset.csv")
split_data_to_store = split_data(data)
storing_to_vdb = store_data(split_data_to_store)

movie_name = str(input("Enter a movie name\n"))
querying = query_data(storing_to_vdb,movie_name)
print(querying)