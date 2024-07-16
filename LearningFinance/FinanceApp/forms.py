from django import forms


# Forms for loggin in & signing up


class UserLogin(forms.Form):

    email = forms.CharField(label="email", max_length=200)
    password = forms.CharField(label="password", max_length=200)


class UserSignUp(forms.Form):

    name = forms.CharField(label="name", max_length=200)
    email = forms.CharField(label="email", max_length=200)
    password = forms.CharField(label="password", max_length=200)
