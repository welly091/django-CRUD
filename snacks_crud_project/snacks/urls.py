from django.urls import path
from .views import SnackListView, SnackDetailView, SnackCreateView, SnackDeleteView, SnackUpdateView

urlpatterns = [
    path("", SnackListView.as_view(), name="SnackListView"),
    path("<int:pk>/", SnackDetailView.as_view(), name="SnackDetailView"),
    path("create/", SnackCreateView.as_view(), name="SnackCreateView"),
    path("delete/<int:pk>/", SnackDeleteView.as_view(), name="SnackDeleteView"),
    path("update/<int:pk>/", SnackUpdateView.as_view(), name="SnackUpdateView"),
]