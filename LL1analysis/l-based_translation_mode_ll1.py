def message(status, message):
    if status == 'success':
        print(message+'\n')
        exit(0)
    elif status == 'error':
        print(message+'\n')
        exit(0)


def parseB(expression, point, f):
    Bv = None
    if expression[point] == '0':
        Bv = 0
    elif expression[point] == '1':
        Bv = pow(2, -f)
    else:
        message('error', 'syntax error #')
    return Bv


def parseS(expression, point, f):
    Sv = None
    if expression[point] == '0' or expression[point] == '1':
        Bf = f
        Bv = parseB(expression, point, Bf)
        Slf = f + 1
        point = point + 1
        Slv = parseS(expression, point, Slf)
        Sv = Slv + Bv
    elif expression[point] == '#':
        Sv = 0
    else:
        message('error', 'syntax error #')
    return Sv


def parseN(expression, point, *args):
    if expression[point] == '.':
        point = point + 1
        Sf = 1
        Sv = parseS(expression, point, Sf)
        return Sv
    else:
        message('error', 'syntax error #')


if __name__ == '__main__':
    point = 0
    expression = '.101#'
    result = parseN(expression, point)
    print(result)
    message('success', '分析成功')
