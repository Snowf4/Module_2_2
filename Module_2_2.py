first = int(input('Ведите любое целое число: '))
second = int(input('Ведите любое целое число: '))
thrid = int(input('Ведите любое целое число: '))
if first == second == thrid:
   print('Все значения повторяются! ', int(3))
elif first == second or first == thrid or second == thrid:
   print('Повторяются только два из трёх значений! ', int(2))
elif first != second != thrid:
   print('Ни одно из значений не повторяется! ', int(0))