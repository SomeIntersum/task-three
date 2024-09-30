from django import forms

from travels.models import Travel, TravelImage


class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = ['title', 'description', 'location', 'cost', 'heritage_sites', 'recommended_places',
                  'convenience_rating', 'latitude', 'longitude', 'safety_rating', 'population_density_rating',
                  'vegetation_rating']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'latitude': forms.NumberInput(attrs={'step': 0.000001}),
            'longitude': forms.NumberInput(attrs={'step': 0.000001}),
        }
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'location': 'Местоположение',
            'cost': 'Стоимость путешествия',
            'heritage_sites': 'Места культурного наследия',
            'recommended_places': 'Рекомендуемые места для посещения',
            'convenience_rating': 'Оценка удобства передвижения',
            'latitude': 'Широта',
            'longitude': 'Долгота',
            'safety_rating': 'Оценка безопасности',
            'population_density_rating': 'Оценка населенности',
            'vegetation_rating': 'Оценка растительности',
        }


class TravelImageForm(forms.ModelForm):
    class Meta:
        model = TravelImage
        fields = ['image', 'caption']
