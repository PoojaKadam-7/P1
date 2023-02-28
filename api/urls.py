from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.views import StudentViewset

router=routers.DefaultRouter()
router.register(r'student',StudentViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),
]
