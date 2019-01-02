from django.shortcuts import render
from ..layaway.utils import get_pricing_data

def layaway(request):
    data = get_pricing_data('gold', 1)
    return render(request, 'layaway/details.html', {
        'gold_price': data['price'],
        'extend_price': data['extended_price'],
        'skip_fee': data['skip_fee'],
        'setup_fee': data['setup_fee'],
        'monthly_price': data['monthly_price'],
    })
