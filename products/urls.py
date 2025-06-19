from django.urls import path
from .views import MenuListCreateView, MenuDetailView, CategoryListCreateView, CategoryDetailView, Productlistcreate, ProductDetailView


urlpatterns = [
    path("menu/",MenuListCreateView.as_view()), 
    path("menu/<int:pk>/",MenuDetailView.as_view()),  

    path("category/", CategoryListCreateView.as_view()),  
    path("category/<int:pk>/", CategoryDetailView.as_view()),  

    path("sub/",Productlistcreate.as_view()),
    path("sub/<int:pk>", ProductDetailView.as_view()),
    
]
