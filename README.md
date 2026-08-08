# 🤖 Employee Support AI

An AI-powered employee support assistant that simplifies common workplace operations through a conversational interface. The application enables employees to perform routine tasks such as password resets, leave management, ticket handling, employee profile retrieval, and company policy assistance from a single interface.

The project combines **Hybrid Intent Detection**, **LangGraph**, and **Retrieval-Augmented Generation (RAG)** to intelligently process employee requests. Routine operations are handled using predefined tools, while policy-related questions are answered using a RAG pipeline powered by **Google Gemini** and **FAISS**.

Built with a modular architecture, the application separates the user interface, workflow orchestration, business logic, and AI components, making it scalable, maintainable, and easy to extend with additional employee support services.

---

## ✨ Features

| Feature | Description |
| ------- | ----------- |
| 🔐 Password Reset | Generate a temporary password for employees. |
| 🔓 Account Unlock | Unlock employee accounts through the chatbot. |
| 📅 Leave Management | View leave balances and submit leave requests with persistent updates. |
| 👤 Employee Profile | Retrieve employee information including department, designation, manager, and location. |
| 🎫 Ticket Management | Create new support tickets and view existing tickets. |
| 📚 Policy Assistance | Answer company policy questions using Retrieval-Augmented Generation (RAG). |
| 🧠 Hybrid Intent Detection | Combines rule-based matching with Gemini LLM for accurate intent classification. |
| 🔄 LangGraph Workflow | Routes requests through modular workflow nodes for execution and response generation. |

---
## 🏗️ System Architecture

```mermaid
flowchart TD

    A[Employee] --> B[Streamlit Chat Interface]

    B --> C[LangGraph Workflow]

    C --> D[Hybrid Intent Detection]

    D -->|Rule-Based Match| E[Intent Router]
    D -.->|LLM Fallback| F[Gemini LLM]

    F --> E

    E --> G[Support Services]
    E --> H[RAG Pipeline]

    G --> I[Response Formatter]
    H --> I

    I --> J[User Response]
```

The Employee Support AI follows a modular architecture where every user request is processed through a LangGraph workflow. User queries are first analyzed using a hybrid intent detection strategy. Requests that match predefined patterns are handled directly, while paraphrased or unseen requests are forwarded to the Gemini LLM for intent classification. Once the intent is identified, the Intent Router directs the request either to the appropriate support service or to the RAG pipeline for policy-related queries. Finally, the Response Formatter converts the output into a user-friendly response that is displayed in the Streamlit chat interface.

---

---

## 🎯 Objectives

The primary objectives of this project are:

- Automate routine employee support operations through a conversational interface.
- Reduce manual HR and IT support effort for repetitive employee requests.
- Provide accurate and context-aware responses to company policy questions using RAG.
- Demonstrate the integration of LangGraph, Hybrid Intent Detection, and Large Language Models in a practical application.
- Build a modular and extensible architecture that can be expanded with additional employee support services.

---
