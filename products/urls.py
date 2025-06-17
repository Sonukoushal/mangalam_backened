from django.urls import path
from .views import MenuListCreateView, MenuDetailView, CategoryListCreateView, CategoryDetailView, Productlistcreate, ProductDetailView


urlpatterns = [
    path("menu/",MenuListCreateView.as_view()), #as_view() hi object banata hai class ka aur method call karta hai 
    path("menu/<int:pk>/",MenuDetailView.as_view()),  #.as_view() ek inbuilt class method hai jo view class ka object banata hai

    path("category/", CategoryListCreateView.as_view()),  # 🔹 All/Create
    path("category/<int:pk>/", CategoryDetailView.as_view()),  # 🔹 Detail/Update/Delete

    path("sub/",Productlistcreate.as_view()),
    path("sub/<int:pk>", ProductDetailView.as_view()),
    
]
