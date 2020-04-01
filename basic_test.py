# 소수 구하기
def getPrime(x):
    for i in (2, x-1):
        if( x % i == 0 ):
            break        
    else :
        return x
    
list1 = [117,119,16]
ret = filter( getPrime, list1 )
print( list(ret) )

# 문자열
str1 = 'aAbBcCdD'

print( len(str1) )  #문자열길이
print( str1[::2] )  #홀수번째 문자열
print( str1[::-1] )  #문자열 뒤집기
print( str1.count('aA') )  #문자열개수
print( str1.find('cC') )  #문자열위치
print( str1.replace('a','Z') )  #문자열치환
print( str1.isalpha() )  #알파벳여부, isdigit(), isalnum(), upper(), lower(), strip()
print( ''.join( sorted(str1)) , ''.join( sorted(str1, reverse=True ) ) ) #문자열 정렬

from urllib.request import urlopen
url = 'https://www.python.org'
with urlopen(url) as f:
    doc = f.read().decode()
    print(doc)





