from rest_framework import serializers
from .models import LightModule

class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightModule
        # fields = ('id','module_name','module_ip','number_of_relays','number_of_relays_used','setting_each_light')
        fields = [
            'id',
            'module_name',
            'module_ip',
            'number_of_relays',
            'number_of_relays_used',
            'setting_each_light',
        ]