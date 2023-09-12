import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a rocket engineer and you everthing about rocket and astrophysics"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Rocket Engineer Deepak")

demo.launch(share=True) 