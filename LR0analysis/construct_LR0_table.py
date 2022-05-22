# P131----LR(0)项目集规范族的构造
import copy
import json

def read_grammer(filepath):
    grammer_G = json.load(open(filepath, 'r', encoding="utf-8"))
    n_terminator = []
    for key in grammer_G.keys():
        n_terminator.append(key)
    for li in grammer_G['S']:
        li = '.' + li
    beginnings = {"S": [li]}
    return grammer_G, n_terminator, beginnings

def move_next_status(now_state, ):
    pass


def closure(*args):
    for key_state in state_I:
        now_status = state_I[key_state]
        template = copy.deepcopy(now_status)
        for key in now_status:
            for li in now_status[key]:
                if li.index('.') + 1 >= len(li):
                    continue
                else:
                    clo = li[li.index('.') + 1]
                    list = []
                    if clo in grammer_G.keys():
                        for state in grammer_G[clo]:
                            list.append('.' + state)
                    template[clo] = list
        state_I[key_state] = template


if __name__ == '__main__':
    grammer_G, n_terminator, beginnings = read_grammer('./Grammer/G.json')
    state_I = {'I0': beginnings}
    transform_table = {}
    print(grammer_G)
    print(state_I)
    closure(grammer_G, state_I, n_terminator, grammer_G)
    print(state_I)
    # index = begining.index('*')
    # begining = list(begining)
    # begining.pop(index)
    # begining = ''.join(begining)
    # print(begining)