from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^chat1$', views.line_callback),

]