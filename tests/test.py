def calculate_discount(total_price, discount_percentage):
    discount_total = (discount_percentage * total_price) / 100
    return discount_total 

def calculate_total(products, discount=0):
    total = 0

    for product in products:
        total += product["price"]

    if discount > 0:
        discount_value = calculate_discount(total, discount)
        total -= discount_value
    
    return total

def test_calculate_total_with_empty_list():

    assert calculate_total([]) == 0
    print("Passed Test 1 😁")

def test_calculate_total_with_single_product():
    
    products = [
        {
            "name": "Notebook", "price": 5
        }
    ]

    assert calculate_total(products) == 5
    print("Passed Test 2 😁")

def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "Book", "price": 10
        },
        {
            "name": "Pen", "price": 2
        }
    ]

    assert calculate_total(products) == 12
    print("Passed Test 3 😁")

def test_calculate_total_with_discount():
    
    products = [
        {
            "name": "Book", "price": 5
        },
        {
            "name": "Pen", "price": 5
        }
    ]

    discount = 50
    assert calculate_total(products, discount) == 5
    print("Passed Test 4 😁")

def test_calculate_total_without_discount():

    products = [
        {
            "name": "Book", "price": 5
        },
        {
            "name": "Pen", "price": 5
        }
    ]

    assert calculate_total(products) == 10
    print("Passed Test 5 😁")

def test_calculate_discount_total():
    total_product = 20
    discount_total = 50

    assert calculate_discount(total_product, discount_total) == 10
    print("Passed Test 6 😁")

if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()
    test_calculate_total_with_discount()
    test_calculate_total_without_discount()
    test_calculate_discount_total()