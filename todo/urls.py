from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_page_view, name='todo-home'),
    path('update/<int:pk>', views.update_view, name='todo-home-up'),
    path('delete/<int:pk>', views.delete_view, name='todo-home-del'),

]
