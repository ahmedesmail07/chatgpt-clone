from email import message
from urllib import response
from click import Choice, prompt
from django.http import JsonResponse
from django.shortcuts import render
import openai

openai_api_key = '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'
openai.api_key = openai_api_key


def askOpenAI(message):
    response = openai.ChatCompletion.create(

        model="gpt-3.5-turbo",
        prompt=message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
        messages=[
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "user", "content": "Who won the world series in 2020?"},
              {"role": "assistant",
                  "content": "The Los Angeles Dodgers won the World Series in 2020."},
              {"role": "user", "content": "Where was it played?"}
        ]

    )
    print(response)
    answer = response.choices[0].message['content'].strip()
    return answer


def chatBot(request):
    if request.method == "POST":
        message = request.POST.get('message')
        response = askOpenAI(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, "chatbot.html")
