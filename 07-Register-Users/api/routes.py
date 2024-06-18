from rest_framework import routers
from api.viewsets.usersViewsets import UserViewset, RegisterViewset
from api.viewsets.playersViewsets import PlayerListViewset, PlayerSearchViewset

routes = routers.SimpleRouter()

routes.register('players', PlayerListViewset, basename="Players")

routes.register('search', PlayerSearchViewset, basename='Search')

routes.register('users', UserViewset, basename="Users")

routes.register('auth/register', RegisterViewset, basename='Register')

urlpatterns = routes.urls

#API URLConf
#localhost:8000/api/players
