def error():
    print('不是LL1文法')
    exit(0)


class LL1:
    def __init__(self):
        self.Vn = ['S', 'A']
        self.Vt = ['a', 'b']
        self.start = 'S'  # 开始符号
        self.production = ['S->aSA', 'A->b', 'A->$', 'S->$']  # 产生式
        self.isempty = {}
        self.first = {}
        self.follow = {}

    def init(self):
        for vn in self.Vn:
            self.isempty[vn] = None
            self.first[vn] = []
            self.follow[vn] = []

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

    def __follow_priv(self):
        pass

    def follow_solve(self):
        pass


if __name__ == '__main__':
    a = LL1()
    a.begin_judge()
    a.init()
    a.empty()
    a.first_solve()

    print(a.first)
    print(a.isempty)