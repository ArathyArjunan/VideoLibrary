from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from videoapp.models import Video,Member,Event,VideoMember,Session
from videoapp.serializers import VideoMemberSerializer,VideoSerializer,SessionSerializer,EventSerializer,MemberSerializer



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


class SessionView(ViewSet):

    def create(self,request,*args, **kwargs):
        serializer=SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        
        else:
            return Response(data=serializer.errors)
        

    def list(self,request,*args, **kwargs):
        qs=Session.objects.all()
        serializer=SessionSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def update(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Session.objects.get(id=id)
        serializer=SessionSerializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        
        else:
            return Response(data=serializer.errors)
        
    

    def retrieve(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Session.objects.get(id=id)
        serializer=SessionSerializer(qs)
        return Response(data=serializer.data)
    

    def delete(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        Session.objects.get(id=id).delete()
        return Response(data={"msg":"deleted"})


class VideoView(ModelViewSet):
    serializer_class=VideoSerializer
    queryset=Video.objects.all()

    def my_view(request):
     print(request.body)



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
    

class VideoMemberView(ViewSet):

    def create(self,request,*args, **kwargs):
        serializer=VideoMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        
        else:
            return Response(data=serializer.errors)
        

    def list(self,request,*args, **kwargs):
        qs=VideoMember.objects.all()
        serializer=EventSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def update(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=VideoMember.objects.get(id=id)
        serializer=VideoMemberSerializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        
        else:
            return Response(data=serializer.errors)
        
    

    def retrieve(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=VideoMember.objects.get(id=id)
        serializer=VideoMemberSerializer(qs)
        return Response(data=serializer.data)
    

    def delete(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        VideoMember.objects.get(id=id).delete()
        return Response(data={"msg":"deleted"})











