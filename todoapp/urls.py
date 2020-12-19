from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import TodoBlockListView, TodoBlockDetailView, TodoBlockCreateView, TodoItemDetailView, TodoItemCreateView


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/token', obtain_auth_token, name='token'),

    path('todo/', TodoBlockListView.as_view(), name='todo'),
    path('todo/block/<int:pk>/', TodoBlockDetailView.as_view(), name='todo-block-detail'),
    path('todo/block/create/', TodoBlockCreateView.as_view(), name='todo-block-create'),

    path('todo/item/<int:pk>/', TodoItemDetailView.as_view(), name='todo-item-detail'),
    path('todo/item/create/', TodoItemCreateView.as_view(), name='todo-item-create'),
]
