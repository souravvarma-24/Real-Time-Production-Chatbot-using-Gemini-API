# 🚀 Real-Time Production Chatbot using Gemini API
---


**Innomatics Research Labs – Advanced Generative AI Internship**

This repository contains a **Production-Ready AI Career Strategy Chatbot** developed using **Google Gemini API and Streamlit**.

The application implements:

- Modular backend architecture  
- Advanced prompt engineering  
- Multi-turn conversation memory  
- Token-aware optimization  
- Logging and structured error handling  
- Clean UI rendering  

The system is designed to simulate a **real-world production-grade GenAI application architecture**.

---

## 🧩 Problem Statement

Develop a **Production-Ready Domain-Specific GenAI Chatbot** that:

- Integrates Google Gemini API  
- Uses secure API key management  
- Implements structured prompt engineering  
- Supports multi-turn contextual conversation  
- Follows clean backend architecture principles  
- Includes logging and fallback handling  
- Uses Streamlit for interactive UI  

The system must follow production-grade best practices.

---

## 📁 Project Structure

All submission files are organized as shown below:

```
career_strategy_ai/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── ai_coach_image.jpg
│
├── configuration/
│   └── environment.py
│
├── core/
│   ├── engine.py
│   ├── prompt_manager.py
│   ├── context_manager.py
│   └── logger.py
│
└── logs/
```

Each module has a dedicated responsibility to ensure clean architecture and separation of concerns.

---

## 🛠 Technologies Used

- Python  
- Streamlit  
- Google Gemini API  
- python-dotenv  
- Logging module  

---

## 🏗 System Architecture

The application follows clean architecture principles:

User  
→ UI Layer (Streamlit)  
→ Backend Layer (CareerAIEngine)  
→ Prompt Engineering Module (PromptManager)  
→ Gemini API  
→ Response Processing  
→ UI Rendering  

### Module Responsibilities

- **app.py** → UI rendering and user interaction  
- **engine.py** → API handling and response management  
- **prompt_manager.py** → Structured prompt building and token optimization  
- **context_manager.py** → Multi-turn conversation memory  
- **logger.py** → Logging API calls and errors  
- **environment.py** → Secure configuration management  

---

## ▶️ Application Workflow

1. User enters a career-related query.  
2. Conversation history is maintained in session memory.  
3. PromptManager builds a structured system prompt.  
4. Engine sends request to Gemini API.  
5. Response is processed and rendered in chat UI.  
6. Logs are recorded for monitoring and debugging.  
7. Token estimation ensures optimized prompt size.  

---

## ▶️ How to Run the Application

### Step 1 – Install Dependencies

pip install -r requirements.txt

### Step 2 – Create .env File

Create a `.env` file in the root folder:

GEMINI_API_KEY=your_api_key_here  
MODEL_NAME=gemini-1.5-flash  

### Step 3 – Run the Application

streamlit run app.py

Open in browser:

http://localhost:8501

---

## 📌 Features Implemented

- Secure Gemini API integration  
- Environment-based configuration  
- Structured system prompt engineering  
- Role-based domain-specific constraints  
- Multi-turn session memory  
- Token-aware context trimming  
- Logging of API calls and errors  
- Retry and fallback mechanism  
- Clean modular architecture  
- Professional Streamlit UI  

---

## 🧑‍🎓 Intern Details

| Field | Information |
|------|-------------|
| **Name** | Sourav Varma Gottumukkala |
| **Project** | Real-Time Production Chatbot using Gemini API |
| **Internship** | Advanced Generative AI Internship |
| **Organization** | Innomatics Research Labs |

---

## 🏁 Final Summary

This project demonstrates the development of a **production-grade AI chatbot system** using Google Gemini API. It implements modular backend architecture, structured prompt engineering, multi-turn conversation handling, token optimization, and clean UI rendering aligned with real-world deployment standards.

---

This completes Internship Assignment => Real-Time Production Chatbot using Gemini API successfully.

---

## ⭐ If this repository helped you, please leave a star.
