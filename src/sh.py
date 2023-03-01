alf = "QWERTYUIOPASDFGHJKLZXCVBNMabcdefghiЙФЯЧЫЦУКАВСМИПЕНРТЬОГШЩДЛБЮЖЗХЭЪЬjklmnopqrstuvwxyz123456789_йфячыцувсмипакенртьогшлбюдщзжэхъ*-+=*&:;?!@"
table = ["q", "w", "e", "r", "t",
         "y", "u", "i", "o", "p",
         "a", "s", "d", "f", "g",
         "h", "j", "k", "l", "z",
         "x", "c", "v", "b", "n",
         "m", "1", "2", "3", "4",
         '5', '6', '7', '8', '9',
         '0', 'й', 'ц', 'у', 'к',
         'е', 'н', 'г', 'ш', 'щ',
         'з', 'х', 'ъ', 'ф', 'ы',
         'в', 'а', 'п', 'р', 'о',
         'л', 'д', 'ж', 'э', 'я',
         'ч', 'с', 'м', 'и', 'т',
         'ь', 'б', 'ю', '_', '!',
         '_', '?', '*', '!', '@',
         '=', '+', '&', ';', ':',
         "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
         "A", "S", "D", "F", "G", "H", "J", "K", "L",
         "Z", "X", "C", "V", "B", "N", "M", "Й", "Ц", "У", "К", "Е",
         "Н", "Г", "Ш", "Щ", "З", "Х", "Ъ", "Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д",
         "Э", "Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю"]

cezar_shifr, cezar_un, polibia_shifr, polibia_un = [], [], [], []


def cezar(text, alf, key):
    for j in range(len(text)):
        for i in range(len(alf)):
            # print(i,j)
            if text[j] == alf[i]:
                if i + key > len(alf):
                    # print("          ",i,j)
                    continue
                else:
                    # print("                          ",i,j)
                    cezar_shifr.append(alf[i + key])
                    continue
    return ''.join(cezar_shifr)


def cezar_unsc(text, alf, key):
    for j in range(len(text)):
        for i in range(len(alf)):
            # print(i,j)
            if text[j] == alf[i]:
                if i + key > len(alf):
                    # print("          ",i,j)
                    continue
                else:
                    # print("                          ",i,j)
                    cezar_un.append(alf[i - key])
                    continue
    return cezar_un


def polibia(text, table):
    for i in range(0, len(text)):
        for j in range(0, len(table)):
            if text[i] == table[j]:
                polibia_shifr.append(j)
    return polibia_shifr


def polibia_unsc(text, table):
    for c in text:
        polibia_un.append(table[c])
    return polibia_un


# while cezar_shifr!=[] and cezar_un!=[] and polibia_shifr!=[] and polibia_un!=[]:
#	cezar_shifr,cezar_un,polibia_shifr,polibia_un=[],[],[],[]

"""
while True:
	q1=int(input("1-cezar; 2-polibia; 3-unsifr cezar; 4-unshifr poliba; 5-doubleshifr; 6-unshifr doubleshifr; 7 -quit: "))
	if q1==1:
		text=input("Press the text: ")
		key=int(input("key not more please: "))
		print(cezar(text,alf,key))
	elif q1==2:
		text=input("Press the text: ")
		print(polibia(text,table))
	elif q1==3:
		text=input("Press the text: ")
		key=int(input("key not more please: "))
		cezar_unsc(text,alf,key)
	elif q1==4:
		zx=None
		while zx!=1234:
			zx=int(input())
			if zx <= len(table):
				vrem.append(zx)
				continue
			else:
				continue
		print(polibia_unsc(vrem,table))
	elif q1==5:
		text=input("Press the text: ")
		key=int(input("key not more please: "))
		cezar(text,alf,key)
		print(polibia(cezar_shifr,table))
	elif q1==6:
		key=int(input("key not more please: "))
		zx=int(input())
		while zx!=123:
			zx=int(input())
			vrem.append(zx)
		polibia_unsc(vrem,table)
		print(cezar_unsc(polibia_un,alf,key))
	elif q1==7:
		break
"""
