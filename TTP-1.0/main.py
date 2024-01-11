from os import system
from essential_generators import DocumentGenerator
import re


def true_false_item_of_menu():
    system('cls')
    text = ('__Главное меню__\n'
            '1.Ввести текст с клавиатуры\n'
            '2.Ввести случайный текст\n'
            '3.Выполнение алгоритма программы\n'
            '4.Вывод результата в консоль\n'
            '5.Вывод текста в консоль\n'
            '6.Завершение работы программы\n')
    print(text)
    while True:
        # нахождение ошибки в исполнении
        try:
            return int(input('Введите пункт меню: '))
        except ValueError:
            system('cls')
            print('Введённое значение должно быть цифрой!!!\n'
                  'Попробуйте ещё раз.')
            system('pause')
            system('cls')
            print(text)


def algorithm(input_str):
    algo_work_end = []
    part_of_word = input('Введите символьное сочетание, для проверки его наличия в тексте: ')
    for i in input_str:
        delimiters = "[ ,.!?();]" # выделение символов, которыми разделяются слова
        words = re.split(delimiters, i)
        for word in words:
            if re.search(part_of_word, word):
                algo_work_end.append(word)
    return algo_work_end


def output_text(list_of_str):
    system('cls')
    print(list_of_str)
    system('pause')
    system('cls')


def input_string(input_string_another):
    while True:
        input_str = input('Введите текст: ')
        if input_str:
            input_string_another.append(input_str)
        else:
            break


def main():
    fl_output = False      # флаг не дающий вывести текст
    fl_start_alg = False   # флаг не дающий запустить алгоритм
    list_input_str = []    # пустой список для заполнения нашей строкой
    end_of_alg = []        # пустой список для заполнения нашим алгоритмом

    while True:
        menu_items = true_false_item_of_menu()
        if menu_items == 1:
            list_input_str = end_of_alg = []
            system('CLS')
            input_string(list_input_str)
            fl_start_alg = True
            fl_output = False

        elif menu_items == 2:
            list_input_str = end_of_alg = []
            english_random_text = DocumentGenerator()
            en_text = english_random_text.sentence()
            list_input_str.append(en_text)
            fl_start_alg = True
            fl_output = False

        elif menu_items == 3:
            if not fl_start_alg:
                output_text('Отсутствуют введённые данные, сначла исполните пункты 1 или 2')
            else:
                system('cls')
                end_of_alg = algorithm(list_input_str)
                fl_output = True

        elif menu_items == 4:
            if fl_output == 1:
                output_text(end_of_alg)
            else:
                output_text('Алгоритм не выполнен, вывести результат невозможно')

        elif menu_items == 5:
            system('cls')
            for i in range(len(list_input_str)):
                print(list_input_str[i])
            system('pause')

        elif menu_items == 6:
            system('cls')
            break


if __name__ == '__main__':
    main()
