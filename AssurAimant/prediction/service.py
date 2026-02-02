import os
import joblib
from django.conf import settings

def get_model():
    MODEL_PATH = os.path.join(settings.BASE_DIR, 'prediction', 'resources', 'linear_model.joblib')
    return joblib.load(MODEL_PATH)