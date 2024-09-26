import json

def bubble_sort(arr):
    swap_counter = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_counter += 1
    return swap_counter

def run_test(test_num, arr, expected_swaps, expected_sorted_arr):
    
    swaps = bubble_sort(arr)
    if swaps == expected_swaps and arr == expected_sorted_arr:
        print(f"Тест {test_num}: Результат: да. Обменов : {expected_swaps}. Массив: {expected_sorted_arr}")
        return True
    else:
        print(f"Тест {test_num}: Результат: нет")
        print(f"Ожидалось: {expected_swaps} обменов, массив: {expected_sorted_arr}")
        print(f"Получено: {swaps} обменов, массив: {arr}")
        return False

def input_test_cases():
    test_cases = []
    num_tests = int(input("Введите количество тестов: "))
    for i in range(num_tests):
        arr = list(map(int, input(f"Введите элементы массива для теста {i + 1}, разделенные пробелом: ").split()))
        expected_swaps = int(input(f"Введите ожидаемое количество обменов для теста {i + 1}: "))
        expected_sorted_arr = list(map(int, input(f"Введите ожидаемый отсортированный массив для теста {i + 1}, разделенный пробелом: ").split()))
        test_cases.append({"arr": arr, "expected_swaps": expected_swaps, "expected_sorted_arr": expected_sorted_arr})
    return test_cases

def main():
    user_choice = input("Вы хотите ввести свои тестовые случаи? (да/нет): ").lower()
    if user_choice == 'да':
        test_cases = input_test_cases()
    else:
        test_cases = json.load(open(r"C:\Users\febor\YandexDisk\Data Sciense\SkillFacroty\VIVT\Testing_vivt\1\test_cases.json"))  #для проверки работы программы изменить путь к файлу с тестовыми случаями
        print(f'Ввывод тестовых случаев в формате json:{test_cases}')

    passed_tests = 0
    for i, test in enumerate(test_cases):
        arr_copy = test["arr"].copy()  # Создаем копию массива для тестирования
        if run_test(i + 1, arr_copy, test["expected_swaps"], test["expected_sorted_arr"]):
            passed_tests += 1
    
    print(f"Количество пройденных тестов: {passed_tests} из {len(test_cases)}")

if __name__ == "__main__":
    main()
