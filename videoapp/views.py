from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from videoapp.models import Video,Member,Event,Session
from videoapp.serializers import VideoSerializer,SessionSerializer,EventSerializer,MemberSerializer



class EventView(ViewSet):

    def create(self,request,*args, **kwargs):
        serializer=EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        
        else:
            return Response(data=serializer.errors)
        

    def list(self,request,*args, **kwargs):
        qs=Event.objects.all()
        serializer=EventSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def update(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Event.objects.get(id=id)
        serializer=EventSerializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        
        else:
            return Response(data=serializer.errors)
        
    

    def retrieve(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Event.objects.get(id=id)
        serializer=EventSerializer(qs)
        return Response(data=serializer.data)
    

    def delete(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        Event.objects.get(id=id).delete()
        return Response(data={"msg":"deleted"})


class SessionView(ModelViewSet):
    serializer_class=SessionSerializer
    queryset=Session.objects.all()
        
    @action(methods=["get"],detail=True)
    def video_by_session(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Video.objects.get(session_id=id)
        serializer=VideoSerializer(qs)
        return Response(data=serializer.data)

  

class VideoView(ModelViewSet):
    serializer_class=VideoSerializer
    queryset=Video.objects.all()

    @action(methods=["get"],detail=True)
    def members(self, request, pk=None):
        video = self.get_object()  
        members = video.member_id.all()  
        serializer = MemberSerializer(members, many=True) 
        return Response(serializer.data)




class MemberView(ViewSet):

    def create(self,request,*args, **kwargs):
        serializer=MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        
        else:
            return Response(data=serializer.errors)
        

    def list(self,request,*args, **kwargs):
        qs=Member.objects.all()
        serializer=MemberSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def update(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Member.objects.get(id=id)
        serializer=MemberSerializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        
        else:
            return Response(data=serializer.errors)
        
    

    def retrieve(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Member.objects.get(id=id)
        serializer=Member(qs)
        return Response(data=serializer.data)
    

    def delete(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        Member.objects.get(id=id).delete()
        return Response(data={"msg":"deleted"})
    












