from django import forms
class selection(forms.Form):
	input=forms.CharField(label='Enter a word with length less than 9',max_length=9,min_length=1)

