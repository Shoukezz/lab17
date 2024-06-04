import itertools
import math

def number_generator(numbers):
    for number in numbers:
        yield number

def even_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

def odd_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num

def fibonacci_generator():
    a, b = 2, 3
    while True:
        yield a
        a, b = b, a + b

def prime_number_generator(limit):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(root):
    if root:
        yield root.value
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)

def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.value
        yield from in_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.value

def dfs_traversal(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            yield node
            visited.add(node)
            stack.extend(reversed(graph[node]))

def bfs_traversal(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            yield node
            visited.add(node)
            queue.extend(graph[node])


def dict_keys_generator(d):
    for key in d.keys():
        yield key


def dict_values_generator(d):
    for value in d.values():
        yield value


def dict_items_generator(d):
    for item in d.items():
        yield item


def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word


def string_chars_generator(s):
    for char in s:
        yield char


def unique_elements_generator(lst):
    seen = set()
    for elem in lst:
        if elem not in seen:
            seen.add(elem)
            yield elem


def reverse_list_generator(lst):
    for elem in reversed(lst):
        yield elem


def cartesian_product_generator(lst1, lst2):
    for elem1 in lst1:
        for elem2 in lst2:
            yield (elem1, elem2)


def permutations_generator(lst):
    for perm in itertools.permutations(lst):
        yield perm


def combinations_generator(lst):
    for r in range(1, len(lst) + 1):
        for comb in itertools.combinations(lst, r):
            yield comb


def tuple_list_generator(lst):
    for tup in lst:
        yield tup


def parallel_lists_generator(*lists):
    for elems in zip(*lists):
        yield elems


def flatten_list_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
        else:
            yield item


def nested_dict_generator(d):
    for key, value in d.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)


def powers_of_two_generator(n):
    for i in range(n + 1):
        yield 2 ** i


def powers_of_base_generator(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base


def squares_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 2


def cubes_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 3


def factorials_generator(n):
    for i in range(n + 1):
        yield math.factorial(i)


def collatz_sequence_generator(n):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1


def geometric_progression_generator(initial, ratio, limit):
    term = initial
    while term <= limit:
        yield term
        term *= ratio


def arithmetic_progression_generator(initial, difference, limit):
    term = initial
    while term <= limit:
        yield term
        term += difference


def running_sum_generator(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total


def running_product_generator(numbers):
    total = 1
    for number in numbers:
        total *= number
        yield total