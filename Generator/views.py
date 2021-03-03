from django.shortcuts import render
from django.http import HttpResponse
from .models import Mathematics
from django.template import loader
from .forms import questionFormResponse
import csv

# Create your views here.
def index(request):
    try:
        question_list = Mathematics.objects.order_by('id')[0:5]
    except Mathematics.DoesNotExist:
        raise Http404("Question does not exist")

    template = loader.get_template('pages/activity.html')
    return render(request, 'pages/activity.html', {'question': question_list})

def qp(request):
    
      if request.method == 'POST':
        form = questionFormResponse(request.POST)
        if form.is_valid():
            # process form data
            obj = Listing() #gets new object
            obj.question = form.cleaned_data['question_text']
            obj.answer = form.cleaned_data['answer']
            obj.marks = form.cleaned_data['marks']
            obj.difficultylevel = form.cleaned_data['difficulty_level']
        
            obj.save()
            return HttpResponseRedirect('/')
    #if request.method =='POST':
     # dict1 = request.POST
      #with open('question.csv','w') as csvfile :
       # wrt=csv.writer(csvfile)
        #for key,value in dict1.items():
         #   wrt.writerow([key,value])
      return render(request,'pages/activity.html', {'form': form})




   




    
    

   
    
    

    