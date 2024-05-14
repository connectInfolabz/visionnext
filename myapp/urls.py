from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('index.html', views.index, name='index.html'),
    path('about.html', views.about, name='about.html'),
    path('blog.html', views.blog, name='blog.html'),
    path('blog-single.html', views.blog_single, name='blog_single.html'),
    path('cases.html', views.cases, name='cases.html'),
    path('contact.html', views.contact, name='contact.html'),
    path('main.html', views.main, name='main.html'),
    path('services.html', views.services, name='services.html'),
    path('Service.html', views.service, name="service"),
    path("contactus", views.contactus, name="contactus"),
    path("login.html", views.loginpage, name="loginpage"),
    path("signup.html", views.signuppage, name="signuppage"),
    path("registeruser", views.registeruser, name="registeruser"),
    path("verifyuser", views.verifyuser, name="verifyuser"),
    path("logout", views.logout, name="logout"),
    path("storefeedback", views.storefeedback, name="storefeedback"),
    path("feedback.html", views.feedbakcpage, name="feedbakcpage"),
    path("serviceDetails.html", views.serviceDetails, name="serviceDetails.html"),
    path("forgotpassword.html", views.forgotpwdpage, name="forgotpassword.html"),
    path("forgotpwd", views.forgotpwd, name="forgotpwd"),
    path("profile.html", views.profile, name="profile.html"),
    path("storeInquiry", views.storeInquiry, name="storeInquiry"),
    path("courceCategories.html", views.courcesCategoriesPage, name="courceCategories.html"),
    path("cources.html", views.cources, name="cources.html"),
    path("courceDetails.html", views.courceDetails, name="courceDetails.html"),
    path("storeCourceInquiry", views.storeCourceInquiry, name="storeCourceInquiry")
]

