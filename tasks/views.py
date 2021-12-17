from rest_framework import generics
from tasks.serializers import TaskDetailSerializer, TaskListSerializer, GroupOfUsersSerializer
from tasks.models import TaskModel
from tasks.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication
from tasks.serializers import TaskUserSerializer, TaskUserListSerializer, TaskUserDetailSerializer
from django.contrib.auth.models import User, Group

# Create your views here.


class TaskUserCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TaskUserSerializer


class TaskUserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = TaskUserListSerializer


class TaskUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)
    queryset = User.objects.all()
    serializer_class = TaskUserDetailSerializer


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskDetailSerializer
    permission_classes = (IsAuthenticated,)


class TasksListView(generics.ListAPIView):
    serializer_class = TaskListSerializer
    queryset = TaskModel.objects.all()
    permission_classes = (IsAuthenticated,)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskDetailSerializer
    queryset = TaskModel.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


class GroupOfUsersCreateView(generics.CreateAPIView):
    serializer_class = GroupOfUsersSerializer
    permission_classes = (IsAdminUser,)


class GroupOfUsersListView(generics.ListAPIView):
    serializer_class = GroupOfUsersSerializer
    queryset = Group.objects.all()
    permission_classes = (IsAdminUser,)


class GroupOfUsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupOfUsersSerializer
    queryset = Group.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)


