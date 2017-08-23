from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = "about.html"

class CoursePageView(TemplateView):
    template_name = "courses.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"
