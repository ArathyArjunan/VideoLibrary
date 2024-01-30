from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    event_name=models.CharField(max_length=200,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)


    def  __str__(self):
       return self.event_name
   


class Member(models.Model):
    member_name=models.CharField(max_length=200,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)


    def __str__(self) :
        return self.member_name
    


class Session(models.Model):
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    event_id=models.ForeignKey(Event,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)



class Video(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    subject=models.CharField(max_length=200)
    video_file=models.URLField()
    upload_date=models.DateTimeField()
    uploader=models.ForeignKey(User,on_delete=models.CASCADE)
    session_id=models.ForeignKey(Session,on_delete=models.CASCADE)
    event_id=models.ForeignKey(Event,on_delete=models.CASCADE)
    member_id=models.ManyToManyField(Member)

    def __str__(self) -> str:
        return self.title


