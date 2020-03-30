from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[
    path('home/', views.HomePageView.as_view(), name='home'),
    path('home/', views.home, name='home'),
    path('detail/<int:contact_id>/', views.detail, name='detail'),
    #path('search/', views.HomePageView.as_view(), name='HomePageView'),
    path('details/<int:pk>/', views.ContactDetailsView.as_view(), name='details'),
    #path('search/', views.SearchView.as_view(), name='SearchView')
    path('search/', views.search, name='search'),
    path('contacts/create/', views.ContactCreateViews.as_view(), name='create'),
    path('contacts/update/<int:pk>/', views.ContactUpdateViews.as_view(), name='update'),
    path('contacts/delete/<int:pk>/', views.ContactDeleteView.as_view(), name='delete'),
    path('signup/', views.SignUpView.as_view(), name='signup'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)