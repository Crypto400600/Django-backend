from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Choice, Question
from django.urls import reverse
def home(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/home.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/home.html', context)
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
def results(request, question_id):
    question = Question.objects.get(pk = question_id)
    return render(request, 'polls/results.html', {'question': question})
def vote(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
