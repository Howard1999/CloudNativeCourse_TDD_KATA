from collections import Counter

def discount(n_diff):
    percentage = 1.0

    if   n_diff == 2:
        percentage = 0.95
    elif n_diff == 3:
        percentage = 0.90
    elif n_diff == 4:
        percentage = 0.80
    elif n_diff == 5:
        percentage = 0.75
        
    return percentage

def price(books: list)-> float:
    result = Counter(books)
    n_diff = len(result)
    
    return discount(n_diff) * len(books) * 8