from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse


def index(request):
    return HttpResponse("Как выбрать и как приготовить молодой картофель: советы от шефа!")

def my_post(request):
    data = {
        'вкусное блюдо': 'дранiчкi'
    }
    return JsonResponse(data)

def my_new_url(request, posts: int):
    if posts == 5:
        return redirect('/post/home')

def index_html(request):
    return render(request, "index_html.html")

def about(request):
    return render(request, "about.html")
