from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse

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
def clearCart(request, pk):
    client = Compte.objects.get(userId=pk)
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
                return cartPage(request)
            else:
                return redirect('accueilBoutique')

    return render(request, 'boutique/cartRecap.html', {'cart': cart, 'total': total, 'qtyTotal': qtyTotal, 'payForm': form})
