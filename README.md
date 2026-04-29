# 💬 customer-feedback-ai-chatbot

# 💬 Customer Feedback AI Chatbot (RAG + LangGraph)

This project is a **Retrieval-Augmented Generation (RAG) chatbot** enhanced with **LangGraph**.  
It allows users to ask questions about customer feedback data and get **structured insights like summary, sentiment, and suggestions**.

---

## 🚀 Features

* 📂 Load customer feedback from CSV file  
* ✂️ Split large text into manageable chunks  
* 🔍 Convert text into embeddings  
* 🧠 Store embeddings in vector database  
* 🔎 Retrieve most relevant feedback  
* 🤖 Generate structured insights using LLM  
* 🔗 Multi-step pipeline using LangGraph  
* 🌐 Interactive UI using Streamlit  
* 📊 Shows retrieved source data for transparency  

---

## 🛠️ Tech Stack

* Python  
* LangChain  
* LangGraph  
* Qdrant (Vector Database)  
* Ollama (LLM & Embeddings)  
* Streamlit (Frontend UI)  

---

## 📁 Project Structure

```
project/
│
├── customer_feedback.py          # Main Streamlit app
├── customer_feedback.ipynb       
├── customer_feedback.csv         # Dataset
└── README.md                     # Documentation
```


---

## ⚙️ Installation

### 1️⃣ Clone repository

```bash
git clone https://github.com/your-username/customer-feedback-chatbot.git
cd customer-feedback-chatbot

---

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
```

Activate:

**Windows:**

```bash
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit langchain langchain-community langchain-qdrant qdrant-client langchain-ollama langgraph
```

---

## 🤖 Setup Ollama Models

Install **Ollama** and download required models:

```bash
ollama pull llama3.2:1b
ollama pull qwen3-embedding:0.6b
```

---

## ▶️ Run the Application

```bash
streamlit run customer_feedback.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. Load customer feedback from CSV  
2. Split feedback into smaller chunks  
3. Convert chunks → embeddings  
4. Store embeddings in Qdrant  
5. User asks a question  
6. Retrieve top relevant feedback (k=3)  
7. Pass context + question to LLM  
8. Generate structured output:
   - Summary  
   - Sentiment  
   - Suggestions  

👉 This pipeline is managed using **LangGraph nodes**:

- Retrieve Node  
- Generate Node  

👉 This approach is called **RAG (Retrieval-Augmented Generation)**

---

## 🔗 LangGraph Workflow

User Query
   ↓
Retrieve Node (Qdrant)
   ↓
Generate Node (LLM)
   ↓
Final Answer

## 💡 Example Usage

**Input:**

```
What are customers saying about delivery service?
```

**Output:**

```
Customers report delays in delivery and inconsistent timing.

Sentiment:
Mostly Negative

Suggestions:
Improve logistics planning and provide accurate delivery tracking.
```

---

## 📄 Output Sections

The chatbot returns:

* ✅ **Summary** → Overall feedback understanding  
* 😊 **Sentiment** → Positive / Negative / Neutral  
* 💡 **Suggestions** → Actionable improvements  

---

## ⚠️ Notes

* Ensure `customer_feedback.csv` is in correct path  
* Make sure Ollama is running  
* First run may take time (model loading)  
* Using `@st.cache_resource` improves performance  

---

## 🚀 Future Improvements

* 📤 Upload CSV dynamically  
* 💬 Add chat history (memory)  
* 🧠 Multi-agent workflows using LangGraph  
* 📊 Advanced analytics dashboard  
* ☁️ Deploy to cloud (AWS / Streamlit Cloud)  

---

## 👩‍💻 Author

**Sandhiya**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
