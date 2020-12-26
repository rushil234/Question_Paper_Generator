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

    # output = ', '.join([q.question_text for q in question_list])
    # return HttpResponse(output)