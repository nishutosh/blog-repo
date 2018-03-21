from django import forms

class RegisterForm(forms.Form):
	firstname=forms.CharField(max_length=50)
	lastname=forms.CharField(max_length=50)
	email=forms.EmailField()
	username=forms.CharField(max_length=50)
	password=forms.CharField(widget=forms.PasswordInput)
	confirm_password=forms.CharField(widget=forms.PasswordInput)
	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		password= cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")
		if password != confirm_password:
				raise forms.ValidationError(
					"Password and confirm Password fields does not match"
				)
