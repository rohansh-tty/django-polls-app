from . import views
from django.urls import path

# 127.0.0.1:8000/polls/index


# specific to polls app
urlpatterns = [
    path("", views.index, name="index"),
    path('/about', views.about, name="about"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results", views.results, name="result"),
    path("<int:question_id>/vote", views.vote, name="vote")
    
    # value:question_id ---> send value as question_id to views.detail
  
]

# 127.0.0.1:8000/index

# is it visible???https://prod.liveshare.vsengsaas.visualstudio.com/join?8C2499867C66557BF60E5861A1EB0E7E70E8

