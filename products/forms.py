from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'border rounded border-green-600 m-auto my-2'
            visible.field.widget.attrs['placeholder']= visible.field.label

    class Meta:
        model = Product
        fields = [
                'title',
                'price',
                'description',
                ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')

        if not "plant" in title.lower().strip():
            raise forms.ValidationError("This is not a valid title")

        return title
