import imp
import django
from django.shortcuts import get_object_or_404, render, get_list_or_404  #404에러 짧은 코드
from django.http import HttpResponse,Http404 , HttpResponseRedirect
from django.template import loader
from polls.models import Question, Choice
from django.urls import reverse
from django.views import generic

# def index(request): #클라이언트로부터 리퀘스트를 받아서 index뷰를 호출
#     # return HttpResponse("Hello, world. You're at the polls index.") #response 해준다
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # # output = ', '.join([q.question_text for q in latest_question_list])
#     # # return HttpResponse(output)
#     # template = loader.get_template('polls/index.html')
#     # context = {  #context 를 통해서 데이터를 전달
#     #     'latest_question_list' : latest_question_list,
#     # }
#     # return HttpResponse(template.render(context,request))

#     #render 사용
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list' : latest_question_list}
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     return HttpResponse("you're looking at question %s." %question_id)

# def results(request, question_id):
#     # response = "you're looking at the results of question %s."
#     # return HttpResponse(response % question_id)

#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  # pk값 : 템플릿에서 넘겨받은 값을 조회
    except (KeyError, Choice.DoesNotExist):
        # 선택된 선택지가 없을때 다시 detail페이지로 이동하게 함
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

# def detail(request,question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question' : question})
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/detail.html',{'question':question})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'