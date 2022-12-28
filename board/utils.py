from datetime import datetime


def hex_to_rgb(hex):
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex[i:i + 2], 16)
        rgb.append(decimal)

    return tuple(rgb)


def rgb_to_hex(r, g, b):
    return '{:X}{:X}{:X}'.format(r, g, b)


def create_data_format(board_data):
    dict_board = dict()
    dict_board["color_R"] = board_data[0]
    dict_board["color_G"] = board_data[1]
    dict_board["color_B"] = board_data[2]
    dict_board["date_time"] = datetime.fromtimestamp(float(board_data[3]) / 1000.0)
    dict_board["temp"] = board_data[4]
    dict_board["humidity"] = board_data[5]
    dict_board["LED_1"] = board_data[6]
    dict_board["LED_2"] = board_data[7]
    dict_board["LED_3"] = board_data[8]
    dict_board["speaker"] = board_data[9]
    return dict_board


