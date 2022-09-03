from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html' )

def count(request):

    return render(request, 'count.html')

def review(request):
    name = request.POST['name']
    message = request.POST['message']
    character = len(message)
    message_count = len(message.split())

    return render(request, 'review.html' ,{'message':message_count, 'name':name ,'character':character} )