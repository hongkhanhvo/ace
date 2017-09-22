# layout/urls.py
from django.conf.urls import url
from layout import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^contact/$', views.ContactPageView.as_view()),
    url(r'^courses/$', views.CoursePageView.as_view()),
    url(r'^tin-tuc-su-kien/$', views.TinTucView.as_view()),
    url(r'^ielts/$', views.IELTSPageView.as_view()),
    url(r'^toeic/$', views.TOEICPageView.as_view()), # Add this /about/ route
    url(r'^vstep/$', views.VSTEPPageView.as_view()),
    url(r'^giao-tiep/$', views.GiaoTiepPageView.as_view()),
    url(r'^thanh-tich-ielts/$', views.ThanhTichIeltsPageView.as_view()),
    url(r'^thanh-tich-toeic/$', views.ThanhTichToeicPageView.as_view()),
    url(r'^thanh-tich-vstep/$', views.ThanhTichVstepPageView.as_view()),
    url(r'^hinh-anh-lop-hoc/$', views.HinhAnhLopHocPageView.as_view()),
]
