name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
rost = input("Введите ваш рост: ")
ves = input("Введите свой вес: ")

print (f"{name}, вы ниже увидите ваши данные")


#возраст
if int(age) <= 10:
    print ("Возраст: Ну ты и малолетка")
elif int(age) <= 15:
    print ("Возраст: Жоский подросток")
elif int(age) <= 20:
    print ("Возраст: Усы побрил?")
elif int(age) <= 30:
     print ("Возраст: Скоро женится")   
elif int(age) <= 50:
     print ("Возраст: Скоро уже и помирать")
elif int(age) <= 70:
     print ("Возраст: Ты всё ещё не сдох?")
elif int(age) <= 90:
     print ("Возраст: Ебать ты конечно,Старик")
elif int(age) <= 10000:
     print ("Ебааааааа")

#рост


if int(rost) <= 100:
     print ("Рост: Блоха")
elif int(rost) <= 120:
     print ("Рост: Гном")
elif int(rost) <= 140:
     print ("Рост: Не путайся под ногами")
elif int(rost) <= 160:
     print ("Рост: Ты мне по-нос")
elif int(rost) <= 170:
     print ("Рост: Полу дылда")
elif int(rost) <= 190:
     print ("Рост: Дылда")
elif int(rost) <= 300:
     print ("Рост: Титан")
elif int(rost) <= 100000000:
     print ("Рост: Куда вымахал")
#вес


if int(ves) <= 20:
     print ("Вес: Дрыщ")
elif int(ves) <= 40:
     print ("Вес: худощавка")
elif int(ves) <= 60:
     print ("Вес: норм чел")
elif int(ves) <= 70:
     print ("Вес: Жирный")
elif int(ves) <= 100:
     print ("Вес: Жиробасина")
elif int(ves) <= 300:
     print ("Вес: Жиртресс")
elif int(ves) <= 10000:
     print ("Вес: Сумаист")                                   
input("нажмите 2 раза enter что бы выйти")                                             