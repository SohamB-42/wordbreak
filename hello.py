import os
from mira_sdk import MiraClient, Flow
import sys

# Set the default encoding to utf-8
sys.stdout.reconfigure(encoding='utf-8')

# Initialize the client with the API key from environment variable or default value
api_key = os.getenv("MIRA_API_KEY", "sb-782f03d4e3be67f93857cba3af9fb129")
client = MiraClient(config={"API_KEY": api_key})

def test_flow(flow_id, inputs):
    result = client.flow.execute(flow_id, inputs)
    return result

# Test code reviewer
code_sample = """
hello
"""
print("\nTesting word-break flow...")
result = test_flow("sohamb/word-break", {
    "word":"hello"
})
if result:
    print("\nThe Breakdown")
    print(result)