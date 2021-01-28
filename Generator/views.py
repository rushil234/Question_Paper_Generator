from django.shortcuts import render
from django.http import HttpResponse
from .models import Mathematics
from django.template import loader


# Create your views here.
def index(request):
    try:
        question_list = Mathematics.objects.order_by('id')[0:5]
    except Mathematics.DoesNotExist:
        raise Http404("Question does not exist")

    template = loader.get_template('pages/activity.html')
    return render(request, 'pages/activity.html', {'question': question_list})

def paper(request):

    if request.method=='POST':
        x=request.POST
        a=open('c:\Desktop\Project\QuestionPaperGenerator\q.txt','w') 
        for i in x:
           a.write(i)
        a.close()
    template = loader.get_template('pages/paper.html')
    return render(request, 'pages/paper.html')
    
    

   
    
    

    