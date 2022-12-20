from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('events/', views.eventspage, name='eventspage'),
    path('events/<int:event_id>', views.eventdetails, name='eventdetails'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
]
