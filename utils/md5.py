#coding:utf-8
import hashlib

#简单的测试一个字符串的MD5值
def getMD5(src):
    m=hashlib.md5()
    m.update(src)
    return m.hexdigest()

