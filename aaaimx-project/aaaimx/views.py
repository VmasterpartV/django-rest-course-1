from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import Group

from .serializers import GroupSerializer, UserSerializer, DivisionSerializer, UserInfoSerializer, UserCreateSerializer
from .models import User, Division
from .permissions import UserPermission

# Create your views here.

class GroupView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    http_method_names = ['get', 'post', 'patch', 'delete']

    permission_classes = (UserPermission,)

    filterset_fields = []
    search_fields = ['username', 'email']
    ordering_fileds = ['id', 'email', 'birthdate', 'username']
    ordering = ['-date_joined']
    
    def get_queryset(self):
        division = self.request.user.division
        return User.objects.filter(division=division)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserInfoSerializer
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    #def create(self, request, *args, **kwargs):
    #   division = request.user.division
    #    serializer = self.get_serializer(data=request.data)
    #    serializer.is_valid(raise_exception=True)
    #    serializer.save(division=division)
    #    headers = self.get_success_headers(serializer.data)
    #    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer