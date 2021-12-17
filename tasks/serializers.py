from rest_framework import serializers
from tasks.models import TaskModel
from django.contrib.auth.models import User, Group


class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class TaskUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'groups']


class TaskUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'is_staff', 'email', 'groups']


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id', 'task_title', 'task_text', 'task_author', 'users_performers', 'task_image']


class TaskDetailSerializer(serializers.ModelSerializer):
    task_author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TaskModel
        fields = ['task_title', 'task_text', 'task_author', 'users_performers', 'task_image']


class GroupOfUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
