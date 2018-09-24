from django import forms

class RegistrationForm(forms.Form):

    choice_list = (
        ("E1","Event 1"),
        ("E2","Event 2"),
        ("E3","Event 3"),
        )

    name = forms.CharField(max_length=20)
    phone = forms.IntegerField(min_value=1000000000,max_value=9999999999,widget=forms.widgets.TextInput)
    email = forms.EmailField()
    college = forms.CharField(max_length=50)
    year = forms.IntegerField(min_value=1,max_value=4)
    event_selected = forms.ChoiceField(choices=choice_list)
    txn_id = forms.CharField(label="Transaction ID")
