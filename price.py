from collections import Counter

def discount(n_diff: int)->float:
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

def price_of_set(set: list[int]) -> float:
    return 8 * len(set) * discount(len(set))

def took_out_a_set(books: list[int]) -> tuple[list[int], list[int]]:
    remain, took_out = [], []

    result = Counter(books)
    for ind in result:
        if result[ind]>0:
            result[ind] -= 1
            took_out.append(ind)
            remain += [ind] * result[ind]

    return remain, took_out

def price(books: list[int]) -> float:
    ans = 0
    while len(books)>0:
        books, took_out = took_out_a_set(books)
        ans += price_of_set(took_out)
    
    return ans