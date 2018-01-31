from audioop import reverse
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .models import Question,Choice
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):

    template_name = 'demsite/index.html'
    context_object_name = 'latest_question_name'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):

    model = Question
    template_name = 'demsite/detail.html'


class ResultsView(generic.DetailView):

    model = Question
    template_name = 'demsite/results.html'

def vote(request,question_id):

    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except(KeyError, ObjectDoesNotExist):
        return render(request,'demsite/detail.html',{
            'question':question,
            'error_message':'Select a choice, please.',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('demsite:results',args=(question.id,)))

# def index(request):
#
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     # output = ', '.join([q.question_text for q in lastest_question_list])
#     return render(request,'demsite/index.html',context)

# def detail(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'demsite/detail.html',{'question':question})
#
# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'demsite/results.html',{'question':question})
