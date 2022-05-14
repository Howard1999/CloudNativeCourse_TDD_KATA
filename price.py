from collections import Counter

def price(books: list)-> float:
    result = Counter(books)

    n_diff = len(result)
    discount = 1.0

    if   n_diff == 2:
        discount = 0.95
    elif n_diff == 3:
        discount = 0.90
    elif n_diff == 4:
        discount = 0.80
    elif n_diff == 5:
        discount = 0.75
    
    return discount * len(books) * 8