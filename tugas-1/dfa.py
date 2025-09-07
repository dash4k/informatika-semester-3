from delta_hat import l1_hat, l2_hat, l3_hat, l4_hat

def l1(x) -> bool:
    print('A ', end='')
    return True if l1_hat('A', x) == 'F' else False

def l2(x) -> bool:
    print('A ', end='')
    return True if l2_hat('A', x) == 'E' else False

def l3(x) -> bool:
    print('A ', end='')
    state = l3_hat('A', x)
    return True if  state == 'E' or state == 'C' else False

def l4(x) -> bool:
    print('A ', end='')
    state = l4_hat('A', x)
    return True if  state == 'F' or state == 'I' else False