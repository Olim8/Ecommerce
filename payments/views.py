from django.shortcuts import render


def payment_success(request):
    return render(request, 'payments/payment_success.html', {})
