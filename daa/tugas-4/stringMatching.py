def match(ls: str, s: str, l_ls: int, l_s: int) -> int:
    i = 0
    found = False
    while i <= l_ls - l_s and not found:
        j = 0
        while j < l_s and ls[i+j] == s[j]:
            j += 1
        if j == l_s:
            found = True
        else:
            i += 1
    if found:
        return i
    else:
        return -1