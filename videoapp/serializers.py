
from rest_framework import serializers
from videoapp.models import Event, Member, Session, Video

class EventSerializer(serializers.ModelSerializer):
    is_active=serializers.CharField(read_only=True)
    class Meta:
        model = Event
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    is_active=serializers.CharField(read_only=True)

    class Meta:
        model = Member
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
     
    is_active=serializers.CharField(read_only=True)

    class Meta:
        model = Session
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'


