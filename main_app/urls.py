from django.urls import path
from . import views
from main_app.views import BoatList



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('boats/', views.boats_index, name='index'),
    path('boats/<int:boat_id>/',views.boats_detail, name='detail'),
    path("boats/cbv", views.BoatList.as_view(), name='boats_index' ),
    path('boats/create/', views.BoatCreate.as_view(), name='boats_create'),
    path('boats/<int:pk>/update/', views.BoatUpdate.as_view(), name='boats_update'),
    path('boats/<int:pk>/delete/', views.BoatDelete.as_view(), name='boats_delete'),
    path('boats/<int:boat_id>/add_gear/', views.add_gear, name='add_gear'),
      # associate a owner with a boat (M:M)
    path('boats/<int:boat_id>/assoc_owner/<int:owner_id>/', views.assoc_owner, name='assoc_owner'),
    # unassociate a owner and boat
    path('boats/<int:boat_id>/unassoc_owner/<int:owner_id>/', views.unassoc_owner, name='unassoc_owner'),
    path('owners/', views.OwnerList.as_view(), name='owners_index'),
    path('owners/<int:pk>/', views.OwnerDetail.as_view(), name='owners_detail'),
    path('owners/create/', views.OwnerCreate.as_view(), name='owners_create'),
    path('owners/<int:pk>/update/', views.OwnerUpdate.as_view(), name='owners_update'),
    path('owners/<int:pk>/delete/', views.OwnerDelete.as_view(), name='owners_delete'),
    
]