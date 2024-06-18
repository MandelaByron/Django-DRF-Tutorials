from rest_framework import viewsets, status
from rest_framework.response import Response
from users.models import User
from api.serializers.users import UserSerializer, RegisterSerializer


class UserViewset(viewsets.ModelViewSet):
    
    http_method_names = ['get', 'patch', "delete"]
    
    serializer_class = UserSerializer
    
    queryset =  User.objects.all()
    
    
    def get_object(self):
        user = User.objects.get_object_by_public_id(self.kwargs['pk'])
        
        return user



class RegisterViewset(viewsets.ViewSet):
    #list(), create(), retrieve(), update(), partial_update(),destroy()

    def create(self, request):
        
        serializer = RegisterSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response(
            
            {
                "user": serializer.data
            },
            
            status=status.HTTP_201_CREATED
            
            
        )

        
    
    















