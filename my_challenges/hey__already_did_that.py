#  to_base_n(str: int_base_10, int: n) -> str: str_base_n
#  2 <= n < 10
def to_base_n(int_base_10, n):
    residual = int(int_base_10)
    digits_base_n = []
    while residual >= n:
        r = residual % n
        digits_base_n.append(str(r))
        residual = (residual - r) // n
    digits_base_n.append(str(residual))
    return ''.join(digits_base_n[::-1])

#  to_base_10(str: int_base_n, int: n) -> str: str_base_10
#  2 <= n < 10
def to_base_10(int_base_n, n):
    x = list(int_base_n[::-1])
    y_base_10 = 0
    for i, a in enumerate(x):
        y_base_10 += int(a) * (n ** i)
    return str(y_base_10)

def solution(n, b):
    k = len(n)
    m = n
    mini_id = []
    while m not in mini_id:
        mini_id.append(m)
        s = sorted(m)
        x_descend = ''.join(s[::-1])
        y_ascend = ''.join(s)        
        if b == 10:
            int_m = int(x_descend) - int(y_ascend)
            m = str(int_m)
        else:
            int_m_10 = int(to_base_10(x_descend, b)) - int(to_base_10(y_ascend, b))
            m = to_base_n(str(int_m_10), b)
        
        m =  (k - len(m)) * '0' + m
    
    return len(mini_id) - mini_id.index(m)

print(solution("1211", 10))

print(solution("210022", 3))