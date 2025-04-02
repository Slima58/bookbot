
def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        contents = contents.split()
    return len(contents)

def order_dict(d_sample):
    dvalues = [ (k,v) for k,v in d_sample.items()]
    ordered = sorted([*d_sample.values()])
    ordered.reverse()
    enum_list = list(enumerate([*d_sample.values()]))
    o_id = []
    for num in ordered:
        for i, v in enum_list:
            if num == v:
                o_id.append(i)
            else:
                pass
    return { dvalues[id][0] : dvalues[id][1] for id in o_id }

def alpha_check(dict_sample):
    remove_k = []
    for k, v in dict_sample.items():
        if k.isalpha():
            pass
        else:
            remove_k.append(k)
    for key in remove_k:
        dict_sample.pop(key)
    return dict_sample

def get_character_dict(file_path):
    with open(file_path) as f:
        contents = f.read()
    char_l = [*contents.lower()]
    char_set = { char for char in char_l}
    char_dict = {char : 0 for char in char_l}
    for char in char_set:
        for i in char_l:
            if char == i:
                char_dict[char] += 1
            else:
                pass
    acheck = alpha_check(char_dict)
    result = order_dict(acheck)
    return result

