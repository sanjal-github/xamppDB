from django.urls import path
from . import views

urlpatterns = [
    path('userdb/',views.UserView,name="addrec"),
    path('showrecs/',views.showstud, name="dispall")
]