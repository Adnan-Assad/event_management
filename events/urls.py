from django.urls import path
from events.views import ( event_list ,category_list,category_create, category_update,category_delete, event_create, event_detail, event_update, event_delete, participant_list, participant_create, participant_update, participant_delete, dashboard)
 

urlpatterns = [
    
     path('event_list/', event_list, name="event_list"), 
     path('event_create/', event_create, name="event_create"),
     path('event_detail/<int:id>/', event_detail, name="event_detail"),
     path('event_update/<int:id>/', event_update, name="event_update"),
     path('event_delete/<int:id>/', event_delete, name="event_delete"),
     path('category_list/', category_list, name="category_list"),
     path('category_create/', category_create, name="category_create"),
     path('category_update/<int:id>/', category_update, name="category_update"),
     path('category_delete/<int:id>/', category_delete, name='category_delete'),
     path('participant_list/', participant_list, name="participant_list"),
     path('participant_create/', participant_create, name="participant_create"),
     path('participant_update/<int:id>', participant_update, name="participant_update"),
     path('participant_delete/<int:id>/', participant_delete, name="participant_delete"),
     path('dashboard/', dashboard, name="dashboard"),
]