data_list_in_dict = [{
    "name": "ahmet",
    "lastname": "yilmaz"
}]

data_list_in_tuple = [('name', 'mehmet'), ('lastname', 'yilmaz')]
data_list_in_list = [['name', 'aysel'], ['lastname', 'yilmaz']]

data_tuple_in_tuple = (('name', 'mesut'), ('lastname', 'oncel'))
data_tuple_in_list = (['name', 'serkan'], ['lastname', 'inan'])


def tutorial_talent(data) -> list:
    data_output = []
    if type(data) == list:
        data_output = append_key(data)

    elif type(data) == tuple:
        data_output = append_key(data)

    return data_output

def append_key(data):
    data_output = []

    for item in data:
        if type(item) == dict:
            for key, value in item.items():
                if key == 'name':
                    data_output.append(value)
        elif type(item) == tuple or type(item) == list:
            if item[0] == 'name':
                data_output.append(item[1])
        else:
            return data_output

    return data_output


if __name__ == '__main__':

    print('---- data_list_in_dict -----')
    print(tutorial_talent(data_list_in_dict))

    print(' --- data_list_in_tuple -----')
    print(tutorial_talent(data_list_in_tuple))

    print('---- data_list_in_list -----')

    print(tutorial_talent(data_list_in_list))

    print(' --- data_tuple_in_tuple -----')
    print(tutorial_talent(data_tuple_in_tuple))

    print('---- data_tuple_in_list -----')

    print(tutorial_talent(data_tuple_in_list))
