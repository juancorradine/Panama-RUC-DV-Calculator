def calculate(old_ruc, ructb):
    j = 2
    nsuma = 0

    for c in reversed(ructb):
        if old_ruc and j == 12:
            old_ruc = False
            j -= 1

        nsuma += j * (ord(c) - ord("0"))
        j += 1
    r = nsuma % 11
    return str(11 - r) if r > 1 else str(0)
