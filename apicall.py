import json
import requests
import openai


headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNmUyNGJlNDEtNmU0My00MDVmLTlkZjgtYTc5OWFjYTFkMzA2IiwidHlwZSI6ImFwaV90b2tlbiJ9.HVnarl3h57V9e2AaqjU0id6XzWBXHIH3xrRa-x3FgBc"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hey tell me a joke...",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "hello"
}
response = requests.post(url, json=payload, headers=headers)

result = json.loads(response.text)
print(result['openai']['generated_text'])

def take(que):
    payload["text"]=que
    #print(payload)
    response = requests.post(url, json=payload, headers=headers)
    #print(response.text)
    result=json.loads(response.text)
    print(result['openai']['generated_text'])
take("How are you..")
