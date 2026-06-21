from django import forms


class CheckoutForm(forms.Form):


    address = forms.CharField(

        max_length=200,

        widget=forms.Textarea

    )