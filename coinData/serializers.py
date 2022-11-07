from rest_framework import serializers
from .models import coinsSupportedCoinListModel

class coinsSupportedCoinListSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = coinsSupportedCoinListModel
        fields = "__all__"

    def get_label(self, obj):
        try:
            label = str(obj.name).upper()
        except:
            label = ""
        return label



class coinsDatetimeToUnixTimeSerializer(serializers.Serializer):
    datetime = serializers.DateField(required=True)

