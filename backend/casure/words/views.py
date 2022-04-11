from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.



from .models import Word


def index(request):
    latest_word_list = Word.objects.order_by('-created_at')[:5]
    context = {'latest_word_list':latest_word_list}
    return render(request, 'words/index.html',context)

def detail(request,word_id):
    word = get_object_or_404(Word, pk=word_id)
    
    return render(request,'words/detail.html',{'word':word})


def results(request, word_id):
    response = "You're looking at the results of word %s."
    return HttpResponse(response % word_id)



