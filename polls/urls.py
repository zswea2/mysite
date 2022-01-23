from django.urls import path

from . import views

app_name = 'polls'  #이름명시
# urlpatterns = [
#     #ex : /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/',views.detail, name='detail'),  # question_id 는 viwe에있는 question_id랑 일치하여야 한다.
#     #ex : /polls/5/results/
#     path('<int:question_id>/results/',views.results, name='results'),
#     #ex : /polls/5/vote/
#     path('<int:question_id>/vote/',views.vote, name='vote'),
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),          #2~3번째 경로가 pk로 됨
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), #pk란 DB내의 하나의 열(하나의 데이터를)구분할수 있는 값
    path('<int:question_id>/vote/', views.vote, name='vote'),
]