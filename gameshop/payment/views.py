from django.shortcuts import render


def address(request):
    return render(request, 'payment/address.html')


def bank_card(request):
    return render(request, 'payment/bank_card.html')
