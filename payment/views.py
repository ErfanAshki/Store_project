import requests, json
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse

from orders.models import Order


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    toman_total_price = order.get_total_price()
    rial_total_price = order.get_total_price() * 10

    zarinpal_request_url = 'https://payment.zarinpal.com/pg/v4/payment/request.json'

    request_header = {
        'accept': 'application/json',
        'content_type': 'application/json',
    }

    request_data = {
        'merchant_id': settings.MERCHANT_ID,
        'amount': rial_total_price,
        'description': f"{order.id} : {order.user.first_name} {order.user.last_name}",
        'callback_url': reverse('payment:payment_callback'),
    }

    res = requests.post(url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header)

    data = res.json()['data']
    authority = data['authority']
    order.authority = authority
    order.save()

    if 'errors' not in data or len(data['errors']) == 0:
        return redirect(f"https://payment.zarinpal.com/pg/StartPay/{authority}")
    else:
        return HttpResponse('Error from zarinpal')


def payment_callback(request):
    payment_authority = request.GET.get('authority')
    payment_status = request.GET.get('status')

    order = get_object_or_404(Order, authority=payment_authority)
    toman_total_price = order.get_total_price()
    rial_total_price = order.get_total_price() * 10

    if payment_status == 'OK':
        zarinpal_verify_url = 'https://payment.zarinpal.com/pg/v4/payment/verify.json'

        request_header = {
            'accept': 'application/json',
            'content_type': 'application/json',
        }

        request_data = {
            'merchant_id': settings.MERCHANT_ID,
            'amount': rial_total_price,
            'authority': payment_authority,
        }

        res = requests.post(url=zarinpal_verify_url, data=json.dumps(request_data), headers=request_header)

        if 'data' in res.json() and ('errors' not in res.json()['data'] or len(res.json()['data']['errors']) == 0):
            data = res.json()['data']
            payment_code = data['code']

            if payment_code == 100:
                order.is_paid = True
                order.ref_id = data['ref_id']
                order.zarinpal_data = data
                order.save()
                return HttpResponse('ok payment')

            elif payment_code == 101:
                return HttpResponse('already payment')

            else:
                error_code = res.json()['errors']['code']
                error_message = res.json()['errors']['message']
                return HttpResponse(f"{error_code}  {error_message} nok payment")
