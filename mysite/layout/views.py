from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index2.html'

class AboutPageView(TemplateView):
    template_name = "about.html"

class CoursePageView(TemplateView):
    template_name = "courses.html"

class TinTucView(TemplateView):
    template_name = "tin-tuc-su-kien.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class IELTSPageView(TemplateView):
    template_name = "ielts.html"

class TOEICPageView(TemplateView):
    template_name = "toeic.html"

class VSTEPPageView(TemplateView):
    template_name = "vstep.html"

class GiaoTiepPageView(TemplateView):
    template_name = "giao-tiep.html"

class ThanhTichIeltsPageView(TemplateView):
    template_name = "thanh-tich-ielts.html"

class ThanhTichVstepPageView(TemplateView):
    template_name = "thanh-tich-vstep.html"

class ThanhTichToeicPageView(TemplateView):
    template_name = "thanh-tich-toeic.html"

class HinhAnhLopHocPageView(TemplateView):
    template_name = "hinh-anh-lop-hoc.html"
