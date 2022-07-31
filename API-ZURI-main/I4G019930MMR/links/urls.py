from django.urls import path
from . import views 

app_name="link"

urlpatterns = [
    path("create/", views.PostCreateApi.as_view({'get': 'list'}), name="api_create"),
    path("update/<int:pk>", views.PostUpdateApi.as_view({'get': 'list'}), name="api_update"),
    path("delete/<int:pk>", views.PostDeleteApi.as_view({'get': 'list'}), name="api_delete"),
    path("", views.PostListApi.as_view({'get': 'list'}), name="api_list"),
]

