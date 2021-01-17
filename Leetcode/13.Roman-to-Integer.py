class Solution:
    def romanToInt(self, s: str) -> int:
        symb = {"I" : 1, 
        "V" : 5, 
        "X" : 10, 
        "L" : 50, 
        "C" : 100, 
        "D" : 500, 
        "M" : 1000
        }
        
        num = 0
        roman = list(s)
        
        i = 0
        while i < len(roman):
            try:
                if roman[i] == "I" and (roman[i+1] == "V" or roman[i+1] == "X"):
                    num += symb[roman[i+1]] - 1
                    i += 2
                elif roman[i] == "X" and (roman[i+1] == "L" or roman[i+1] == "C"):
                    num += symb[roman[i+1]] - 10
                    i += 2
                elif roman[i] == "C" and (roman[i+1] == "D" or roman[i+1] == "M"):
                    num += symb[roman[i+1]] - 100
                    i += 2
                else:
                    num += symb[roman[i]]
                    i += 1
            except:
                num += symb[roman[i]]
                i += 1


        return (num)
 
 
 
 
 
 
#Took me 1 hr to accomplish
