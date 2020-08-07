"""

WOLFSORT

AUF

by PVPender

"""


class AUFexception(Exception):
    def __init__(self, text):
        self.text = text


class Wolf:

    def __init__(self):
        pass
    @staticmethod
    def wolf_sort(mas, left, right):
        massive = mas
        if left > right:
            raise AUFexception ("AUF exception! Can't count auf_int!")
        else:
            auf_int = (right - abs(left)) // 2
            auf_mas = [auf_int]
            auf_index = 0
            for i in range(len(mas)):
                if mas[i] < auf_int:
                    auf_mas.insert(0, mas[i])
                    auf_index += 1
                else:
                    auf_mas.append(mas[i])
            auf_mas.pop(auf_index)
            del mas[:]
            mas.extend(auf_mas)
            return mas

