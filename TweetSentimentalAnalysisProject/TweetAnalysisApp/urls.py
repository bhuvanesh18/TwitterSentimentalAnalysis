from django.urls import path
from . import views
from . import tweet_analysis
from . import hashtag_analysis
urlpatterns = [
    path('', views.web_content),
    path('analysis',tweet_analysis.main),
    path('hashtag_analysis',hashtag_analysis.main)
]