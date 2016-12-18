from django.conf.urls import url, include

urlpatterns = [
    url(r'^chatbot/', include('chatbot.urls')),
]