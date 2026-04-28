import streamlit as st
from typing import TypedDict, List

# LangChain
from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_qdrant import QdrantVectorStore

# Qdrant
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

# LangGraph
from langgraph.graph import StateGraph

# ---------------- UI ----------------
st.set_page_config(page_title="💬 Customer Feedback Chatbot", layout="wide")
st.title("💬 Customer Feedback AI Chatbot")

query = st.text_input("Ask about customer feedback:")

# ---------------- LOAD DATA ----------------
@st.cache_resource
def load_data():
    loader = CSVLoader(file_path="customer_feedback.csv")
    return loader.load()

data = load_data()

# ---------------- SPLIT ----------------
@st.cache_resource
def split_data(data):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(data)

docs = split_data(data)

# ---------------- EMBEDDINGS ----------------
@st.cache_resource
def get_embeddings():
    return OllamaEmbeddings(model="qwen3-embedding:0.6b")

embeddings = get_embeddings()

# ---------------- QDRANT ----------------
@st.cache_resource
def get_vector_store(docs):
    client = QdrantClient(":memory:")

    vector_size = len(embeddings.embed_query("test"))

    if not client.collection_exists("feedback"):
        client.create_collection(
            collection_name="feedback",
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )

    vector_store = QdrantVectorStore(
        client=client,
        collection_name="feedback",
        embedding=embeddings
    )

    vector_store.add_documents(docs)

    return vector_store

vector_store = get_vector_store(docs)
retriever = vector_store.as_retriever()

# ---------------- LLM ----------------
@st.cache_resource
def get_llm():
    return OllamaLLM(model="llama3.2:1b")

llm = get_llm()

# ---------------- LANGGRAPH STATE ----------------
class State(TypedDict):
    query: str
    docs: List
    answer: str

# ---------------- RETRIEVE ----------------
def retrieve(state: State):
    docs = retriever.invoke(state["query"])
    return {"docs": docs}

# ---------------- GENERATE ----------------
def generate(state: State):
    context = " ".join([doc.page_content for doc in state["docs"]])

    prompt = f"""
    You are a business analyst AI.

    Analyze customer feedback and give clear insights.

    Context:
    {context}

    Question:
    {state['query']}

    Give:
    - Summary
    - Sentiment (Positive/Negative)
    - Suggestions (if any)
    """

    answer = llm.invoke(prompt)
    return {"answer": answer}

# ---------------- GRAPH ----------------
@st.cache_resource
def build_graph():
    graph = StateGraph(State)

    graph.add_node("retrieve", retrieve)
    graph.add_node("generate", generate)

    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "generate")

    return graph.compile()

app = build_graph()

# ---------------- RUN ----------------
if query:
    result = app.invoke({"query": query})

    st.subheader("🤖 AI Insight")
    st.write(result["answer"])

    with st.expander("📄 Retrieved Feedback Data"):
        for doc in result["docs"]:
            st.write(doc.page_content)