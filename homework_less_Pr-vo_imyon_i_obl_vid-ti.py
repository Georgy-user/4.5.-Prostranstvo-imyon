def test_function(das):

    def inner_function(Inner_Text):
        print(Inner_Text)

    inner_function(das) # Функция inner_function вызывается внутри функции tes_function.

print()
# Внутренняя функция inner_function вызывается из глобальной области видимости
# с помощью функции test_function:
test_function(""" "Я в области видимости функции test_function." """)

# Внутренняя функция inner_function вызывается непосредственно
# из глобальной области видимости вне функции test_function.
print()
inner_function("Я в области видимости функции test_function.")
