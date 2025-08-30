# from django import forms
# from .models import Expense

# class ExpenseForm(forms.ModelForm):
#     class Meta:
#         model = Expense
#         fields = ['title', 'amount', 'category', 'date', 'notes']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#         }
#         labels = {
#             'title': 'Expense Title',
#             'amount': 'Amount ($)',
#             'category': 'Category',
#             'date': 'Date',
#             'notes': 'Additional Notes (optional)',
#         }   

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Expense

# -------------------------------
# Expense Form
# -------------------------------
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'date', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg '
                         'focus:ring-2 focus:ring-teal-600 focus:outline-none',
                'placeholder': 'Enter expense title'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg '
                         'focus:ring-2 focus:ring-teal-600 focus:outline-none',
                'placeholder': 'Enter amount'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg '
                         'focus:ring-2 focus:ring-teal-600 focus:outline-none'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg '
                         'focus:ring-2 focus:ring-teal-600 focus:outline-none'
            }),
            'notes': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg '
                         'focus:ring-2 focus:ring-teal-600 focus:outline-none',
                'placeholder': 'Add notes (optional)'
            }),
        }

# -------------------------------
# Signup Form
# -------------------------------
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg '
                 'focus:ring-2 focus:ring-teal-600 focus:outline-none',
        'placeholder': 'Enter username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg '
                 'focus:ring-2 focus:ring-teal-600 focus:outline-none',
        'placeholder': 'Enter email address'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg '
                 'focus:ring-2 focus:ring-teal-600 focus:outline-none',
        'placeholder': 'Enter password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg '
                 'focus:ring-2 focus:ring-teal-600 focus:outline-none',
        'placeholder': 'Confirm password'
    }))

# -------------------------------
# Login Form
# -------------------------------
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg '
                 'focus:ring-2 focus:ring-teal-600 focus:outline-none',
        'placeholder': 'Enter username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg '
                 'focus:ring-2 focus:ring-teal-600 focus:outline-none',
        'placeholder': 'Enter password'
    }))
