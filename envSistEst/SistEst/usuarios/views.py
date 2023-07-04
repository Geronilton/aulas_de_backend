from django.shortcuts import render
from .forms import RegisterForms


# Create your views here.
def register_view(request):
    form = RegisterForms()
    return render(request, 'pages/register_view.html', {'form': form})