def upload_location_main_image(instance, filename):
    return f"{instance.seller.id}/{filename}"


def upload_location(instance, filename):
    return f"{instance.product.seller.id}/{filename}"
