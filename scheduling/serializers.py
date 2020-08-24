from rest_framework import serializers
from .models import Scheduler


class SchedulingCallSerializers(serializers.ModelSerializer):

    class Meta:
        model = Scheduler
        fields = '__all__'