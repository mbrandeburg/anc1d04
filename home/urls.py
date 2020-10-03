from django.conf.urls import url
from . import views

## NOTE: When adding, define these guys as functions under `view.py` so they can be called via `views.<routeAdded>`
urlpatterns = [
    url(r'^$', views.index, name="index"),  
    # localhost:8000/home

    url(r'^about$', views.about, name="about"),
    # localhost:8000/about

    url(r'^contact$', views.contact, name="contact"),  
    # localhost:8000/contact

]