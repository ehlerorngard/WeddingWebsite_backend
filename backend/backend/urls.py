from django.contrib import admin
from django.urls import path, include            
from rest_framework import routers               
from wedding import views                       

router = routers.DefaultRouter()                 
router.register(r'invitees', views.InviteeView, basename='invitee')
router.register(r'rsvps', views.RsvpView, 'rsvp')
router.register(r'messages', views.MessageView, 'message')

urlpatterns = [
    path('admin/', admin.site.urls),         
    path('api/', include(router.urls)),
    # path('api/rsvps/<int:id>/', views.RsvpView), # <–– example without router...
    path('csrf/', views.csrf),
    path('ping/', views.ping),        
]