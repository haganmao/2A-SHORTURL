import pytest
import hashlib


def getMd5(self, originalUrl):
        hl = hashlib.md5()
        hl.update(originalUrl.encode(encoding='utf-8'))
        return hl.hexdigest()


original_Url='https://www.tornadoweb.org'
def tone_getMd5():
    getMd5_one = getMd5('',originalUrl=original_Url)

    hlib = hashlib.md5()
    hlib.update(original_Url.encode(encoding='utf-8'))
    getMd5_two = hlib.hexdigest()

    assert getMd5_one == getMd5_two

tone_getMd5()