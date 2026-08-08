# 🤖 Employee Support AI

An AI-powered Employee Support Assistant that helps employees perform common workplace tasks through a conversational interface. The system combines **Rule-Based Intent Detection**, **Large Language Models (LLMs)**, **Retrieval-Augmented Generation (RAG)**, and **LangGraph** to provide accurate, context-aware, and efficient responses.

Instead of relying solely on keyword matching or an LLM, the application adopts a **hybrid intent detection approach**. Frequently used employee requests are handled instantly using a rule-based classifier, while natural language or paraphrased queries are delegated to Google's Gemini model for intent classification. Policy-related questions are answered using a Retrieval-Augmented Generation (RAG) pipeline powered by **FAISS** and **Gemini Embeddings**.

The chatbot provides an interactive Streamlit interface that enables employees to retrieve information, perform self-service operations, and access company policies through a single conversational platform.

---

# ✨ Key Features

The Employee Support AI currently supports the following employee services:

- 🔐 Password Reset
- 🔓 Account Unlock
- 📅 View Leave Balance
- 📝 Apply for Leave
- 👤 View Employee Profile
- 🎫 Create Support Tickets
- 📋 View Existing Tickets
- 📚 Company Policy Assistance
- 👋 Greeting & Goodbye Responses
- 💾 Persistent JSON-based Data Storage

---

# 🧠 AI Capabilities

The application incorporates multiple AI techniques to improve user experience and response quality.

### Hybrid Intent Detection

The chatbot intelligently combines:

- Rule-Based Intent Detection for predefined employee requests
- Gemini LLM for understanding paraphrased or unseen queries

This approach provides both speed and flexibility while minimizing unnecessary LLM calls.

---

### Retrieval-Augmented Generation (RAG)

Instead of relying solely on the language model's knowledge, policy-related questions are answered using a RAG pipeline.

Relevant policy documents are:

- Converted into vector embeddings
- Stored inside a FAISS vector database
- Retrieved using semantic similarity search
- Passed to Gemini as contextual information
- Used to generate an accurate answer grounded in company documents

---

### LangGraph Workflow Orchestration

The entire chatbot workflow is orchestrated using **LangGraph**.

Rather than writing a single sequential chatbot, the application is divided into multiple workflow nodes, allowing conditional routing, modular execution, and better maintainability.

---

# 🏗️ System Architecture

```

```
                    Employee
                        │
                        ▼
                Streamlit Chat UI
                        │
                        ▼
               LangGraph Workflow
                        │
                        ▼
            Hybrid Intent Detection
                        │
         ┌──────────────┴──────────────┐
         │                             │
         ▼                             ▼
 Rule-Based Classifier          Gemini LLM
         │                             │
         └──────────────┬──────────────┘
                        ▼
                 Intent Router
                        │
      ┌─────────────────┼──────────────────┐
      │                 │                  │
      ▼                 ▼                  ▼
 Password Tool     Leave Tool       Ticket Tool
      │                 │                  │
      ├─────────────────┼──────────────────┤
      │                 │                  │
      ▼                 ▼                  ▼
 Profile Tool     Greeting Tool    Goodbye Tool
                        │
                        ▼
                 Policy Query Tool
                        │
                        ▼
                 RAG Pipeline
                        │
                        ▼
              Response Formatter
                        │
                        ▼
                 Streamlit Response
```

---

# 🎯 Project Objectives

The primary objectives of this project are:

- Automate routine employee support requests.
- Reduce manual HR and IT support workload.
- Provide instant access to employee information.
- Improve policy accessibility through semantic search.
- Demonstrate modern AI application development using LangGraph and RAG.
- Build a scalable architecture that can be extended with additional enterprise services.

---

# 🚀 Why Hybrid Intent Detection?

Traditional rule-based chatbots fail when users phrase the same request differently.

For example,

```
Reset my password
```

and

```
I can't remember my login credentials.
```

represent the same intent but use different wording.

To overcome this limitation, the chatbot follows a hybrid strategy:

- **Known requests** are handled instantly using keyword matching.
- **Unrecognized or paraphrased requests** are forwarded to Gemini for intent classification.

This reduces latency, improves flexibility, and minimizes unnecessary LLM usage while maintaining high accuracy.

---
