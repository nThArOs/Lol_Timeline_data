for p_id, p_info in timelime_data.items():
    #print("ID ", p_id)

    for key in p_info:
        #print(key + ':', p_info[key])
        print(key)

def recursive_items(dict):
    for key, value in dict.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)


#for key, value in recursive_items(timelime_data):
    #print(key, value)