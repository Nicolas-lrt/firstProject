from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse

from compte.models import Compte, CartLine
from produit.models import Produit


@login_required(login_url='login')
def accueilBoutique(request):
    produits = Produit.objects.all()
    return render(request, 'boutique/accueil.html', {'produits': produits})


@login_required(login_url='login')
def productDetail(request, pk):
    liste_produits = Produit.objects.all()
    produit = Produit.objects.get(id=pk)
    return render(request, 'boutique/productDetail.html', {'produits': liste_produits, 'produit': produit})


@login_required(login_url='login')
def addToCart(request, pk, qty):
    client = Compte.objects.get(user_id=request.user.id)
    if CartLine.objects.filter(product_id=pk, client_id=client.id).exists():
        cart_line = CartLine.objects.get(product_id=pk, client_id=client.id)
        cart_line.quantity += int(qty)
    else:
        cart_line = CartLine(product_id=pk, client_id=client.id, quantity=qty)
    cart_line.save()
    messages.add_message(request, messages.SUCCESS,
                         'Le produit a été correctement ajouté à votre panier. '
                         )
    if request.META.get('HTTP_REFERER'):
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(reverse('accueilBoutique'))


def cartPage(request, pk):
    # total = 0
    client = Compte.objects.filter(userId=pk)
    cart = CartLine.objects.filter(client=client)
    # for cart_line in cart:
    #     total += cart_line.total()

    return render(request, 'boutique/cart.html', {'cart': cart})
