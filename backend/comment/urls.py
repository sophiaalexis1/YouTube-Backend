from django.urls import path, include
from comment import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('comments/', views.user_comments),
    path('comments/replies', views.user_replies),
    path('comments/<str:video_id>', views.get_comments_for_video),
]
