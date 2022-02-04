from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..models import Question, Answer
from ..forms import AnswerForm


def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', 1)  # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {
        'question_list': page_obj
    }
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)  # id=question_id 로 해도 된다.
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {
        'question': question,
        'form': form,
    }
    return render(request, 'pybo/question_detail.html', context)
