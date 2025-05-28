# Stateless Chat Graph with Time Tool

A minimal LangGraph agent that replies to each user input.  
If the user asks “What time is it?”, it calls a tool that returns the current UTC time in ISO‑8601 format.

---

## Quickstart

1. **Clone the repository and enter the directory:**

    ```bash
    git clone git@github.com:closecodex/stateless-chat-agent.git
    cd stateless-chat-agent
    ```

2. **Set up the virtual environment and install dependencies:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    pip install -r requirements.txt
    ```

3. **(If using Ollama) Download the Llama 3 model:**

    ```bash
    ollama pull llama3
    ```

4. **Run the bot:**

    **Note:**  
    In some LangGraph versions, the CLI command `langgraph dev` may not be installed due to packaging issues.  
    If so, simply run:

    ```bash
    python app.py
    ```

    Example interaction:

    ```
    You: What time is it?
    Bot: Current UTC time is: 2025-05-27T19:37:35.834012Z
    ```

    Or, if the CLI is available:

    ```bash
    langgraph dev
    ```

