from django import forms


class BirthdayForm(forms.Form):
    first_name = forms.CharField(max_length=20, label='Имя')
    last_name = forms.CharField(
        required=False,
        label='Фамилия',
        help_text='Необязательное поле'
    )
    birthday = forms.DateField(
        label='День рождения',
        widget=forms.DateInput(attrs={'type': 'date'})
    )


"""description = forms.CharField(
        required=True,
        label='Описание',
        widget=forms.Textarea(attrs={'cols': '30', 'rows': '5'})
    )
    price = forms.IntegerField(
        required=True,
        help_text='Рекомендованная розничная цена',
        min_value=10,
        max_value=100
    )
"""
