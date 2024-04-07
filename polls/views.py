from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question
from django.template import loader 
from django.db.models import F 
from django.urls import reverse

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
        print('question object>', question_object)
        # return HttpResponse(f'Question Number {question_id}: {question_object.question_text}')
        template = loader.get_template('polls/detail.html')
        context = {'question': question_object, 'name': 'Django Polls App'}
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        raise Http404('Question does not exist...')

def results(request, question_id):
    # get the question object
    question_object = get_object_or_404(Question, pk=question_id)
    # create a template
    template = loader.get_template('polls/results.html')
    # passing a dictionary to template
    context = {'question': question_object}
    return HttpResponse(template.render(context, request))


def vote(request, question_id):
    # get_object_or_404(Model, pk) ---> tries to give you an object based on key that you pass, if doesn't exist then 404
    question = get_object_or_404(Question, pk=question_id)
    print('vote request >>>', request.POST)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
       
       # Q3 - IPL - 2 votes
       # 2 users answering Q3 
       # 1st user will answer IPL - 3 votes 
       # 2nd user is answering -- total number of IPL votes 2 or 3?
       
        # method to avoid race condition, F is DJango class, which helps you get value directly from DB 
        selected_choice.votes = F('votes') + 1 
        selected_choice.save() # update choice object in db

        # since we're moving to result page, HttpResponseRedirect should be used
        # question id should be passed because result url needs that
        return HttpResponseRedirect(reverse('polls:result', args=(question_id,) ))
        
    except Exception as e:
        return HttpResponse(f'Faced an Exception while voting, {e}')
    
# {'csrfmiddlewaretoken': ['eK1K1wqPhKKUnc9P2PAtxP8f8XAfKgmdJDkC3A5hi3WJuFLdbmPiUsoZZNBRP3IG'], 'choice': ['3']}

# polls app 
# question - choice 
#

# polls app pages
# question page - displays a question 
# feed page - list of questions 
# results page - result of particular question
# vote page - question and options
# {%%}

# what's new ?

# choice 1 - 10%
# choice 2 - 20%
# IPL - 70%

