from collections import Counter


def price(books: list[int]) -> float:
    combination = get_combination(books)
    move_5_to_3(combination)

    return price_of_combination(combination)

def discount(n_diff: int)->float:
    return {
        0: 1.0, 1: 1.0,
        2: 0.95, 3: 0.90,
        4: 0.80, 5: 0.75
    }[n_diff]

def price_of_set(n) -> float:
    return 8 * n * discount(n)

def price_of_combination(combination: dict[int:int]) -> float:
    ans = 0
    for ind in combination:
        ans += price_of_set(ind) * combination[ind]
    return ans

# combination=> {n_books_set: count}
def get_combination(books: list[int]) -> dict[int:int]:
    combination = {cnt:0 for cnt in range(1, 6)}

    uni_books = set(books)
    while len(books) > 0:
        combination[len(uni_books)] += 1
        for book in uni_books:
            books.remove(book)
        uni_books = set(books)
    
    return combination

# make 3, 5 to 4, 4
def move_5_to_3(combination: dict[int:int]) -> None:
    min_35 = min(combination[3], combination[5])
    combination[3] -= min_35
    combination[5] -= min_35
    combination[4] += min_35 * 2
    return
