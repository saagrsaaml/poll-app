from django.urls import path

from . import views

# app_name = 'polls'
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5
#     path('<int:question_id>/', views.detail, name="question_detail"),
#     # ex: polls/5/results
#     path('<int:question_id>/results', views.results, name='question_results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='question_vote')
#
# ]

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5
    path('<int:pk>/', views.DetailView.as_view(), name="question_detail"),
    # ex: polls/5/results
    path('<int:pk>/results', views.ResultsView.as_view(), name='question_results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='question_vote')

]