from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext,loader
from .models import Choice,Question
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

# def index(request):
#     '''latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     # context = RequestContext(request,{'latest_question_list':latest_question_list,})
#     # output = "，".join([p.question_text for p in latest_question_list])
#     # context = RequestContext(request, {
#     #     'latest_question_list': latest_question_list,
#     # })
#     return HttpResponse(template.render({'latest_question_list': latest_question_list,}))
# '''
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     content = {'latest_question_list':latest_question_list};
#     return render(request,'polls/index.html',content)

# def detail(request,question_id=0):
#     '''try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('question does not exist')
#     return render(request,'polls/detail.html',{'question':question})'''
#     content = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/detail.html',{'question':content})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request,question_id=0):
    p = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return HttpResponse('你好')
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    return HttpResponse('你好')


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'