def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    return sorted(strings, key=last_letter)


def enclosing():
    x = 'closed over'
    def local_func():
        print(x)
    return local_func

def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp
