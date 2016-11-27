# coding:utf-8
import sys
import traceback
import subprocess


def create_file():
    sys.stdout = open("tmp.txt", "w", encoding='utf-8')


class EvalProblem(object):
    def __init__(self, answer, src):
        self.answer = answer
        self.src = src

    def eval(self):
        try:
            create_file()
            exec(self.src)
        except SyntaxError:
            # print('--------------------------------------------')
            print(traceback.format_exc(sys.exc_info()[2]))
            # print('--------------------------------------------')
            return False
        except TypeError:
            # print('--------------------------------------------')
            print(traceback.format_exc(sys.exc_info()[2]))
            # print('--------------------------------------------')
            return False
        else:
            with open("tmp.txt", "r", encoding='utf-8') as read_file:
                if self.answer == read_file.readline():
                    return True
            return False
