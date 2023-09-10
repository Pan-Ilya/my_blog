from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('post/<slug:url_name>/', ShowPost.as_view(), name='post')
]
