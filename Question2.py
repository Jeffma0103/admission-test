def count(input):
    res = {}
    n = 0
    while n < len(input) :
        if input[n] not in res:
            tmp_char = input[n]
            res[tmp_char] = 0
            
            for i in range(n, len(input)):
                if input[i] == tmp_char:
                    res[tmp_char] += 1
            else :
                continue
        else : 
            n += 1
    return res


def group_by_key(input):
    res = {}
    n = 0
    while n < len(input):
        for i in range(n, len(input)):
            if input[n]["key"] not in res:
                tmp_char = input[n]["key"]
                res[tmp_char] = input[n]["value"]
 
                for j in range(i+1, len(input)):
                    if input[j]["key"] == tmp_char:
                        res[tmp_char] += input[j]["value"]
                    else :
                        continue
            n += 1
    return res
