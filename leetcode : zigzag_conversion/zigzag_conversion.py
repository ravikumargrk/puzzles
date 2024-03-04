# Question: 
# https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        N = len(s)
        result = ''
        if numRows == 1:
            return s
        for i in range(numRows):
            d = (numRows-2)
            vgap = numRows + d
            for j in range(i, N, vgap):
                vElem = j
                dElem = j+vgap-2*i
                if i in [0, numRows-1]:
                    # print(vElem, end='\t\t')
                    result += s[vElem] 
                else:
                    if dElem >= N:

                        result += s[vElem] 
                    else:
                        # print((vElem, dElem), end='\t\t') 
                        result += s[vElem] 
                        result += s[dElem]

        return result

# testing
cases = [
    {
        'in': ("PAYPALISHIRING", 1),
        'out': "PAYPALISHIRING"
    },
    {
        'in': ("PAYPALISHIRING", 3),
        'out': "PAHNAPLSIIGYIR"
    },
    {
        'in': ("PAYPALISHIRING", 4),
        'out': "PINALSIGYAHRPI"
    },
    {
        'in': ("A", 1),
        'out': "A"
    }
]

def test_answer():
    for id, case in enumerate(cases):
        out = Solution.convert(None, *case['in'])
        if out!=case['out']:
            print('Case  :', id, ' FAIL')
            print('inputs: ', case['in'])
            print('output:', out)
            print('expect:', case['out'])
        else:
            print('Case  :', id, ' PASS')

test_answer()