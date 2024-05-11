# Task 1
arrList1 = ['Kostya', 22, 22.67, ' Be The Legend']
print(arrList1[0], arrList1[2])
arrList1[2] = 'Anne'
print(arrList1)
print(arrList1[1:2])
print(type(arrList1[0]), type(arrList1[1]))
print(len(arrList1))
print(arrList1[2].upper())
print(arrList1[3].strip())
print(arrList1[3].lower(), '\n')

# Task 2
arrList2 = ('You are the best', 234, 'Hello', 25.01)
print(type(arrList2))
print(type(arrList2[0]), type(arrList2[3]))
print(arrList2[0], arrList2[3])
tupleOne = tuple(arrList2[2])
print(tupleOne)
print(len(arrList2[0]))
print(arrList2[1], 'Is it integer?', isinstance(arrList2[1], int), '\n')

# Task 3
setOne = {2, 5, 6, 6, 7, 3, 5, 8, 4}
print('set =', setOne)
print(len(setOne))
setOne.add(10)
print('set =', setOne)
setOne.discard(6)
print('set =', setOne, '\n')

# Task 4
myDict = {'carType': 'universal',
          'carName': 'Renault',
          'carModel': 'Scenic',
          'carYear': 1997}
carDict = {1: 'Mercedes 190E',
           2: 'Ferrari F40',
           3: 'BMW E30',
           4: 'Audi 100 C4 Quattro'}
print(myDict['carName'])
print(carDict[1])
print(myDict['carName'].upper())
print(carDict[2].split())
print(carDict.keys())
print(len(carDict[3]))
print(tuple(myDict['carType']), '\n')

# Task 5
strYear = str(myDict['carYear'])
setToList = list(setOne)
print(strYear, '\n', setToList)

# Task 6
productListNum = [10100, 12500, 18250]
productListCars = ['Renault Megane', 'Honda CR-V', 'Hyondai SantaFe']
productsCount = 'Автомобиль: {}, Цена: {} euro.'
productName1 = productsCount.format(productListCars[0], productListNum[0])
productName2 = productsCount.format(productListCars[1], productListNum[1])
productName3 = productsCount.format(productListCars[2], productListNum[2])
print('\n', productName1, '\n', productName2.strip(), '\n', productName3.strip(), '\n')

# Task 7
yourAge = input('Введите свой возраст: ')
age = int(yourAge)
newAge = age + 15
newAge1 = str(age)
print('Ваш возраст через 15 лет составит:', newAge, '\n')

# Task 8
fruits = ['Apple', 'Banana', 'Pear']
searchItem = input('Enter your item: ')
print(searchItem in fruits, '\n')

newList = {1, 0, 6, 4, 5, 2, 38, 45}
searchNumber = int(input('Enter your number: '))
print(searchNumber not in newList)
