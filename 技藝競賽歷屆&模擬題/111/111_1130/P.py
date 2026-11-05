# -*- coding: utf-8 -*-
def treesplit(pre,ino):
    if len(pre)<=1:
        return pre
    
    pre=list(pre)
    root=pre.pop(0)
    
    
    
    left_ino, right_ino = ino.split(root)
    left_pre, right_pre = pre[:len(left_ino)], pre[len(left_ino):]


    return *treesplit(left_pre,left_ino),*treesplit(right_pre,right_ino),root

while 1:
    try:
        pre,ino = input().split()
        print("".join(treesplit(pre,ino)))
    except EOFError:
        break