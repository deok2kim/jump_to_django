from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {
        'question_list': question_list
    }
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)  # id=question_id 로 해도 된다.
    context = {
        'question': question
    }
    return render(request, 'pybo/question_detail.html', context)
