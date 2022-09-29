from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    context = {"message" : ""}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))
