from django import forms
from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['review', 'rating', 'user', 'product']
        exclude = ('date',)

    def __init__(self, *args, **kwargs):
        super(ProductReviewForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['user'].required = False

        self.fields['product'].widget = forms.HiddenInput()
        self.fields['product'].required = False

        self.fields['review'].widget.attrs['style'] = 'width: 100%; height: 40%; border-radius: 8px;'
        self.fields['rating'].widget.attrs['style'] = 'width: 100px;'

    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.user = self.initial.get('user')
        instance.product = self.initial.get('product')

        if commit:
            instance.save()

        return instance
