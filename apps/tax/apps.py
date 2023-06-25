from django.apps import AppConfig


class TaxConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    label = "tax"
    name = "apps.tax"

    @staticmethod
    def model_imports():
        import apps.tax.models  # noqa

    @staticmethod
    def signal_imports():
        pass

    def ready(self):
        self.model_imports()
        self.signal_imports()
