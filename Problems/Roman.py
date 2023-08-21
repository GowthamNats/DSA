def romanToInt(s: str) -> int:
    roman = {
        'I': 1, 
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    val = 0
    
    for i in range(len(s)):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i+1]]:
            val -= roman[s[i]]
        else:
            val += roman[s[i]]

    return val

def intToRoman(n: int) -> str:
    roman = {
        'I': 1, 
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    vals = list(roman.values())
    keys = list(roman.keys())
    count = len(vals) - 1
    string = ""

    while n > 0:
        if n < vals[count]:
            count -= 1
        else:
            string += keys[count]
            n -= vals[count]
        
    return string

print(romanToInt(intToRoman(689)))