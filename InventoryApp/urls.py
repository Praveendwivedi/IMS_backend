
from . import views
from django.urls import  re_path

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r"^factory$",views.factoryApi),
    re_path(r"^factory/([0-9]+)$",views.factoryApi),

    re_path(r"^product$",views.productApi),
    re_path(r"^product/([0-9]+)$",views.productApi),

    re_path(r"^product/savefile",views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)