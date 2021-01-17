        s = list(s)
        o = ['(', '[', '{']
        f = [')', ']', '}']
        all = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        p = 0
        n = 0
        b = list()
        for i in s:
            if (i =="(") or (i == "[") or (i == "{"):
                p += 1
            if i in o:
                b.append(i)
            try:
                if i in f and i == all[b[-1]]:
                    n += 1
                    b.pop()
                elif i in f and i != all[b[-1]]:
                    return False
            except:
                return False


        if p == n:
            return (True)
        else:
            return (False)
            
#Runtime: 32 ms, faster than 62.18% of Python3 online submissions for Valid Parentheses.
#Memory Usage: 14.4 MB, less than 7.99% of Python3 online submissions for Valid Parentheses.
#0:45
