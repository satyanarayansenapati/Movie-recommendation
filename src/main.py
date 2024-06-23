from src import logger
# loading the data 

# import
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings()


def load_data(filepath:str):
    '''
    Loads the data into vector storage
    
    '''
    try:
        loader = CSVLoader(file_path=filepath, encoding='utf-8')
        data = loader.load()
        logger.info("Data loaded")
        return data
    except Exception as e:
        logger.error(f"Error while loading the data. Error : {e}")

   
def split_data(data):

    #initilalizing the text splitter
    text_splitter = CharacterTextSplitter(
        separator="\n\n",
            chunk_size=500,
            chunk_overlap=80,
            length_function=len,
            is_separator_regex=False
    )

    try:
        # splitting the data into chunks
        split_data = text_splitter.split_documents(data)
        logger.info("Data splitted")
        return split_data

    except Exception as e:
        logger.error(f"Error during splitting the data. Error is {e}")


def store_data(split_data):
    # store the data to vdb

    
    try:
        vdb = FAISS.from_documents(documents=split_data, embedding=embeddings)
        logger.info("Data is stored in vdb")
        return vdb
    
    except Exception as e:
        logger.error(f"Error while storing the data. Error is {e}")



def query_data(vdb,movie_name):
    # querying similar movie names

    embed_movie = embeddings.embed_query(movie_name)

    try:
        # running search
        search_result = vdb.similarity_search_by_vector(embed_movie, fetch_k = 3)
        logger.info("Searching done")

    except Exception as e:
        logger.error(f"Error while searching similar movie. Error is {e}")
    
    # processing the search result
    result_list = []
                
    for i in search_result:
                    
        # converting list to string
        text = str(i)
        txt = ''

        for i in range(text.find('movie title :')+len('movie title :'),text.find('movie info :')-2):
            txt +=text[i]

        result_list.append(txt)
            
    return result_list[1:]   
