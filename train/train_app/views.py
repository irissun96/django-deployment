from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dic = {'insert_me': "Hello I'm from train_app/view.py"}
    return render(request, 'train_app/index.html', context = my_dic)
