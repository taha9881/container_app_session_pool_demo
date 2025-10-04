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
print("Code Output: ",result)