from django.urls import path
from .views import QuestionListView, QuestionDetailView, QuestionCreateView, QuestionUpdateView, QuestionDeleteView
from . import views

urlpatterns = [
    # path('', views.home, name='question'),
    path('', QuestionListView.as_view(), name='question'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='detail-question'),
    path('question/new/', QuestionCreateView.as_view(), name='create-question'),
    path('question/<int:pk>/update/', QuestionUpdateView.as_view(), name='update-question'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='delete-question'),
]
