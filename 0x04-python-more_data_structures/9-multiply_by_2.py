#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multipled_dic = {}
    for key, value in a_dictionary.items():
        multipled_dic[key] = value * 2
    return multipled_dic
