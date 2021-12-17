from django.urls import path
from tasks.views import TaskCreateView, TasksListView, TaskDetailView, TaskUserCreateView, TaskUserListView
from tasks.views import TaskUserDetailView, GroupOfUsersCreateView, GroupOfUsersListView, GroupOfUsersDetailView

app_name = 'task'
urlpatterns = [
    path('user/create/', TaskUserCreateView.as_view()),
    path('user/list/', TaskUserListView.as_view()),
    path('user/detail/<int:pk>/', TaskUserDetailView.as_view()),
    path('task/create/', TaskCreateView.as_view()),
    path('task/list/', TasksListView.as_view()),
    path('task/detail/<int:pk>/', TaskDetailView.as_view()),
    path('user_group/create/', GroupOfUsersCreateView.as_view()),
    path('user_group/list/', GroupOfUsersListView.as_view()),
    path('user_group/detail/<int:pk>/', GroupOfUsersDetailView.as_view()),
]