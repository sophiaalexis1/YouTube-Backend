from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

class CommentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comment'

class ReplyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reply'