from django import forms
from Tender.models import USER, POST, APPLY

class userform(forms.ModelForm):
	class Meta:
		model = USER
		fields = "__all__"

class postform(forms.ModelForm):
	class Meta:
		model = POST
		fields = "__all__"

class applyform(forms.ModelForm):
	class Meta:
		model = APPLY
		fields = "__all__"