from django.urls import path
from . import views

urlpatterns = [
    path('QR-Generator', views.QR_Generator , name="QRGen"),
    path('QR-Generator\<str:path>', views.QR_Generator , name="QRGen"),
    path('Making-QRCode', views.QR_Generator_Img , name="QRGenImg")
]
