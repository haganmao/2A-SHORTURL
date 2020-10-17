import pytest
import hashlib



def getCode(self, originalUrl):
        shortCode = []
        for code in range(97, 123):
            if (code == 105 or code == 106 or code == 108 or code == 111):
                continue
            shortCode.append(chr(code))
        for code in range(0, 10):
            if (code == 0):
                continue
            shortCode.append(str(code))
        for code in range(65, 91):
            if (code == 73 or code == 79):
                continue
            shortCode.append(chr(code))
        shortCode = tuple(shortCode)
        # return shortCode, len(shortCode)

        # get the md5 str for originalurl
        originalMd5 = '52faae1ac7f8f63f2db5df97ba41f5eb'

        # The final options for code list
        code = []
        # slice the Md5 to 4 pieces
        for i in range(0, 4):
            p = int(originalMd5[i * 8:(i + 1) * 8], 16)
            shortCodeList = []
            # for loop 5 times to get each option of shortCodeList
            for j in range(0, 5):
                k = 0x00000036 & p
                shortCodeList.insert(0, shortCode[k][::-1])
                p = p >> 6
            code.append(''.join(shortCodeList))
        return code


def tonecinclist(self,originalUrl):
    getCode_list = getCode('',originalUrl)
    print(getCode_list)
    getCode_one = getCode_list[0]
    assert getCode_one in getCode_list

tonecinclist('',originalUrl='https://www.tornadoweb.org')
