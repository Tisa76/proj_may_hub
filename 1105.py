print('infodocs')
#second_street
#XXX
#a = 45
#print (2+a)
#print (a % 10)
#text = 'Glory glory man united'
#print('united' in text)
#print('united' not in text)

#Преобразователи
#Q = input('biggest club?')
#print('Yes', Q, 'GGMU') # между слов не забывать запятую

#Q2 = input('enter the number')
#print(type(Q2)) #при написании 'type' выводит какой тип этой строки как в примере это как 'str - строка/текст'

#Q3 = int(input('only number pls')) # int преобразовывает значение 'str' в 'int -целые цифры/числа'
#print(type(Q3))
#print(2 + Q3) #в последующем можно добавлять команды (+-)

#Если еще 'bool' те булевое/логическое значение ответ всегда будет содержать true/false
#Также есть 'float' это цифры/числа дробные.


#Коллекции.
some_list = [2, 3, 4, 'cow', 'car', 765, 'negros'] #[] пишется чтобыБ создать формат list без него будет формат tuple
#Если писать тип list без [] то, нужно проделывать такое: some_list = list(2, 3, и тд)
print(some_list)
print(some_list[2]) #[] вытаскивает опредленное значение из списка,
#питон начинает отсчет с 0 а не с 1, поэтому, чтобы запросить 3 значение в списке нужно писать 3.
print(some_list[-1]) #[-1]вытаскивает последнее значение в списке. те когда дает значение [-] питом считает с конца.

some_list [-1] = 'spanishword' #так мы поменяли последнее значение
print(some_list)


