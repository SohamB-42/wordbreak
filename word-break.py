from mira_sdk import MiraClient, Flow
import sys

# Set the default encoding to utf-8
sys.stdout.reconfigure(encoding='utf-8')

# Initialize the client
client = MiraClient(config={"API_KEY": "sb-782f03d4e3be67f93857cba3af9fb129"})

version = "1.0.0"
input_data = {
    "word": ""
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@sohamb/word-break/{version}"
else:
    flow_name = "@sohamb/word-break"

result = client.flow.execute(flow_name, input_data)
print(result)