todos = []



while True:
    action = input('Выбери действие: Y) Добавить задачу V) Показать задачу ')
    if action == 'Y' :
        todo = input('Задача:')
        deadline = input('Дэдлайн:')
        dead_added = input('Добавленно:')
        todos.append([todo, deadline, dead_added ])
    elif action == 'V':
        print()
        if len(todos) == 0:
            print('Нет задач!')
        for i in todos:
            print(i[0], i[1], i[2])
        else:
            print('Выберите правильный вариант! \n')

