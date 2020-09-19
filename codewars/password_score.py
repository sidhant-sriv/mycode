def alphanumeric(password):
    characterset = 'qazwsxedcrfvtgbyhnujmikolp1234567890QAZWSXEDCRFVTGBYHNUJMIKOLP'
    score = 0
    length = len(password)
    if length==0:
        return False
    for i in password:
        if i in characterset:
            score += 1
        else:
            pass
    return length==score