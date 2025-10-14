from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['MovieID','MovieTitle','Actor1Name','Actor2Name','DirectorName','MovieGenre','ReleaseYear']

    def clean_ReleaseYear(self):
        yr = self.cleaned_data['ReleaseYear']
        if yr < 1880 or yr > 2100:
            raise forms.ValidationError("Enter a valid year.")
        return yr
