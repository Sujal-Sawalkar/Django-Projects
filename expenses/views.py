
# from django.shortcuts import render, redirect
# from .forms import ExpenseForm
# from django.contrib.auth.decorators import login_required

# @login_required
# def add_expense(request):
#     if request.method == "POST":
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             expense = form.save(commit=False)
#             expense.user = request.user  # link expense to logged-in user
#             expense.save()
#             return redirect('view_expenses')
#     else:
#         form = ExpenseForm()
#     return render(request, 'expenses/add_expense.html', {'form': form})

# def home(request):
#     return render(request, 'expenses/home.html')

# def login(request):
#     return render(request, 'expenses/login.html')

# def logout(request):
#     return render(request, 'expenses/logout.html')   

# # def add_expense(request):
# #     return render(request, 'expenses/add_expense.html')

# def view_expenses(request):
#     return render(request, 'expenses/view_expenses.html')

# def summary(request):
#     return render(request, 'expenses/summary.html')

# def sign_up(request):
#     return render(request, 'expenses/sign_up.html')





# from django.shortcuts import render, redirect
# from .forms import ExpenseForm
# from .models import Expense
# from django.contrib.auth.decorators import login_required, login
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.db.models import Sum

# from .forms import ExpenseForm, SignupForm, LoginForm
# from .models import Expense


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .forms import ExpenseForm, SignupForm, LoginForm
from .models import Expense

# ----------------- Add Expense -----------------
@login_required
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # link expense to logged-in user
            expense.save()
            return redirect('view_expenses')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

# ----------------- Dashboard -----------------
def home(request):
    return render(request, 'expenses/home.html')

# ----------------- View Expenses -----------------
@login_required
def view_expenses(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')  # latest first
    return render(request, 'expenses/view_expenses.html', {'expenses': expenses})

# ----------------- Summary -----------------
@login_required
def summary(request):
    # expenses = Expense.objects.filter(user=request.user)

    # category_summary = expenses.values('category').annotate(total=Sum('amount'))
    # total_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0

    # return render(request, 'expenses/summary.html', {
    #     'category_summary': category_summary,
    #     'total_expense': total_expense
    

    expenses = Expense.objects.all().order_by('-date')  # get all expenses
    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0  # sum of all amounts

    # If you also want category breakdown
    category_summary = expenses.values('category').annotate(total=Sum('amount'))

    return render(request, 'expenses/summary.html', {
        'expenses': expenses,
        'total_expenses': total_expenses,
        'category_summary': category_summary,
    })

# ----------------- Auth Pages -----------------
def sign_up(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # log in automatically after signup
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'expenses/sign_up.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')

def login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'expenses/login.html', {'form': form})
