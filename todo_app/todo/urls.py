from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, TaskDetailView
from .import views
urlpatterns= [
    path('task-list',TaskList.as_view(),name='task'),
    path('task-create',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('register/', RegisterPage.as_view(), name='register'),
    path('login/',views.login_fun,name='login'),
    path('register/', views.register_fun, name='register'),


]
