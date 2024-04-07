from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader 

# Create your views here.
# request is sent by django automatically
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:10]
    # print('latest question list >>', latest_question_list)
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    template = loader.get_template('polls/index.html')
    context = {'question_list': latest_question_list, 'name': 'Django Polls App'}
    return HttpResponse(template.render(context, request))
    



def about(request):
    return HttpResponse('About Polls App...')

def detail(request, question_id):
    try:
        # get all questions and filter out using question id
        question_object = Question.objects.filter(id=question_id)[0]
        # print('question object>', question_object)
        # return HttpResponse(f'Question Number {question_id}: {question_object.question_text}')
        template = loader.get_template('polls/detail.html')
        context = {'question': question_object, 'name': 'Django Polls App'}
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        raise Http404('Question does not exist...')

def results(request, question_id):
    return HttpResponse(f'Results of Question Number {question_id}')


def vote(request, question_id):
    return HttpResponse(f"Vote of Question Number {question_id}")



# polls app 
# question - choice 
#

# polls app pages
# question page - displays a question 
# feed page - list of questions 
# results page - result of particular question
# vote page - question and options
# {%%}