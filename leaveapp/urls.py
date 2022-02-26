from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('leave/', views.fetch_all_leaves, name="leaves"),
    path('leave/<int:id>/', views.fetch_leave_details, name="leave-details")
]