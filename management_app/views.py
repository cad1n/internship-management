from django.shortcuts import redirect


def redirect_to_angular(request):
    return redirect('http://localhost:4200/')
