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
    ans = 0
    book_cnt = len(books)
    result = Counter(books)

    while book_cnt>0:
        n_diff = 0
        for ind in result:
            if result[ind]>0:
                n_diff += 1
                result[ind] -= 1
                book_cnt -= 1

        ans += 8 * n_diff * discount(n_diff)
    
    return ans