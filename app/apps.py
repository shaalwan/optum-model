from django.apps import AppConfig
import joblib
from django.conf import settings
import os


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    MODEL_FILE = os.path.join(settings.MODELS, "Model.joblib")
    model = joblib.load(MODEL_FILE)
