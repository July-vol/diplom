from django import forms


class Contactform(forms.Form):
    name = forms.CharField(
        min_length=6,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя'}
        ))
    email = forms.EmailField(
        wdget=forms.EmailInput(
            attrs={'placeholder': 'E-mail'})
    )
    phone = forms.CharField(
        wdget=forms.TextInput(
            attrs={'placeholder': 'Телефон'})
    )
    message = forms.CharField(
        min_length=20,
        widget=forms.Textarea(
            attrs={'placeholder': 'Сообщение', 'cols': 30, 'rows': 9, 'class': 'col-md-9 contact-left'}
        )
    )
