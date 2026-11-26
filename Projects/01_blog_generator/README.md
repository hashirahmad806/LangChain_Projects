# AI Blog Post Generator

A small Streamlit application that turns a topic and a chosen writing tone into a polished, downloadable blog post. It uses LangChain prompt pipelines with a Groq-hosted language model.

## What the application does

The app in `app.py` accepts a blog topic and tone, then runs three steps:

1. **Outline** — asks the model for an opening line, four section headings, and five key points.
2. **Draft** — expands the outline into a Markdown blog post and applies the requested tone and human-style writing guidance.
3. **Polish** — edits the draft without changing its meaning, adds a title, and preserves Markdown formatting.

The final post appears in the page, can be downloaded as `final_post.txt`, and is also available in a collapsed raw-text panel. Streamlit spinners indicate which generation step is running.

## Requirements

- Python 3.10 or later
- A Groq API key
- The Python packages used by the application:

```powershell
python -m pip install streamlit langchain langchain-core langchain-groq python-dotenv
```

## Configuration

Set `GROQ_API_KEY` before starting the application. You can set it in the shell or create a `.env` file next to `app.py`:

```env
GROQ_API_KEY=your_groq_api_key
```

Keep the key private. Do not commit `.env` or publish its contents.

The model is selected by the `MODEL` constant in `app.py` (currently `openai/gpt-oss-20b`). Change that value to use another model supported by your Groq account.

## Run locally

From this directory, run:

```powershell
streamlit run app.py
```

Streamlit opens the app in a browser. Enter a topic, choose a tone, and select **Generate Blog Post**. The first run may take a little while because the app makes three model calls in sequence.

## Implementation overview

- `ChatPromptTemplate` defines separate instructions for outlining, drafting, and polishing.
- `ChatGroq` provides the shared language model.
- Each prompt, model call, and `StrOutputParser` are composed into a LangChain pipeline using `|`.
- The Streamlit UI gathers input, displays progress and the final Markdown, and provides a text download.
- The model and prompts are initialized when Streamlit runs the script; generation occurs when the button is selected.

The application currently displays only the polished post; the intermediate outline and draft are used internally. Agent and tool-related imports in `app.py` are not currently part of the generation workflow.

## Notes

Generated content can contain inaccurate or outdated claims. Review and fact-check it before publishing. The app requires an active internet connection and valid Groq credentials for generation.
