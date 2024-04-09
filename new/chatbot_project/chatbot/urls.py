from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_question, name='chat_question'),
    path('chat/<str:button_id>/', views.chat, name='chat'),
    # path('chat/<str:chat-input>/', views.chat, name='chat'),
]
