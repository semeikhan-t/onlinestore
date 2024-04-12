from django import forms
from django.core.exceptions import ValidationError
import datetime
import re

from payment.models import PaymentData


def true_expiry_date(given_date):
    year_now = str(datetime.datetime.now().year)
    month_now = str(datetime.datetime.now().month)

    if int(given_date[3:]) < int(year_now[2:]):
        return False
    elif int(given_date[0:2]) > 12 or int(given_date[0:2]) < 1:
        return False
    elif int(given_date[0:2]) < int(month_now) and int(given_date[3:]) == int(year_now[2:]):
        return False
    else:
        return True


def is_valid_credit_card(card_number):
    # Удаляем все нецифровые символы из номера карты
    card_number = re.sub(r'\D', '', card_number)

    # Проверяем, что номер карты состоит из 16 цифр
    if not re.match(r'^\d{16}$', card_number):
        return False

    # Проверка по алгоритму Луна (Luhn algorithm) для валидации номера карты
    total_sum = 0
    reverse_digits = card_number[::-1]

    for i, digit in enumerate(reverse_digits):
        digit = int(digit)

        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9

        total_sum += digit

    return total_sum % 10 == 0


def is_valid_cardholder_name(name):
    # Имя может содержать только заглавные буквы, пробелы и дефисы
    # Имя также не должно начинаться или заканчиваться пробелом, или дефисом
    pattern = re.compile(r'^[A-Z]+([- ]?[A-Z]+)*$')

    return bool(pattern.match(name))


class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentData
        exclude = ('time_payment',)

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['city'].widget.attrs['placeholder'] = 'Название города'
        self.fields['full_address'].widget.attrs['placeholder'] = 'Район, улица/микрорайон, дом, квартира'
        self.fields['post_index'].widget.attrs['placeholder'] = '00000'
        self.fields['post_index'].widget.attrs['style'] = 'width: 62px;'
        self.fields['country'].widget.attrs['placeholder'] = 'Название страны'
        self.fields['card_number'].widget.attrs['placeholder'] = '0000 0000 0000 0000'
        self.fields['card_number'].widget.attrs['style'] = 'width: 186px;'
        self.fields['expiry_date'].widget.attrs['placeholder'] = '00/00'
        self.fields['expiry_date'].widget.attrs['style'] = 'width: 60px;'
        self.fields['cvv'].widget.attrs['placeholder'] = '000'
        self.fields['cvv'].widget.attrs['style'] = 'width: 42px;'
        self.fields['cardholder_name'].widget.attrs['placeholder'] = 'ALEKSANDR ALEKSANDROV'
        self.fields['cardholder_name'].widget.attrs['style'] = 'width: 238px;'
        self.fields['full_address'].widget.attrs['style'] = 'width: 300px;'
        self.fields['cart'].widget = forms.HiddenInput()
        self.fields['cart'].required = False
        self.fields['total_price'].widget = forms.HiddenInput()
        self.fields['total_price'].required = False
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['user'].required = False

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Здесь получаем значение из куки и устанавливаем его в поле 'cart'
        cart_value = self.initial.get('cart_from_cookie')
        total_price = self.initial.get('total_price')
        user = self.initial.get('user')

        instance.cart = cart_value
        instance.total_price = total_price
        instance.user = user

        if commit:
            instance.save()

        return instance

    def clean_post_index(self):
        post_index = self.cleaned_data['post_index']
        if post_index.isdigit() is False or len(post_index) < 5:
            raise ValidationError('Почтовый индекс должен состоять из 5 цифр!')
        return post_index

    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']
        if is_valid_credit_card(card_number) is False:
            raise ValidationError('Убедитесь что вы правильно ввели номер карты!')
        else:
            return card_number

    def clean_expiry_date(self):
        expiry_date = self.cleaned_data['expiry_date']
        if ('/' not in expiry_date or expiry_date[2] != '/') or (expiry_date[0:2].isdigit() is False or expiry_date[3:-1].isdigit is False):
            raise ValidationError("В поле даты истечения срока знак '/' должен прописываться в виде '00/00' !")
        elif true_expiry_date(expiry_date) is False:
            raise ValidationError("Срок годности вашей карты истек!")
        return expiry_date

    def clean_cvv(self):
        cvv = self.cleaned_data['cvv']
        if len(cvv) < 3 or not cvv.isdigit():
            raise ValidationError('CVV должен состоять из трех цифр!')
        return cvv

    def clean_cardholder_name(self):
        name = self.cleaned_data['cardholder_name']
        if is_valid_cardholder_name(name) is False:
            raise ValidationError('Убедитесь что вы правильно ввели имя, оно должно состоять только из заглавных букв!')
        return name
