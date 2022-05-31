import re


def error():
    print('不是LL1文法')
    exit(0)


def left(head):
    return head.split('->')[0]


def right(head):
    return head.split('->')[1]


class LL1:
    def __init__(self):
        self.Vn = ['S', 'A']
        self.Vt = ['a', 'b']
        self.start = 'S'  # 开始符号
        self.production = ['S->aSA', 'A->b', 'A->$', 'S->$']  # 产生式
        self.isempty = {}
        self.first = {}
        self.follow = {}
        self.select = {}

    def init(self):
        for vn in self.Vn:
            self.isempty[vn] = None
            self.first[vn] = []
            self.follow[vn] = []
            self.follow[self.start] = ['#']
            self.select[vn] = {}

        for pro in self.production:
            self.select[left(pro)][right(pro)] = []

    def begin_judge(self):
        dic_map = {}
        for st in self.Vn:
            array = []
            for line in self.production:
                if line.split('->')[0] == st:
                    array.append(line.split('->')[1])
            dic_map[st] = array
        for key in dic_map.keys():
            lens = len(dic_map[key])
            for i in range(lens - 1):
                x = dic_map[key][i][0]
                for j in range(i + 1, lens):
                    y = dic_map[key][j][0]
                    if x == y:
                        error()
        for line in self.production:
            if line.split('->')[0] == line.split('->')[1][0]:
                error()

    def __judge_empty(self, head):
        if head.split('->')[1][0] in self.Vt:
            self.isempty[head.split('->')[0]] = False
        elif head.split('->')[1][0] == '$':
            self.isempty[head.split('->')[0]] = True
        elif head.split('->')[1][0] in self.Vn:
            x = head.split('->')[1][0]
            for pro in self.production:
                if pro.split('->')[0] == x:
                    self.__judge_empty(pro)

    def empty(self):
        for i in range(len(self.production)):
            self.__judge_empty(self.production[i])

    def __first_priv(self, head):
        if head.split('->')[1][0] in self.Vt:
            self.first[head.split('->')[0]].append(head.split('->')[1][0])
        elif head.split('->')[1][0] == '$':
            self.first[head.split('->')[0]].append('$')
        elif head.split('->')[1][0] in self.Vn:
            x = head.split('->')[1][0]
            for pro in self.production:
                if pro.split('->') == x:
                    self.__first_priv(pro)

    def first_solve(self):
        for i in range(len(self.production)):
            self.__first_priv(self.production[i])

    def __follow_priv(self, head):
        fin = head
        for pro in self.production:
            try:
                index = right(pro).index(fin)
            except:
                index = -1
            if index == -1:
                continue
            if index + 1 == len(right(pro)):
                self.follow[fin].append('Follow(' + left(pro) + ')')
            elif right(pro)[index + 1] in self.Vt:
                if right(pro)[index + 1] not in self.follow[fin]:
                    self.follow[fin].append(right(pro)[index + 1])
            elif right(pro)[index + 1] in self.Vn:
                for i in self.first[right(pro)[index + 1]]:
                    if i != '$':
                        self.follow[fin].append(i)

    def follow_solve(self):
        for i in range(len(self.Vn)):
            self.__follow_priv(self.Vn[i])
        judic = {}
        while 1:
            if judic == self.follow:
                break
            judic = self.follow
            for key in self.follow:
                for str in self.follow[key]:
                    ret = re.match('Follow...', str)
                    if ret != None:
                        k = str.split('(')[1].split(')')[0]
                        for s in self.follow[k]:
                            self.follow[key].append(s)
        for key in self.follow:
            for str in self.follow[key]:
                ret = re.match('Follow...', str)
                if ret != None:
                    self.follow[key].remove(str)

    def __select_priv(self, head):
        fin = left(head)
        ter = right(head)
        if ter[0] in self.Vt:
            self.select[fin][ter].append(ter[0])
        elif ter[0] == '$':
            self.select[fin][ter] = list(set(self.select[fin][ter]).union(set(self.follow[fin])))
        elif ter[0] in self.Vn:
            pass

    def select_solve(self):
        for i in range(len(self.production)):
            self.__select_priv(self.production[i])

if __name__ == '__main__':
    a = LL1()
    a.begin_judge()
    a.init()
    a.empty()
    a.first_solve()
    a.follow_solve()
    a.select_solve()
    print('Empty:', end=" ")
    print(a.isempty)
    print('First:', end=" ")
    print(a.first)
    print('Follow:', end=" ")
    print(a.follow)
    print('Select:', end=" ")
    print(a.select)
