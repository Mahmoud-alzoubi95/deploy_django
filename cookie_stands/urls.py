from django.urls import path
from .views import ThingList, ThingDetail

urlpatterns = [
    path("", ThingList.as_view(), name="CookieStand_list"),
    path("<int:pk>/", ThingDetail.as_view(), name="CookieStand_detail"),
]
