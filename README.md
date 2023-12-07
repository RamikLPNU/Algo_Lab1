# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконав: Нестор Роман Богданович(Група ІР-25)

### Лабораторна робота №1 (Варіант 2 Рівень 3)

Напишіть функцію, яка приймає невпорядкований масив цілих чисел і повертає довжину найдовшої пікової підпослідовностію Для формування пікової підпослідовності необхідно мінімум 3 числа. Пікова підпослідовність визначається як послідовність чисел, яка починається з меншого числа, після чого наступне число строго більше попереднього, поки вони не досягнуть вершини (максимального значення у підпослідовності). Всі значення після досягнення вершини мають бути завжди меншими від попередника. Наприклад, пікова послідовність може мати вигляд:

1 7 2 Де 7 - є вершиною послідовності

1 2 3 - не є піковою послідовністю (немає лівої частки) 3 2 1 - також не є піковою полідовністю (немає правої частки) -1 -5 -1 - теж не є піковою послідовністю (необхідно знайти вершину, а не впадину)

У масиві може бути декілька пікових підпослідовностей, необхідно знайти довжину максимальної

Приклад Для вхідного масиву: 1, 3, 5, 4, 2, 8, 3, 7, знайдена найдовша пікова підпослідовність має довжину 5 - 1, 3, 5, 4, 2

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest та перевірити сценарії коли: всі елементи масиву посортовані за зростанням, посортовані за спаданням, масив з 2х елементів, не містять пікових підпослідовностей, містять 3 пікові послідовності
​

***
### Лабораторна робота №2 (Варіант 2 Рівень 3)

Пiсля швидкого випуску нової версiї своєї операцiйної системи, компанiя NanoSoft
почала отримувати вiд користувачiв численнi повiдомлення про помилки. Щоб
слiдкувати за прогресом виправлення помилок, команда розробникiв вирiшила поставити
велику квадратну дошку, i прикрiпити до неї по листку для кожної помилки. Проте,
щоб дошка вмiстилася в кiмнатi, потрiбно, щоб вона була не надто великою.
Всi N листкiв мають прямокутну форму i однаковий розмiр W × H. Їх не можна
повертати, а також накладати один на iнший.
Знайдiть мiнiмальний розмiр квадратної дошки, яка здатна вмiстити всi листки.
Приклад мiнiмальної дошки, яка може вмiстити 10 листкiв 2 × 3 (див картинку)
​
Вхiднi данi
три числа N, W, H — кiлькiсть листкiв, ширина та висота листка вiдповiдно.
• 1 ≤ N ≤ 1012
• 1 ≤ W ≤ 109
• 1 ≤ H ≤ 109
Вихiднi данi
одне число — мiнiмальна довжина сторони квадратної дошки.
​
Приклад 1
N, W, H = 10, 2, 3
Результат:
9
​
Приклад 2
N, W, H = 2, 1000000000, 999999999
Результат:
1999999998
​
Приклад 3
N, W, H = 4, 1, 1
Результат:
2

***

### Лабораторна робота №3 (Варіант 2 Рівень 3)

Для заданого бінарного дерева перевірте, чи воно є збалансованим деревом. Бінарне дерево вважається збалансованим, якщо різниця у висоті його лівого та правого піддерев не перевищує 1 для будь-якого піддерева.

Розглянемо таке бінарне дерево:

    1
   / \
  2   3
 / \     
4   5   

Це дерево є збалансованим, оскільки різниця висоти лівого піддерева та правого піддерева не перевищує 1.

Реалізована вами функція is_tree_balanced(node: BinaryTree) -> bool отримує на вхід корінь бінарного дерева та повертає True, якщо бінарне дерево є збалансованим, та False, якщо воно не збалансоване.

Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу BinaryTree наступним чином:

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)

***

### Лабораторна робота №4 (Варіант 2 Рівень 3)

Задача про шахового коня 

Дано шахівницю, знайдіть найкоротшу відстань (мінімальна кількість ходів), яку пройшов кінь, щоб досягти заданого пункту призначення з заданого джерела.

Наприклад,

Вхідні дані:



 
N = 8 (дошка 8 × 8)
Джерело = (7, 0)
Пункт призначення = (0, 7)
 
Результат: мінімальна необхідна кількість кроків – 6 (див рисунок, червоними хрестиками позначено 

<image src="1.png" alt="Текст с описанием картинки">

Кінь може ходити у восьми можливих напрямках від даної клітини, як показано на наступному малюнку:

<image src="2.png" alt="Текст с описанием картинки">


Ми можемо знайти всі можливі місця, куди лицар може переміститися з даного місця, використовуючи масив, який зберігає відносну позицію руху лицаря з будь-якого місця. Наприклад, якщо поточне розташування (x, y), ми можемо перейти до (x + row[k], y + col[k]) для 0 <= k <= 7 за допомогою такого масиву:

row[] = [ 2, 2, -2, -2, 1, 1, -1, -1 ]
col[] = [ -1, 1, 1, -1, 2, -2, 2, -2 ]

З позиції (x,y) кінь може рухатись на клітинки з координатами:

(x + 2, y – 1)
(x + 2, y + 1)
(x – 2, y + 1)
(x – 2, y – 1)
(x + 1, y + 2)
(x + 1, y – 2)
(x – 1, y + 2)
(x – 1, y – 2)

Вхідні дані містяться у файлі input.txt:
 
8	# розмір поля
7, 0	# стартова точка
0, 7     # точка призначення

Результуючий файл має містити кількість ходів


Результуючий файл має містити значення найкоротшого шляху від початкової точки до точки призначення


### Лабораторна робота №5 (Варіант 2 Рівень 3)

Пиво

Аутсорс компанія (один з лідерів ринку) готується до корпоративу.  HR відділ відправив опитувальник щодо видів пива, які можна буде роздавати на на святі.  Переважно працівники компанії люблять небагато видів пива, і будуть дуже ображені, якщо принаймні одного з пив, які вони люблять, не буде на вечірці.  Оскільки ви - лідер ринку, то вам не можна ображати працівників.
З іншої сторони, закупити усі можливі види пива - дорого.  Вашим завдання буде з’ясувати скільки різних видів пива потрібно буде привезти на корпоратив.


Вхідні дані:
	Перший рядок містить числа N - кількість працівників та B - кількість доступних пив.  Другий рядок містить N*B літер N або Y.  Якщо літера i*N + j - Y, то працівнику i подобається пиво j

Вихідні дані:
	Найменша кількість видів пива, яка повинна бути на святі

Обмеження:
	Кожному працівнику подобається принаймні один вид пива
	0 < N < 50
	0 <B < 50
Приклади:
In:
2 2
YN NY
Out:
	2
	(Першому працівнику подобається тільки пиво 1, а другому тільки пиво 2, тому доведеться купляти два типи пива)

In:
6 3
YNN YNY YNY NYY NYY NYN
Out:
	2
	(Хоча більшості - чотирьом працівникам - подобається третє пиво, найоптимальніше буде купити 1 та 2 сорти)



### Лабораторна робота №5 (Варіант 2 Рівень 3)

Створити функцію на мові програмування Python, яка приймає дві стрічки: "haystack" (довільний текст) та "needle" (шукана стрічка). Програма повинна знайти індекси всіх входжень стрічки "needle" в стрічці "haystack" та повернути цей індекс, використовуючи  метод Кнутта-Морріса-Прата для пошуку підстрічки у стрічці