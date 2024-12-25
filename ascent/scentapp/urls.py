from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
   path("", views.home, name="homePage"),
   path("about/", views.about, name="aboutPage"),
   path("contact/", views.contact, name="contactPage"),
   path("workshops/", views.workshops, name="Workshopspage"),
   path("detailItem/<id>", views.detailItems, name="detailItemPage"),
   path('reserve/', views.make_reservation, name='make_reservation'),
   path('TopNote/',views.TopNote,name='TopNote'),
   path('', views.home, name='home'),
   #path
   
 



]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)