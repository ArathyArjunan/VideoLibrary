from django.urls import path
from rest_framework.routers import DefaultRouter
from videoapp import views

router=DefaultRouter()

router.register('events', views.EventView,basename="events")
router.register('members',views.MemberView,basename="members")
router.register('sessions',views.SessionView,basename="sessions")
router.register('videos', views.VideoView,basename="videos")
router.register('videomember', views.VideoMemberView,basename="videomember")



urlpatterns = [
    
]+router.urls