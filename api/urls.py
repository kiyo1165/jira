from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSets, ProfileViewSets, CategoryViewSets, CreateUserView, ListUserView, LoginUserView

router = routers.DefaultRouter()
router.register('tasks', TaskViewSets)
router.register('profile', ProfileViewSets)
router.register('category', CategoryViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', CreateUserView.as_view(),name='create'),
    path('users/', ListUserView.as_view(),name='users'),
    path('loginuser/', LoginUserView.as_view(),name='loginuser'),
]
