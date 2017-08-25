from django import forms


class SearchForm(forms.Form):
    phrase = forms.CharField(max_length=100)


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.PasswordInput()
    password2 = forms.PasswordInput()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.PasswordInput()


class AskingForm(forms.Form):
    title = forms.CharField(required=True, max_length=128)
    text = forms.TextInput()

    from hasker.apps.hasker_main.models import HaskerTag
    for tag in HaskerTag.objects.all():
        locals()[tag.tag] = forms.BooleanField(initial=False)
