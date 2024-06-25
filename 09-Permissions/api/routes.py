from rest_framework import routers
from api.viewsets.usersViewsets import UserViewset, RegisterViewset, LoginView

from api.viewsets.playersViewsets import PlayerListViewset, PlayerSearchViewset

routes = routers.SimpleRouter()

routes.register('players', PlayerListViewset, basename="Players")

routes.register('search', PlayerSearchViewset, basename='Search')

#users/<public_id>/toggle_favorite
#users/<public_id>/list_favorites/

routes.register('users', UserViewset, basename="Users")

routes.register('auth/register', RegisterViewset, basename='Register')

routes.register('auth/login', LoginView, basename='Login')


urlpatterns = routes.urls

#API URLConf
#localhost:8000/api/players
