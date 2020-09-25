Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 //3
3
>>> 10 // 3
3
>>> print('Mijn naam is Menno')
Mijn naam is Menno
>>> naam = Menno
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    naam = Menno
NameError: name 'Menno' is not defined
>>> naam = "Menno"
>>> print(naam)
Menno
>>> print(naam.upper())
MENNO
>>> print(naam[0:2])
Me
>>> print(naam[::-1])
onneM
>>> leeftijd = 16
>>> print("Hallo " + naam + " ben je al " + str(leeftijd) + "jaar?")
Hallo Menno ben je al 16jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
17
>>> leeftijd-=1
>>> leeftijd
16
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print("Over " + str(hoelang_al18jaar) + " jaar wordt je 18")

Traceback (most recent call last):
  File "<pyshell#23>", line 3, in <module>
    print("Over " + str(hoelang_al18jaar) + " jaar wordt je 18")
NameError: name 'hoelang_al18jaar' is not defined
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print("Over " + str(hoelang_al18jaar) + " jaar wordt je 18")
elif leeftijd > 18:
	hoelang_al18jaar = leeftijd - 18
	print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd
	      
SyntaxError: EOL while scanning string literal
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print("Over " + str(hoelang_al18jaar) + " jaar wordt je 18")
elif leeftijd > 18:
	hoelang_al18jaar = leeftijd - 18
	print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd")
	      
SyntaxError: EOL while scanning string literal
>>> from random import randint
>>> randint(0,1000)
137
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
483
>>> print("Willekeurig getal tussen 0 en 1000: " + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 483
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-25 11:57:39.583802
>>> datum.strftime("%A %d %B %Y")
'Friday 25 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'vrijdag 25 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'venerdì 25 settembre 2020'
>>> 