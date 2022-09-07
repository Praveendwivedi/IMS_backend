
from . import views
from django.urls import  re_path


urlpatterns=[
    re_path(r"^factory$",views.factoryApi),
    re_path(r"^factory/([0-9]+)$",views.factoryApi),

    re_path(r"^product$",views.productClass.as_view()),
    re_path(r"^product/([0-9]+)$",views.productClass.as_view()),
    re_path(r"^products$",views.productClass.as_view()),
    re_path(r"^products/detail$",views.productDetail.as_view()),
    re_path(r"^products/detail/([0-9]+)$",views.productDetail.as_view()),
    re_path(r"^product/savefile",views.SaveFile)
]