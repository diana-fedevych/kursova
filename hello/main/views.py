from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .markov_chain import MarkovChain
from .models import Texts

# Create your views here.
mc = MarkovChain()
# mc.add_file('main/text.txt') 


def index (request):
    texts = Texts.objects.all()
    return render(request, 'main/index.html', {'texts': texts})

def about (request):
    return render(request, 'main/about.html')

# def generate_text(request):
#     print(request.GET)
#     print(request.GET.get('title', ''))
#     # взяти з бд текст по тайтлу , створити новий mc, передати в нього текст 
#     # Генеруйте текст за допомогою Markov Chain
#     generated_text = " ".join(mc.generate_text(max_length=10))

#     # Поверніть згенерований текст у вигляді JSON
#     return JsonResponse({'generated_text': generated_text})


def generate_text(request):
    title = request.GET.get('title', '')
    max_length = int(request.GET.get('max_length', 10))  # Default to 10 if not provided
    print(title, max_length)

    # Fetch the text and generate response
    try:
        selected_text = Texts.objects.get(title=title).full_text
        mc.add_string(selected_text)
        generated_text = " ".join(mc.generate_text(max_length=max_length))
    except Texts.DoesNotExist:
        generated_text = "Error: Text not found"

    print(generated_text)
    return JsonResponse({'generated_text': generated_text})















# def generate_text(request):
#     title = request.GET.get('title', '')
#     print(title)
#     # try:
#     selected_text = Texts.objects.get(title=title).full_text
#     mc.add_string(selected_text)
#     generated_text = " ".join(mc.generate_text(max_length=10))
#     # except Texts.DoesNotExist:
#     #     generated_text = "Error: Text not found"
#     print(generated_text)
#     return JsonResponse({'generated_text': generated_text})
    















# def generate_text(request):
#     title = request.GET.get('title', '')
#     print(title)
#     print('hello')
#     selected_text = Texts.objects.get(title=title).full_text
#     mc.add_string(selected_text)

#     # Отримайте значення max_length з GET-параметрів
#     max_length = int(request.GET.get('max_length', 10))

#     generated_text = " ".join(mc.generate_text(max_length))
#     print(generated_text)
#     return JsonResponse({'generated_text': generated_text})
