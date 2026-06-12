from django import forms

class ProductForm(forms.Form):

    name = forms.CharField(max_length=200)

    description = forms.CharField(
        widget=forms.Textarea
    )

    price = forms.FloatField()

    stock = forms.IntegerField()

    image = forms.ImageField(
        required=False
    )

    featured = forms.BooleanField(
        required=False
    )