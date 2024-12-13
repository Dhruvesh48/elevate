from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    """A view that renders the bag contents page."""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a product to the shopping bag with quantity and size (if applicable) """

    quantity = int(request.POST.get('quantity', 1))  # Default quantity is 1
    size = request.POST.get('product_size', None)  # Get size if provided, else None
    print(request.POST.get('product_size'))
    redirect_url = request.POST.get('redirect_url', '/')  # Default redirect to home

    # Retrieve the shopping bag from the session
    bag = request.session.get('bag', {})

    if size:  # If the product has a size selected
        if item_id in bag:
            if 'items_by_size' not in bag[item_id]:
                bag[item_id]['items_by_size'] = {}
            if size in bag[item_id]['items_by_size']:
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:  # If no size is selected
        if item_id in bag:
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    # Save the updated bag in the session
    request.session['bag'] = bag
    return redirect(redirect_url)
