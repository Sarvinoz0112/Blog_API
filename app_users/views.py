from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app_posts.models import PostModel
from app_posts.serializers import PostSerializer

class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

