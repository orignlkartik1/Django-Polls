from django.views import View
from django.shortcuts import render
from .models import Question

class IndexView(View):
    template_name = 'polls/index.html'

    def get(self, request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, self.template_name, context)
