"""
Для данного задания я выбрал алгоритм быстрой сортировки.
Данный вариант при грамотном выборе опорного элемента (нужно выбирать случайный элемент)
в среднем работает за O(nlog(n)).
При этом обычно он совершает меньше сравнений и перестановок, чем например сортировка слияние,
и на практике он работает быстрее.
К тому же, он требует O(log(n)) памяти.
Конечно, возможна ситуация, когда в каждом случае случайный выбор будет падать на наименьший элемент,
но это крайне маловероятно, и время работы O(n^2) практически невозможный случай.
"""
import random


def quick_sort(nums, l, r):
    if l >= r:
        return
    else:
        q = random.choice(nums[l:r + 1])
        i = l
        j = r
        while i <= j:
            while nums[i] < q:
                i += 1
            while nums[j] > q:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                quick_sort(nums, l, j)
                quick_sort(nums, i, r)


def main():
    nums = random.sample(range(1000), 100)
    print("Not sorted")
    print(nums)
    quick_sort(nums, 0, 99)
    print("Sorted")
    print(nums)


if __name__ == "__main__":
    main()
