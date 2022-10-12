name=str(input("Введите имя студента: "))
surname=str(input("ведите фамилию студента: "))
age=int(input("Введите год рождения студента: "))
print(name,'_',surname,'_',age)
buf=name
name=surname
surname=buf
age+=60
print(name,surname,age)
