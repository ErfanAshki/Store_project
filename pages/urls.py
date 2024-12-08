from django.urls import path

from .views import HomePageView, AboutUsPage

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about_us/', AboutUsPage.as_view(), name='about_us'),

]
