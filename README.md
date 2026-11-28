# LangChain Projects

A collection of LangChain practice and production projects exploring LLM orchestration, agents, and generative AI.

## Projects Overview

- **`00_qna_bot`**: An interactive terminal-based Q&A chatbot powered by Groq (`ChatGroq`) and LangChain.
- **`01_blog_generator`**: An agentic blog content generation tool using LangChain and tools.
- **`02_Project_Search_weather _agent`**: An agent equipped with search and weather capabilities.
- **`03_Email_Agent`**: An automated email sending agent built with LangChain, LangGraph checkpointing, and SMTP tools.

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
