🐳 Container App Session Pool — Safe Execution for LLM-Generated Code

This repository demonstrates how to run untrusted or AI-generated Python code safely using Azure Container Apps Session Pools and LangChain’s SessionsPythonREPLTool.

It isolates each code execution inside a secure, ephemeral sandbox — perfect for experimenting with LLM-generated code, automations, or dynamic agents.

🚀 Features

1. 🧠 Uses LangChain with Ollama for local LLM inference.

2. 🔒 Executes Python code in Azure Container Apps dynamic sessions — not on your local machine.

3. ⚡ Runs quickly thanks to pre-warmed session pools.

4. 🧰 Demonstrates both raw execution and agent-based approaches.

```🗂️ Project Structure
CONTAINER_APP_SESSION_POOL/
│
├── src/
│   ├── llm_generated_code.py     # Runs simple Python code in a sandbox
│   └── run_raw_code.py           # Example of invoking code directly
│
├── .env                          # Contains environment variables (see below)
├── pyproject.toml                # Project dependencies & metadata
├── README.md                     # You're here!
└── uv.lock                       # Dependency lock file
```
⚙️ Setup Instructions
1. Clone the Repository
```
git clone https://github.com/<your-username>/container_app_session_pool.git
cd container_app_session_pool
```
2. Create and Activate Virtual Environment
```
python -m venv .venv
source .venv/bin/activate  # on macOS/Linux
.venv\Scripts\activate     # on Windows
```

3. Install Dependencies
```
pip install -r requirements.txt
```


(or if you’re using uv
):

```
uv sync
```

4. Set Up Environment Variables

Create a .env file in the project root with:

```
POOL_MANAGEMENT_ENDPOINT=<your_azure_container_app_session_pool_endpoint>
```

You can find this endpoint in your Azure Container App Session Pool configuration.

🧩 Example 1 — Run Code Directly

File: src/run_raw_code.py

```
from langchain_azure_dynamic_sessions import SessionsPythonREPLTool
from dotenv import load_dotenv
import os

load_dotenv()
POOL_MANAGEMENT_ENDPOINT = os.getenv("POOL_MANAGEMENT_ENDPOINT")

tool = SessionsPythonREPLTool(pool_management_endpoint=POOL_MANAGEMENT_ENDPOINT)
result = tool.invoke("""
a = 5
b = 10
c = a + b
print(c)
""")
print("Code Output:", result)
```

Run it:

python src/run_raw_code.py


🧾 Output:

Code Output: 15

🤖 Example 2 — Using an LLM Agent (LangChain + Ollama)

File: src/llm_generated_code.py

```
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_azure_dynamic_sessions import SessionsPythonREPLTool
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os

load_dotenv()
POOL_MANAGEMENT_ENDPOINT = os.getenv("POOL_MANAGEMENT_ENDPOINT")

llm = ChatOllama(model="llama3.2:latest", temperature=0)
tool = SessionsPythonREPLTool(pool_management_endpoint=POOL_MANAGEMENT_ENDPOINT)

prompt = hub.pull("hwchase17/openai-functions-agent")
agent = create_tool_calling_agent(llm, [tool], prompt)

agent_executor = AgentExecutor(agent=agent, tools=[tool], verbose=True, handle_parsing_errors=True)

response = agent_executor.invoke({
    "input": "what is the sum of 5 + 10? Please calculate it using python code."
})
print(response)
```

This example shows how an LLM can automatically generate and execute code inside a sandboxed Azure environment.

🧱 Why Use Session Pools?

1. Each session runs in a secure, isolated container.

2. Prevents harmful or buggy code from affecting your local system.

3. Containers spin up instantly from a pre-warmed pool.

4. deal for LLM agents, plugin systems, and user-submitted code.

🧠 Learn More

Azure Container Apps Session Pools Documentation

LangChain Azure Dynamic Sessions

Ollama
 — run open models locally.