from django.shortcuts import render



def home(request):
    """
    Principal home page view. Here we render the welcome website page for 
    the users.

    Args:
        request (HttpRequest): HTTP request

    Returns:
        HttpResponse: HTTP response
    """
    return render(request, 'home/home.html')