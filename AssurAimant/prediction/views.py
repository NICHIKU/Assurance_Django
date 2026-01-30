from django.shortcuts import render
from django.views import View
from .service import get_model
from .forms import PredictionForm
import pandas as pd

# Create your views here.
class MakePredictionView(View):
    template_name = "prediction/make_prediction.html"

    model = get_model()

    def get(self, request):
        form = PredictionForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = PredictionForm(request.POST)

        if form.is_valid():
            age = form.cleaned_data['age']
            children = form.cleaned_data['children']
            smoker = form.cleaned_data['smoker']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            sex = form.cleaned_data['sex']
            region = form.cleaned_data['region']

            bmi = weight / (height / 100) ** 2

            data = pd.DataFrame({
                'age': [age],
                'children': [children],
                'smoker': [smoker],
                'bmi': [bmi],
                'sex': [sex],
                'region': [region]
            })

        result = self.model.predict(data)[0]

        return render(request, self.template_name, {
            'form': form,
            'result': round(result, 2)
        })