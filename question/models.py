from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    questionTitle = models.CharField(max_length=120)
    questionContent = models.CharField(max_length=300)
    #questionContent = forms.CharField(widget=forms.Textarea, max_length = 250)
    acceptanceStatus = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.questionTitle

    def get_absolute_url(self):
        return reverse('detail-question', kwargs={'pk': self.pk})


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answerContent = models.CharField(max_length=300)
    acceptanceStatus = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)

class QuestionComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    commentContent = models.CharField(max_length=300)
    createdDate = models.DateTimeField(default=timezone.now)

class AnswerComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    commentContent = models.CharField(max_length=300)
    createdDate = models.DateTimeField(default=timezone.now)

class AnswerPoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    Upvote = models.BooleanField(default=False)
    Downvote = models.BooleanField(default=False)
    acceptanceStatus = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)

class QuestionPoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Upvote = models.BooleanField(default=False)
    Downvote = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)

class TagDetails(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    TagName = models.CharField(max_length=25)
