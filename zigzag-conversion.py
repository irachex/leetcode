'''
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s

        d = ['' for i in xrange(numRows)]
        x = 0
        dx = 1
        for c in s:
            d[x] += c
            if x == numRows - 1:
                dx = -1
            elif x == 0:
                dx = 1
            x += dx

        return ''.join(d)


if __name__ == '__main__':
    f = Solution().convert
    assert f("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert f("PAYPALISHIRING", 1) == "PAYPALISHIRING"
    assert f("PAYPALISHIRING", 2) == "PYAIHRNAPLSIIG"
    assert f("zcdffagygmalkzfmqavtzeqfjtmdxvvwxbefdmfjyfukhcwxctqdziliexlbtjzsmfxprfzqmvctxbqcuifurqcvqqyjzxbnfbcwidouzrowsgyopgiiyndoddxeabrhevgmzuiynywhfxywdggbvlsaopgqszyyvekuavuqtqxanxysgewbpocdfkwakuyfalbagvqblqcbnavvhrxyhbeplapvwncwydwgypimhmnwmksvcpulsyadapbwfdsdjqmhfutmgilutdqxumimmlrmauifyalhqxqytmmzuxtpalouzxilkaxkufsuhfdacwyvikwekrukfihehpqtrpeoxyiedoehkeesrcybtunyfudmmvgfkmthmcorsuaczewsiutbpgcudhircqwoeqyqumjogjqhpozxiubzddvikezowxebpctlqdzzmrgcfibqecrhhnrtrshnsoqhqkvhnwizoqdvahnflhotugmnawcsktccdxlstttjkxhkgwrrdgkzozmoxphjkllpizhduapgzwrfukzaslzgkoxjfgsprgezflezntgnrzumltoefnkpdhbiptzgzdhgqmighqtzpnnchbgmqrduaeesaeybjiiawqgdgbcxorzxuillbrhdxlvxpwzbejdazlfhmkgcbhcwpnjqequcdrbvncwrlztmkzvyjbaklciaqrtwhpangeiugensdhgpgcnrfnbqsktkdogndjalniftmvnrcuikyvbdkeueqnoubxhgghrvrzofueyyagiydlbpp", 789)
