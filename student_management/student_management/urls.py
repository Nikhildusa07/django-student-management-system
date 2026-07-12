from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home),
    path("update/<int:id>/",views.update_student),
    path("delete/<int:id>/", views.delete_student),
]
