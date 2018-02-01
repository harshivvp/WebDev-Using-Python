from django.urls import path
from . import views
app_name = 'demsite'

urlpatterns = [
    # /demsite/
    path('', views.IndexView.as_view(), name='index'),

    #/demsite/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    #/demsite/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    #/demsite/5/vote/
    path('<int:question_id>/vote/',views.vote, name='vote'),

    # /demsite/home/
    path('home/', views.BaseTemplate.as_view(), name='home'),

]