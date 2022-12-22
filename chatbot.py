import openai

openai.api_key = "YOUR-API-KEY"

def chatbot(prompt):
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  message = completions.choices[0].text
  return message

while True:
  prompt = input("You: ")
  response = chatbot(prompt)
  print("Bot: ", response)
