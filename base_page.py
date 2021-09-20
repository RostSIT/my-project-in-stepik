'''
1. Создайте в своем проекте папку pages, там мы будем хранить все наши Page Object

2. В папке создайте два файла: base_page.py и main_page.py

Для начала сделаем базовую страницу, от которой будут унаследованы все остальные классы. В ней мы опишем
вспомогательные методы для работы с драйвером.

3. В файле base_page.py создайте класс с названием BasePage.

В Python такие вещи делаются с помощью следующей конструкции:

class BasePage(): 4. Теперь в наш класс нужно добавить методы. Первым делом добавим конструктор — метод,
который вызывается, когда мы создаем объект. Конструктор объявляется ключевым словом __init__. В него в качестве
параметров мы передаем экземпляр драйвера и url адрес. Внутри конструктора сохраняем эти данные как аттрибуты нашего
класса. Получается примерно так:

def __init__(self, browser, url):
    self.browser = browser
    self.url = url
5. Теперь добавим еще один метод open. Он должен открывать нужную страницу в браузере, используя метод get().

Объявите ниже в том же классе:

def open(self):
и реализуйте этот метод: нужна всего одна строка. Эту строку нужно отправить в качестве ответа на это задание, без отступов.

6. После того как Stepik принял ваш ответ как правильный, добавьте новые файлы в Git и зафиксируйте изменения
коммитом (не забудьте осмысленное сообщение).



В итоге у вас должен следующий код в файле base_page.py:

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        # ваша реализация
Напиши
'''

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self)
