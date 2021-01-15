class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        i = 0
        s = ''
        a = len(x)/2
        while i < int(a):
            if x[i] == '-':
                # i+=1
                # a += 1
                s = x[i]
                x.pop(i)
                continue
            else:
                tmp = x[i]
                x[i] = x[len(x)-i-1]
                x[len(x)-i-1] = tmp
                i += 1
        i = 0
        if len(x) > 1:
            while x[i] == '0':
                x.pop(0)

        x = "".join(x)

        if int(x).bit_length() < 32:
            return (s+x)
        else:
            return 0
