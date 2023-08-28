from django.urls import path, include
from cars import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.user_cars),
    path('all/', views.get_all_cars),
    path('comments/', views.user_comments),
    path('comments/replies', views.user_replies),
    path('comments/<str:video_id>', views.get_comments_for_video),
]
