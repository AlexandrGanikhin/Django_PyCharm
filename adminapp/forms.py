from django import forms

from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User
from mainapp.models import Product


class UserAdminRegisterForm(UserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfileForm):
    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False


class UserAdminCreateProductForm(forms.ModelForm):
    img = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserAdminCreateProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название продукта'
        self.fields['img'].widget.attrs['placeholder'] = 'Добавьте изображение продукта'
        self.fields['description'].widget.attrs['placeholder'] = 'Описание продукта'
        self.fields['short_description'].widget.attrs['placeholder'] = 'Короткое описание продукта'
        self.fields['price'].widget.attrs['placeholder'] = 'Цена'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Количество на складе'
        self.fields['category'].widget.attrs['placeholder'] = 'Категория'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['img'].widget.attrs['class'] = 'custom-file-input'
