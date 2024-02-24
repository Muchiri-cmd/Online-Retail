from django import forms
from main.models import ProductReview

class ReviewForm(forms.ModelForm):
    review=forms.CharField(max_length=100, required=False,widget=forms.Textarea(attrs={"placeholder":"Review product"}))

    class Meta:
        model=ProductReview
        fields=['review','rating']