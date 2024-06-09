from rest_framework import routers

from api.viewsets.playersViewsets import PlayerListViewset, PlayerSearchViewset

routes = routers.SimpleRouter()

routes.register('players', PlayerListViewset, basename="Players")

routes.register('search', PlayerSearchViewset, basename='Search')

urlpatterns = routes.urls

#API URLConf
#localhost:8000/api/players
