from django.shortcuts import render
from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class AboutUsPage(generic.TemplateView):
    template_name = 'about_us.html'

