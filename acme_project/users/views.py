from django.shortcuts import redirect


def birthday_create(request):
    if not request.user.is_authentificated:
        return redirect('login')
