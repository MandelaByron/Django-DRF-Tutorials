from rest_framework import serializers
from players.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Player
        
        fields = ("id", "name", "age","club" ,"market_value", "caps", "main_position","citizenship", "international_goals")