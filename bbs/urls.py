from django.urls import path

from . import views
app_name = "bbs"
urlpatterns = [
    # path('', views.index, name='index'),
    path('index', views.QuestionListView.as_view(), name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/replay/', views.replay, name='replay'),
    # path('topic/', views.TopicCreateView.as_view(), name='topic'),
    # path('topic-update/', views.TopicUpdateView.as_view(), name='topic-update'),
    path('my_page/', views.my_page, name='my_page'),

    
]