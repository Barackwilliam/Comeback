from  django.urls import path
from . import views
# from .views import TrackVisitView,TrackActivityView,dashboard_view
from .views import TermsAndConditionsView,dashboard_view


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('explore_zanzibar/', views.explore_zanzibar, name='explore_zanzibar'),
    path('zanzibar/<int:pk>/', views.Zanzibar_Tour, name='Zanzibar_Tour'),
    path('terms-and-conditions/', TermsAndConditionsView.as_view(), name='terms_and_conditions'),
    
    path('serengeti_migration/', views.serengeti_migration, name='serengeti_migration'),
    path('serengeti/<int:pk>/', views.serengeti_Tour, name='serengeti_Tour'), 
    
    path('honeymoon_safaris/', views.honeymoon_safaris, name='honeymoon_safaris'),
    path('honeymoon/<int:pk>/', views.honeymoon_Tour, name='honeymoon_Tour'), 
      
    path('camping_safaris/', views.camping_safaris, name='camping_safaris'),
    path('camping/<int:pk>/', views.camping_Tour, name='camping_Tour'),
    # path('zanzibar/<int:pk>/', views.Zanzibar_Tour, name='zanzibar_detail'),


    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('Arusha_highlight/', views.Arusha_highlight, name='Arusha_highlight'),
    path('Bird_Watching/', views.Bird_Watching, name='Bird_Watching'),
    path('Cultural_Immersion/', views.Cultural_Immersion, name='Cultural_Immersion'),
    path('Culinary_Adventure/', views.Culinary_Adventure, name='Culinary_Adventure'),

    path("destinations/", views.destinations_list, name="destinations_list"),
    path("destinations/<int:pk>/", views.destination_detail, name="destination_detail"),
    
    path('Tanzania_Visa/', views.Tanzania_Visa, name='Tanzania_Visa'), 
    path('form/', views.form, name='form'), 
    path('fly_Tz/', views.fly_Tz, name='fly_Tz'), 
    path('Trip_list/', views.Trip_list, name='Trip_list'),
    path('tour_list/', views.tour_list, name='tour_list'),
    path('safari_list/', views.safari_list, name='safari_list'),
    path('tour_detail/<int:pk>/', views.tour_detail, name='tour_detail'),
    path('Trip_detail/<int:pk>/', views.Trip_detail, name='Trip_detail'),
    path('safari_detail/<int:pk>/', views.safari_detail, name='safari_detail'),
    path('questions', views.questions, name='questions'),
    path("booking/submit/", views.booking_form_view, name="booking_submit"),

    path("meru_climbing/", views.meru_climbing, name="meru_climbing"),
    path("Momela_route_3/", views.Momela_route_3, name="Momela_route_3"),
    path("Momela_route_4/", views.Momela_route_4, name="Momela_route_4"),



    # path("track-visit/", TrackVisitView.as_view(), name="track_visit"),
    # path("track-activity/", TrackActivityView.as_view(), name="track_activity"),
    path("dashboard/", dashboard_view, name="dashboard"),

]