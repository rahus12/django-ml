from django import forms
from .models import *

class AlphabetForm(forms.ModelForm):
	number = 0
	img = ''
	class Meta:
		model = Alphabet
		fields = ['Alphabet_img']
