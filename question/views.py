from django.shortcuts import render
from django.http import HttpResponse
from .models import Question , QuestionComment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    questions = Question.objects.all()
    return render(request, 'question/home.html', { 'questions': questions } )

class QuestionListView(ListView):
    model = Question
    template_name = 'question/home.html'
    context_object_name = 'questions'
    ordering = ['-createdDate']


class QuestionDetailView(DetailView):
    model = Question

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['questionTitle', 'questionContent']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['questionTitle', 'questionContent']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        return False

class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = '/'

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        return False

def comment(request):
    questions = Question.objects.all()
    return render(request, 'question/home.html', { 'questions': questions} )
