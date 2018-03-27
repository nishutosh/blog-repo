from django import forms

class RegisterForm(forms.Form):
	firstname=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
	lastname=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		password= cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")
		if password != confirm_password:
				raise forms.ValidationError(
					"Password and confirm Password fields does not match"
				)

class SignInForm(forms.Form):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class ContactForm(forms.Form):
	name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Name'}))
	email=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	body=forms.CharField(max_length=600,widget=forms.Textarea(attrs={'placeholder': 'Content'}))
	company=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Company  Name'}))
