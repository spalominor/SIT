from django.shortcuts import render

# Create your views here.
def billing(request):
    """
    Principal billing page view. Here we render the billing website page for
    the users.
    
    Args:
        request (HttpRequest): HTTP request
        
    Returns:
        HttpResponse: HTTP response
    """
    return render(request, 'billing/billing.html')