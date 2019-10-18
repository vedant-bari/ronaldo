from django.apps import AppConfig


class TaskappConfig(AppConfig):
    name = 'taskapp'
    verbose_name = "taskapp details"


    def ready(self):
        import taskapp.signals
