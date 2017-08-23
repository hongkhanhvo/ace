# layout/urls.py
from django.conf.urls import url
from layout import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^contact/$', views.ContactPageView.as_view()),
    url(r'^courses/$', views.CoursePageView.as_view()), # Add this /about/ route
]
