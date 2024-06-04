Лабораторна робота №17: Генератори в Python
Мета роботи:

    Ознайомитися з поняттям генераторів у Python.
    Навчитися створювати та використовувати різні типи генераторів.
    Зрозуміти переваги генераторів у порівнянні зі звичайними послідовностями.

Опис завдання:

Реалізувати набір функцій-генераторів, які виконують різні операції над даними:

    Генерація числових послідовностей (парні, непарні, числа Фібоначчі, прості числа).
    Обхід структур даних (дерева, графи, словники).
    Робота з файлами та рядками.
    Операції над списками та кортежами (унікальні елементи, реверс, декартовий добуток, перестановки, комбінації).
    Генерація вкладених структур (списки, словники).
    Математичні послідовності (степені, факторіали, послідовність Коллатца).

Виконання роботи:

    Структура проекту:
        main.py: Основний файл з реалізацією всіх генераторів.
        README.md: Цей файл зі звітом.

    Опис функцій:
        number_generator(numbers): Генератор, що повертає елементи з наданої послідовності.
        even_number_generator(start, end): Генератор парних чисел у заданому діапазоні.
        odd_number_generator(start, end): Генератор непарних чисел у заданому діапазоні.
        fibonacci_generator(): Генератор чисел Фібоначчі.
        prime_number_generator(limit): Генератор простих чисел до заданої межі.
        pre_order_traversal(root), in_order_traversal(root), post_order_traversal(root): Генератори для різних типів обходу бінарного дерева.
        dfs_traversal(graph, start), bfs_traversal(graph, start): Генератори для обходу графів у глибину та ширину.
        dict_keys_generator(d), dict_values_generator(d), dict_items_generator(d): Генератори для отримання ключів, значень та пар ключ-значення зі словника.
        file_lines_generator(file_path), file_words_generator(file_path): Генератори для читання рядків та слів з файлу.
        string_chars_generator(s): Генератор символів рядка.
        unique_elements_generator(lst), reverse_list_generator(lst): Генератори для отримання унікальних елементів та реверсу списку.
        cartesian_product_generator(lst1, lst2), permutations_generator(lst), combinations_generator(lst): Генератори для декартового добутку, перестановок та комбінацій.
        tuple_list_generator(lst), parallel_lists_generator(*lists): Генератори для роботи з кортежами та паралельними списками.
        flatten_list_generator(nested_list), nested_dict_generator(d): Генератори для "розплющення" вкладених списків та словників.
        powers_of_two_generator(n), powers_of_base_generator(base, limit), squares_generator(start, end), cubes_generator(start, end), factorials_generator(n): Генератори для різних математичних послідовностей.
        collatz_sequence_generator(n), geometric_progression_generator(initial, ratio, limit), arithmetic_progression_generator(initial, difference, limit): Генератори для послідовності Коллатца, геометричної та арифметичної прогресій.
        running_sum_generator(numbers), running_product_generator(numbers): Генератори для накопичувальної суми та добутку.

Результати:


В ході лабораторної роботи було успішно реалізовано набір генераторів для різних завдань. Генератори є потужним інструментом у Python, що дозволяє ефективно працювати з даними, особливо коли обсяг даних великий або невідомий заздалегідь.


Інструкції з запуску:


    Переконайтеся, що у вас встановлено Python 3.12
    Склонуйте цей репозиторій: git clone <URL-репозиторію>
    Перейдіть у папку з проектом: cd lab17
    Запустіть файл main.py: python main.py