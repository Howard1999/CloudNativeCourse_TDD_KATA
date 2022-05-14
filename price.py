from collections import Counter


def price(books: list[int]) -> float:
    books = get_count_list(books)
    combination = get_combination(books)
    move_5_to_3(combination)
    ans = price_of_combination(combination)
    return ans

def discount(n_diff: int)->float:
    return {
        0: 1.0, 1: 1.0,
        2: 0.95, 3: 0.90,
        4: 0.80, 5: 0.75
    }[n_diff]

def price_of_set(set: list[int]) -> float:
    return 8 * sum(set) * discount(sum(set))

def price_of_combination(combination: list[list[int]]) -> float:
    ans = 0
    for set in combination:
        ans += price_of_set(set)
    return ans

def get_count_list(books: list[int]) -> list[int]:
    ans = [0] * 5
    books_count = Counter(books)
    for ind in books_count:
        ans[ind] = books_count[ind]
    return ans

def simply_took_a_set(books_count_list: list[int]) -> list[int]:
    took_out = [0]*5
    for ind, cnt in enumerate(books_count_list):
        if cnt > 0:
            took_out[ind] += 1
            books_count_list[ind] -= 1
    return took_out

def get_combination(books_count_list: list[int]) -> list[list[int]]:
    combination = []
    while sum(books_count_list) > 0:
        combination.append(simply_took_a_set(books_count_list))
    return combination

# compute how many (3, 5) group
def get_35_cnt(combination:list[list[int]]) -> int:
    cnt_3, cnt_5 = 0, 0

    for set in combination:
        n_diff = sum(set)
        if n_diff == 3:
            cnt_3 += 1
        if n_diff == 5: 
            cnt_5 += 1
    
    return min(cnt_3, cnt_5)

# make 3, 5 to 4, 4
def move_5_to_3(combination: list[list[int]]) -> list[list[int]]:
    cnt_35 = get_35_cnt(combination)
    cnt_3, cnt_5 = cnt_35, cnt_35

    for set in combination:
        cnt = sum(set)
        # because 3, 5 always can move to 4, 4
        # and price_of_set() only care about sum
        # so just move book:0
        if cnt_3 > 0 and cnt == 3:
            set[0] += 1
            cnt_3 -= 1
        if cnt_5 > 0 and cnt == 5:
            set[0] -= 1
            cnt_5 -= 1
        if cnt_3 == 0 and cnt_5 == 0:
            break
    
    return combination