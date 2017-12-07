from django.conf.urls import url
from FirstApp import views

urlpatterns = [

    url(r'^$',views.index,name='index'),

]