class Day:
    '''Класс, описывающий день недели'''
    def __init__(self, dct):
        '''Метод инициализации дня недели'''
        self.lessons = dct['день']

    def __str__(self):
        '''Метод строкового представления'''
        return str(self.lessons)

    def __repr__(self):
        '''Метод представления'''
        return self.__str__()

class Lesson:
    '''Класс, описывающий занятия'''

    def __init__(self, lessons):
        '''Метод инициализации дня недели'''

        self.para1 = lessons[0]
        self.para2 = lessons[1]
        self.para3 = lessons[2]
        self.para4 = lessons[3]
        self.para5 = lessons[4]

    def __str__(self):
        '''Метод строкового представления'''
        return '|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(self.para1, self.para2,
                                                             self.para3, self.para4, self.para5)

    def __repr__(self):
        '''Метод представления'''
        return self.__str__()
