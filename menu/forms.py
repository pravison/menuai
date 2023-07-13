from django import forms 
from . models import Menu , Category, BestServedAt

class NewMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'image', 'price', 'category', 'ingredients', 'overview', 'description', 'best_for', 'promotion', 'special')

        widgets ={
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'overview': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'best_for': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'promotion': forms.CheckboxInput(attrs={
            }),
            'special': forms.CheckboxInput(attrs={
            }),
        }

class MenuCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets ={
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),}

class BestServedForm(forms.ModelForm):
    class Meta:
        model = BestServedAt
        fields = '__all__'
        widgets ={
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),}

