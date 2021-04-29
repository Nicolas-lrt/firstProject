import stripe
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView


@login_required(login_url='login')
def addProject(request):
    return render(request, 'projets/addProject.html')


def devenirPartenaire(request):
    porteur = 0
    for group in request.user.groups.all():
        if group.name == 'porteur-investisseur':
            porteur = 1
    return render(request, 'projets/devenir-partenaire.html', {'porteur': porteur})


def chartePage(request):
    porteur = 0
    for group in request.user.groups.all():
        if group.name == 'porteur-investisseur':
            porteur = 1
    return render(request, 'projets/charte.html', {'porteur': porteur})


def commentInvestir(request):
    porteur = 0
    for group in request.user.groups.all():
        if group.name == 'porteur-investisseur':
            porteur = 1
    return render(request, 'projets/comment-investir.html', {'porteur': porteur})


@login_required(login_url='login')
def pq_sabonner(request):
    porteur = 0
    for group in request.user.groups.all():
        if group.name == 'porteur-investisseur':
            porteur = 1
    return render(request, 'projets/pourquoi_s-abonner.html', {'porteur': porteur})


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://127.0.0.1:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'projets/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'projets/cancelled/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        # 'name': 'Abonnement Enea Club',
                        'price': 'price_1IlDxzKJZrz0NpKj0GhPkDvu',
                        'quantity': 1,
                        # 'currency': 'eur',
                        # 'amount': '70900',
                    }
                ]
            )

            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class SuccessView(TemplateView):
    template_name = 'projets/subPaySuccess.html'


class CancelledView(TemplateView):
    template_name = 'projets/subPayCancelled.html'


def newPartner(request):
    partnerGroup = Group.objects.get(name='porteur-investisseur')
    request.user.groups.add(partnerGroup)
    return redirect(request.META.get('HTTP_REFERER'))