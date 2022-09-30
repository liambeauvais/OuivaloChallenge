from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests


def index(request, context=None):
    template = loader.get_template("index.html")
    message_sent = False
    if request.method == "POST":
        status = send_api(request)
        message_sent = True if status == 200 else False
    context = {"message": "Envoi réussi!!" if message_sent else "Problème à l'envoi "}
    return HttpResponse(template.render(context, request))


def send_api(request):
    url = "https://script.google.com/macros/s/AKfycby-TJmFFUFTfiNUbMoSIZx8LVtiskQ-bUt4xO6hmrU0XQpJS8IPUBow/exec"
    data = {'cle': 'CLE-TEST-IOT', 'donnees': {
        'id': request.POST['email'], 'date': request.POST['date'], 'urlRelais': request.POST['urlRelais'],
        'message': request.POST['message']
    }}
    api_message = requests.post(url, data=data)
    return api_message.status_code
