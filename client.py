from openai import OpenAI

client = OpenAI(
    api_key="NA",  # your Perplexity API key
    base_url="https://api.perplexity.ai/"  # direct Perplexity endpoint
)

response = client.chat.completions.create(
    model="sonar-pro",  
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Vega, skilled like Alexa or Google Assistant."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(response.choices[0].message.content)