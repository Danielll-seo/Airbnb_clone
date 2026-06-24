from django.apps import AppConfig


class DirectMessagesConfig(AppConfig):
    default_auto_filed = "django.db.models.BigAutoField"
    verbose_name = "Direct Messages"
    name = "direct_messages"
