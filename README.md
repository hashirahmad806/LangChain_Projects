# LangChain Projects

A collection of production-ready LangChain & LangGraph projects exploring LLM orchestration, agentic workflows, memory persistence, and tool integration using Groq LPU inference.

> 📖 **Comprehensive Documentation**: For a deep architectural breakdown, flowcharts, idea formulations, and capability comparisons, read [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md).

---

## Projects Overview

- **`00_qna_bot`**: An interactive terminal-based Q&A chatbot powered by Groq (`ChatGroq`) and LangChain.
- **`01_blog_generator`**: A 3-stage LCEL pipeline (Outline $\rightarrow$ Draft $\rightarrow$ Polish) enforcing anti-cliché human writing rules with a Streamlit interface.
- **`02_Project_Search_weather _agent`**: An autonomous research and meteorological agent with real-time web search and Open-Meteo weather lookups backed by LangGraph thread checkpointing.
- **`03_Email_Agent`**: A safe Human-In-The-Loop email assistant with slot-filling, draft approval safeguards, and automated Gmail SMTP delivery.

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/hashirahmad806/LangChain_Projects.git
cd LangChain_Projects
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Copy `.env.example` to `.env` and fill in your API keys:
```bash
cp .env.example .env
```

---

## Quick Start / Running Projects

```bash
# Project 00: Terminal Q&A Bot
python Projects/00_qna_bot/app.py

# Project 01: Blog Post Generator Web App
streamlit run Projects/01_blog_generator/app.py

# Project 02: Search & Weather Agent
cd "Projects/02_Project_Search_weather _agent"
streamlit run app.py

# Project 03: Email Assistant Agent
cd "Projects/03_Email_Agent"
streamlit run app.py
```
