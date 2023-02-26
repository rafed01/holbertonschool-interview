#!/usr/bin/python3
"""
    Box opener method.
"""


def canUnlockAll(boxes):
    if type(boxes) is not list and len(boxes)<0:
        return False
    for box in boxes:
        if type(box) is not list:
            return False
    
    keys=[0]
    for key in keys:
            if type(key) is not int and key<0:
                return False
            else:              
                #print(key)
                for bk in boxes[key]:
                    # print("===")                
                     #print(boxes[key])

                    if bk not in keys and bk < len(boxes):
                        keys.append(bk)


    if len(keys)== len(boxes):

        return True
    else :
        return False
