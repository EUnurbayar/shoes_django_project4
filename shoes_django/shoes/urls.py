from django.urls import path
from . import views

urlpatterns = [
    path('shoes/', views.ShoeList.as_view(), name="shoe_list"),
    path('shoes/<int:pk>', views.ShoeDetail.as_view(), name="shoe_detail"),
]