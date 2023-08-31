from django.shortcuts import render


def chatBot(request):
    return render(request, "chatbot.html")
