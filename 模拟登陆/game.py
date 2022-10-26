import time
game_list = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
def get_n(game_list):
    ns = []
    for i in game_list:
        if i == '1':
            ns.append(str(game_list.index(i)))
    ns = get_n(game_list)
    for n_str in ns:
        n = eval(n_str)
    return n
def Game_tutorial(game_list):
        while True:
            n = get_n(game_list)
            if eval(str(game_list[n])):
                game_list[n] = '0'
                print(n)
                try:
                    game_list[n-1] = '1'
                except:
                    pass
                if '0' not in game_list:
                    break
                try:
                    game_list[n+1] = '1'
                except:
                    pass
                if '0' not in game_list:
                    break
                try:
                    game_list[n+3] = '1'
                except:
                    pass
                if '0' not in game_list:
                    break
                try:
                    game_list[n-3] = '1'
                except:
                    pass
                print(game_list)
                if '0' not in game_list:
                    break


Game_tutorial(game_list)















