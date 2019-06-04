from django.contrib import admin
from django.urls import path, include            
from rest_framework import routers               
from wedding import views                       

router = routers.DefaultRouter()  
# These are routes to build on the 'api/' base (invoked futher below in "urlpatterns"):               
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