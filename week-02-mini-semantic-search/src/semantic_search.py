import chromadb
from chromadb.utils import embedding_functions
import os

class MiniSemanticSearch:
    def __init__(self, persist_directory='./chroma_db'):
        self.persist_directory = persist_directory
        os.makedirs(persist_directory, exist_ok=True)
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name='all-MiniLM-L6-v2'
        )
        self.collection = self.client.get_or_create_collection(
            name='faq_collection',
            embedding_function=self.embedding_fn
        )

    def add_documents(self, df):
        '''Add FAQ documents to ChromaDB.'''
        documents = []
        metadatas = []
        ids = []
        for idx, row in df.iterrows():
            doc_text = f"Q: {row['question']} A: {row['answer']}"
            documents.append(doc_text)
            metadatas.append({
                'question': str(row['question']),
                'answer': str(row['answer'])
            })
            ids.append(f'id_{idx}')
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        return len(documents)

    def search(self, query, n_results=3):
        '''Search for top n similar FAQs.'''
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results
