import tablero
import verifycation

def main():
    turns = [1,2]
    turn = 1
    while 1 > 0:
        tablero.main()
        if turn > 2:
            turn = 1
        if turn == 1:
            nums = input('Ingresa las cordenadas: ')
            column = tablero.tablero[int(nums[0])]
            if column[int(nums[2])] == 'x' or column[int(nums[2])] == 'o':
                nums = input('Ingresa las cordenadas: ')
                column = tablero.tablero[int(nums[0])]
                column[int(nums[2])] = 'o'
            else:
                column[int(nums[2])] = 'x'
        elif turn == 2:
            nums = input('Ingresa las cordenadas: ')
            column = tablero.tablero[int(nums[0])]
            if column[int(nums[2])] == 'x' or column[int(nums[2])] == 'o':
                nums = input('Ingresa las cordenadas: ')
                column = tablero.tablero[int(nums[0])]
                column[int(nums[2])] = 'o'
            else:
                column[int(nums[2])] = 'o'
        if verifycation.main(turn):
            tablero.main()
            print(f'El jugador {turn} gana')
            break
        turn += 1