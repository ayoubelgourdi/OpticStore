def v_username(username):
    if username == "" or " " in username:
        return False
    return True


def v_password(password):
    if password == "" or " " in password or len(password) < 3:
        return False
    return True


def v_price(price):
    try:
        price = float(price)
        if price <= 0:
            return False
        return True
    except:
        return False


def v_quantity(quantity):
    try:
        quantity = int(quantity)
        if quantity < 1:
            return False
        return True
    except:
        return False