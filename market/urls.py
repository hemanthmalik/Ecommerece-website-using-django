from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.index, name="marketHome"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contactus"),
    path("tracker/", views.tracker, name="tracker"),
    path("search/", views.search, name="search"),
    path("productview/<int:pId>", views.productview, name="productview"),
    path("checkout/", views.checkout, name="checkout"),
    url("testpage/", views.testpage, name="testpage"),
]