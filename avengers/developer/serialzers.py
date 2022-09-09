from rest_framework  import serializers
from .models import Developer
class DeveloperSerializers(serializers.ModelSerializer):
    class Meta :
        model=Developer
        fields = "__all__"