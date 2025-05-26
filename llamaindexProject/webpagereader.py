from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex



import os
from dotenv import load_dotenv
load_dotenv()

def main(url:str) -> None:



    document = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    index = VectorStoreIndex.from_documents(documents=document)
    query_engine = index.as_query_engine()
    response = query_engine.query("what is generative AI?")
    print(response)


if __name__ =="__main__":
    main(url="https://aws.amazon.com/what-is/generative-ai/")