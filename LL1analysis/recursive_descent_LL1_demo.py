# start_states->Aa|b
# A->SB
# B->ab

# start_states->bA
# A->abaA|$

# SELECT(start_states->bA) = {b}
# SELECT(A->abaA) = {a}
# SELECT(A->$) = {#}
def message(status, message):
    if status == 'success':
        print(message+'\n')
        exit(0)
    elif status == 'error':
        print(message+'\n')
        exit(0)

def parseS(expression, point, sym):
    if sym == 'b':
        point = point + 1
        sym = expression[point]
        parseA(expression, point, sym)
    else:
        message('error', 'syntax error')

def parseA(expression, point, sym):
    if sym == 'a':
        point = point + 1
        sym = expression[point]
        if sym == 'b':
            point = point + 1
            sym = expression[point]
            if sym == 'a':
                point = point + 1
                sym = expression[point]
                parseA(expression, point, sym)
            else:
                message('error', 'syntax error')
        else:
            message('error', 'syntax error')

    elif sym == '#':
        message('success', '分析成功')
    else:
        message('error', 'syntax error')

if __name__ == '__main__':
    point = 0
    expression = 'baba#'
    sym = expression[point]
    parseS(expression, point, sym)
    if sym == '#':
        message('success', '分析成功')
    else:
        message('error', 'ERROR: expect #')
