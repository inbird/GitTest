# Web Driver 활용
from bs4 import BeautifulSoup
from selenium import webdriver  #chrome webdriver 다운로드 필요
import time

result_list = []

"""    
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(3)


#driver.get("http://www.naver.com")

driver.get( "https://www1.president.go.kr/petitions/best?page=1" )
html = driver.page_source 
#print( html )

soup = BeautifulSoup( html, 'html.parser' )
for d in soup.select("#cont_view > div.cs_area > div > div > div.board.text > div.b_list.category > div.bl_body > ul > li"):
    result_list.append( d.find("div", class_ = "bl_subject" ).text[3:].strip() )

time.sleep(1)
driver.close()

"""

# Request 객체 활용
import requests
from bs4 import BeautifulSoup

req = requests.get( "https://www1.president.go.kr/petitions/best?page=1" )
html = req.text
soup = BeautifulSoup(html, 'html.parser')

for d in soup.select("#cont_view > div.cs_area > div > div > div.board.text > div.b_list.category > div.bl_body > ul > li"):
    #print( "Tot Text : ", d.text )
    #print( "Title : " , d.find("div", class_ = "bl_subject" ).text )
    #print( "Clean : " ,  d.find("div", class_ = "bl_subject" ).text[3:].strip() )
    result_list.append( d.find("div", class_ = "bl_subject" ).text[3:].strip() )



print( result_list )



"""
# 자연어 분석
#JDK설치 후 Anaconda Prompt 오픈
#conda install -c conda-forge jpype1
#pip install konlpy

from konlpy.tag import Kkma

kkma = Kkma()
print( kkma.sentences("네 안녕하세요. 반갑습니다. 직업은 뭐예용? 저는 회사에 다닙니다") )
print( kkma.nouns("우리는 민족중흥의 역사적 사명을 띠고 이땅에 태어났을까? 아니면 커피 혹은 우유") )
"""

"""
# 단어개수 세기
from konlpy.tag import Kkma
import collections
kkma = Kkma()

list_a = ["가","라","다","가","나","라","마"]
list_b = ["가","다","나","나","가","다","다","다"]
list_c = list_a + list_b
for k, v in collections.Counter(list_c).items() :
    print(k,'는', v , '번 존재합니다')

print( collections.Counter(list_c).most_common(3) )

sentence_list = [
        "우리  축구 야구 축구 축구",
        "우리는 민족중흥의 성악설 역사적 사명을 띠고 축구 이땅에 태어났다",
        "우리 나라 말씀이 중국과 성악 달라 고생이 많다 축구나 할까.",
        "우리 오늘 저녁은 간단하게 깁밥, 라면, 떡볶이, 축구 순대, 어묵, 돈까스로",
        "공자 김밥 맹자 순자 성선설 성악설 종교 예수 성악설 석가",
        "우리 라면, 성악설 떡볶이, 순대, 어묵 예수 석가",
        "우리는 김밥 중국 미국 민족의 역사를 사명, 역사와 축구 사명, 역사, 성악설"
        ]
result_list = []
for i in sentence_list :
    #print( kkma.nouns( i ) )
    result_list += kkma.nouns( i )

print( collections.Counter(result_list).most_common(5) )
"""

# 데이터시각화
import numpy as np
import matplotlib.pyplot as plt

plt.bar( ["Andy","Chris","Chalie","Bobby"], [70,42,120,80])
plt.title( "Team Weight" )
plt.xlabel( "Name" )
plt.ylabel( "Weight" )

plt.show()



# wordcloud 사용
# conda install -c conda-forge wordcloud
# 취임사 내용 기반 워드클라우드

import matplotlib.pyplot as plt
from wordcloud import WordCloud

file_name = ['2003(No).txt', '2008(Lee).txt', '2013(Park).txt', '2017(Mun).txt']

# 1) 워드 클라우드 기능 이용

# text = open( '2003(No).txt' ).read()
# wc = WordCloud(font_path='./malgun.ttf', background_color="white").generate(text)
# fig = plt.figure( figsize=(14,14) )
# plt.imshow(wc, interpolation='bilinear')
# plt.axis('off')
# plt.show()

# for i in range(0, len( file_name )) :
#     print( "파일명 : ", file_name[i] )
#     text = open( file_name[i] ).read()
#     wc = WordCloud(font_path='./malgun.ttf', background_color="white").generate(text)
#     fig = plt.figure( figsize=(14,14))
#     plt.imshow(wc, interpolation='bilinear')
#     plt.axis('off')
#     plt.show()

# 2) konlpy 기능 이용
parse_list = []
final_text = ""

for i in range(0, len( file_name )) :
    print( "파일명 : ", file_name[i] )
    text = open( file_name[i] ).read()
    list_sentence = kkma.sentences(text)
    parse_list = []
    final_text = ""
    for i in list_sentence:
        parse_list += [ s for s in kkma.nouns( i ) if len(s) > 1 ]
        for i, s in enumerate(parse_list) :
            final_text = final_text + " " + s
    wc1 = WordCloud(font_path='./malgun.ttf', background_color="white").generate(final_text)
    fig = plt.figure( figsize=(14,14))
    plt.imshow(wc1, interpolation='bilinear')
    plt.axis('off')
    plt.show()