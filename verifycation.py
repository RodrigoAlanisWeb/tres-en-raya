from tablero import tablero

def main(user):
    win = ''
    if user == 1:
        win = 'xxx'
    else:
        win = 'ooo'

    suma = []
    suma_2 = []
    for i in tablero:
        if i[0]+i[1]+i[2] == win:
            return True
        suma.append(i[0])
    if suma[0]+suma[1]+suma[2] == win:
        return True
    else:
        suma.clear()
        for i in tablero:
            suma.append(i[1])

    if suma[0]+suma[1]+suma[2] == win:
        return True
    else:
        suma.clear()
        for i in tablero:
            suma.append(i[2])
    if suma[0]+suma[1]+suma[2] == win:
        return True
    else:
        suma.clear()
        suma_2.clear()
        count = 0
        for i in tablero:
            suma.append(i[count])
            count += 1

            if count == 3:
                if suma[0]+suma[1]+suma[2] == win:
                    return True
        count_2 = 2
        for i in tablero:
            suma_2.append(i[count_2])
            count_2 -= 1
            if count_2 < 0:
                if suma_2[0]+suma_2[1]+suma_2[2] == win:
                    return True
       
            
        
