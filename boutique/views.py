import stripe
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse, HttpResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from boutique.forms import payChoiceForm
from compte.models import Compte, CartLine
from produit.models import Produit


@login_required(login_url='login')
def accueilBoutique(request):
    produits = Produit.objects.all()
    qtyTotal = 0
    client = Compte.objects.filter(userId=request.user.id)
    if CartLine.objects.filter(client__in=client):
        cart = CartLine.objects.filter(client__in=client)
        for cart_line in cart:
            qtyTotal += cart_line.quantity

    return render(request, 'boutique/accueil.html', {'produits': produits, 'cartQty': qtyTotal})


@login_required(login_url='login')
def productDetail(request, pk):
    liste_produits = Produit.objects.all()
    produit = Produit.objects.get(nom=pk)
    qtyTotal = 0
    client = Compte.objects.filter(userId=request.user.id)
    if CartLine.objects.filter(client__in=client):
        cart = CartLine.objects.filter(client__in=client)
        for cart_line in cart:
            qtyTotal += cart_line.quantity
    return render(request, 'boutique/productDetail.html',
                  {'produits': liste_produits, 'produit': produit, 'cartQty': qtyTotal})


@login_required(login_url='login')
def addToCart(request, pk, qty):
    client = Compte.objects.get(user_id=request.user.id)
    if CartLine.objects.filter(product_id=pk, client_id=client.id).exists():
        cart_line = CartLine.objects.get(product_id=pk, client_id=client.id)
        cart_line.quantity += int(qty)
    else:
        cart_line = CartLine(product_id=pk, client_id=client.id, quantity=qty)
    cart_line.save()
    if request.META.get('HTTP_REFERER'):
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(reverse('accueilBoutique'))


@login_required(login_url='login')
def removeFromCart(request, pk):
    client = Compte.objects.get(user_id=request.user.id)
    cart_line = CartLine.objects.get(product_id=pk, client_id=client.id)
    cart_line.quantity -= 1
    if cart_line.quantity <= 0:
        cart_line.delete()
    else:
        cart_line.save()

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def clearCart(request):
    client = Compte.objects.get(userId=request.user.id)
    CartLine.objects.filter(client_id=client.id).delete()

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def clearCartLine(request, pk):
    CartLine.objects.get(id=pk).delete()

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def cartPage(request):
    total = 0
    qtyTotal = 0
    client = Compte.objects.filter(userId=request.user.id)
    cart = CartLine.objects.filter(client__in=client)
    for cart_line in cart:
        total += cart_line.total()
        qtyTotal += cart_line.quantity

    return render(request, 'boutique/cart.html', {'cart': cart, 'total': total, 'qtyTotal': qtyTotal})


@login_required(login_url='login')
def cartRecap(request):
    total = 0
    qtyTotal = 0
    client = Compte.objects.filter(userId=request.user.id)
    cart = CartLine.objects.filter(client__in=client)
    for cart_line in cart:
        total += cart_line.total()
        qtyTotal += cart_line.quantity
    form = payChoiceForm()
    if request.method == 'POST':
        form = payChoiceForm(request.POST)
        if form.is_valid():
            if request.POST.get('choiceForm') == "1":
                return redirect('stripePayment')
            else:
                return redirect('accueilBoutique')

    return render(request, 'boutique/cartRecap.html',
                  {'cart': cart, 'total': total, 'qtyTotal': qtyTotal, 'payForm': form})


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
        client = Compte.objects.filter(userId=request.user.id)
        cart = CartLine.objects.filter(client__in=client)
        lineItems = []
        for cartLine in cart:
            lineItems += {
                'name': str(cartLine.product.nom),
                'quantity': cartLine.quantity,
                'currency': 'eur',
                'amount': str(cartLine.product.prixReel * 10)
            }
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
                success_url=domain_url + 'boutique/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'boutique/cancelled/',
                payment_method_types=['card'],
                mode='payment',
                # line_items=lineItems
                line_items=[
                    {
                        'name': 'T-shirt',
                        'quantity': 1,
                        'currency': 'eur',
                        'amount': '2000',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class SuccessView(TemplateView):
    template_name = 'boutique/paySuccess.html'


class CancelledView(TemplateView):
    template_name = 'boutique/payCancelled.html'


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        #  run some custom code here
        clearCart(request)

    return HttpResponse(status=200)
