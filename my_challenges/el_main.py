from distutils.version import LooseVersion
def solution(l):
    x = []
    x.append(str(",".join(sorted(l, key=LooseVersion))))
    y = x[0].split(',')
    return y

        
print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))