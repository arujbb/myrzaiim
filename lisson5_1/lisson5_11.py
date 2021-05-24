d_rus={
    'мандарин': '귤',
    'яблоко' : '사과',

}

print(d_rus)
print(d_rus['мандарин'])
print(d_rus['яблоко'])

print()

while True:
    lang = input("Выберите язык словаря")
    if lang == "rus":
        word = input("слова с русского на корейский")
        print(d_rus[word])
    elif lang == "kor":
        word = input("слова с руского на корейский")
        print(d_rus[word])
    else:
        print("Выберите один из языков")
        print()


