import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "inputs": "Question:write the caption araffe cat wearing sunglasses laying on a sandy beach? \nAnswer: ",
})
print(output[0]['generated_text'])