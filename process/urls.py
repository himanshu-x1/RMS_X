from django.contrib import admin
from django.urls import path

from process import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIdex,name='main_page'),
    path('registration/',views.registration,name='registration'),
    path('user_registration/',views.registration,name='user_registration'),
    #otp
    path('validate_otp/',views.validate_otp,name='validate_otp'),
    #conformation
    path('conformation/',views.conformation,name= 'conformation'),

    #otp -page
    path('user_otp/',views.user_OTP,name='user-otp')

]