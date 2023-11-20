from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .markov_chain import MarkovChain

# Create your views here.
mc = MarkovChain()
mc.add_file('main/text.txt') 

def index (request):
    return render(request, 'main/index.html')

def about (request):
    return render(request, 'main/about.html')

def generate_text(request):
    # Генеруйте текст за допомогою Markov Chain
    generated_text = " ".join(mc.generate_text(max_length=10))

    # Поверніть згенерований текст у вигляді JSON
    return JsonResponse({'generated_text': generated_text})