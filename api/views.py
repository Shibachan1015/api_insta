from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from . import serializers
from .models import Profile, Post, Comment

class CreateUserView(generics.CreateAPIView):
    serializers_class = serializers.UserSerializer
    permission_classes = (AllowAny,)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializers_class = serializers.ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(userProfile=self.request.user)

class MyprofileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializers_class = serializers.ProfileSerializer
    def get_queryset(self):
        return self.queryset.filter(userProfile=self.request.user)

class PostviewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializers_class = serializers.ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(userPost=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializers_class = serializers.CommentSerializer

    def perform_create(self, serializer):
        serializer.save(userComment=self.request.user)
