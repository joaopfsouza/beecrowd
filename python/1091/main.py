def define_position(N: int, M: int, xy_houses: list):

    for position in xy_houses:

        x_house, y_house = map(int, position.split())

        diff_x = x_house - N
        diff_y = y_house - M

        position = ""

        if diff_x == 0 or diff_y == 0:
            print("divisa")
            continue

        if diff_y > 0:
            position += "N"
        elif diff_y < 0:
            position += "S"

        if diff_x > 0:
            position += "E"
        elif diff_x < 0:
            position += "O"

        print(position)

data_list = []
data_input = input()

while data_input != "0":
    data_list.append(data_input)
    data_input = input()

# data_list = ['3', '2 1', '10 10', '-10 1', '0 33', '4', '-1000 -1000',
#              '-1000 -1000', '0 0', '-2000 -10000', '-999 -1001', '0']

current_k_position = 0
current_k_value = int(data_list[current_k_position])

while True:
    
    current_k_value = int(data_list[current_k_position])
    next_k_position = current_k_position + 2 + current_k_value

    current_n_value, current_m_value = map(
        int, data_list[current_k_position + 1].split())
    
    define_position(current_n_value, current_m_value, data_list[current_k_position+2:next_k_position])
    
    # print(data_list)
    # print(current_k_value, current_k_position, next_k_position)
    
    if len(data_list) <= next_k_position:
        break
    
    current_k_value = int(data_list[next_k_position])
    # print(current_k_value, current_k_position, next_k_position)

    current_k_position = next_k_position


