from rest_framework import status, permissions, generics, viewsets
from .serializers import UserSerializer,TaskSerializer,CategorySerializer,ProfileSerializer
from rest_framework.response import Response
from .models import Task,Category, Profile
from django.contrib.auth.models import User
from .custompermissions import OwnerPermission


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

# ユーザー一覧
class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ログインしているユーザー情報の取得
class LoginUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    # ログインいしているユーザーを指定
    def get_object(self):
        return self.request.user

class ProfileViewSets(viewsets.ModelViewSet):
     serializer_class = ProfileSerializer
     queryset = Profile.objects.all()

     #ログインしているユーザーの情報を格納
     def perform_create(self, serializer):
         serializer.save(user_profile=self.request.user)

     #削除を許可しない
     def destroy(self, request, *args, **kwargs):
         response = {'message': 'DELETE method is not allowed'}
         return Response(response, status=status.HTTP_400_BAD_REQUEST)

    #一部更新を許可しない
     def partial_update(self, request, *args, **kwargs):
         response = {'message': 'PATCH method is not allowed'}
         return Response(response, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # 削除を許可しない
    def destroy(self, request, *args, **kwargs):
        response = {'message': 'DELETE method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # 一部更新を許可しない
    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # 更新を許可しない
    def update(self, request, *args, **kwargs):
        response = {'message': 'PUT method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class TaskViewSets(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, OwnerPermission, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # 一部更新を許可しない
    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
