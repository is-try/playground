def e(n):
    def iter(cnt, res):
        if cnt <= n:
            return iter(cnt + 1, res + [cnt])
        else:
            return res
    return iter(1, [])

def f(is_op, s):
    if s == []:
        return []
    if is_op(s[0]):
        return s[0:1] + f(is_op, s[1:])
    else:
        return f(is_op, s[1:])

def m(op, s):
    if s == []:
        return []
    return [op(s[0])] + m(op, s[1:])

def a(init, op, s):
    if s == []:
        return init
    return op(s[0], a(init, op, s[1:]))

print(a(0, lambda x, y: x + y, e(100)))