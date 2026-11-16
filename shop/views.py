from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import RegistrationForm


def home(request):

    products = Product.objects.select_related('category').all()

    return render(request, 'shop/index.html', {
        'products': products,
    })


def product_list(request):
    """Страница коллекции (/products/)"""
    products = Product.objects.select_related('category').order_by('-created_at')
    categories = Category.objects.all()

    return render(request, 'shop/products.html', {
        'products': products,
        'categories': categories
    })


def register(request):
    """Функция регистрации пользователя"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Автоматический вход после регистрации
            from django.contrib.auth import login
            login(request, user)
            return redirect('home')  # Кидаем на главную
    else:
        form = RegistrationForm()

    return render(request, 'shop/reg.html', {'form': form})