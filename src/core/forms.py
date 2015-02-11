from django import forms
from django.core.exceptions import ValidationError

from core.models import Area


class AreaForm(forms.ModelForm):

	class Meta:
		model = Area


	
	