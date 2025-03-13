import google.generativeai as genai

# Configure the generative model
genai.configure(api_key="AIzaSyCDrIILhOuD6KWU6QWJS1AOocStpoOWEKo")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

prompt="""Suggest a single open-ended technical topic that can be used for a debate. The topic should be thought-provoking, have multiple perspectives, and be relevant to current trends in technology or computer science.
Only return the topic as a concise statement."""
response=model.generate_content(prompt)
topic=response.text
print(topic)

while True:
    print("Now write your response now:\n")
    userinput=input()
    
    if userinput=="exit":break
    prompt=f"""You are in a debate and need to respond to the following argument presented by your opponent. Analyze the response, find counterpoints, and provide a concise rebuttal. Your rebuttal should sound like an opponent's response in a debate, structured as a single paragraph. Keep it direct, challenging, and focused on highlighting weaknesses or alternative viewpoints.
Topic (A): {topic}
Argument (B): {userinput}
Please respond with a single-paragraph rebuttal."""
    response=model.generate_content(prompt)
    User1resp=response.text
    print(f"User1 response:\n {User1resp}")

    prompt=f"""You are in a debate and need to respond to the following argument presented by your opponent. Analyze the response, find counterpoints, and provide a concise rebuttal. Your rebuttal should sound like an opponent's response in a debate, structured as a single paragraph. Keep it direct, challenging, and focused on highlighting weaknesses or alternative viewpoints.
Topic (A): {topic}
Argument (B): {User1resp}
Please respond with a single-paragraph rebuttal."""
    response=model.generate_content(prompt)
    User2resp=response.text
    print(f"User2 response:\n {User2resp}")
