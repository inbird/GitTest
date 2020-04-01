# 웹 크롤링을 통한 시각화
# conda install beautifulsoup4, selenium

from bs4 import BeautifulSoup
from selenium import webdriver  #chrome webdriver 다운로드 필요
from openpyxl import Workbook
import time

# 웹 크롤링 수행 후 엑셀에 저장
"""
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(3)
result_list = []

for i in range(1,11):
    print( i, "페이지")    
    driver.get( "https://www1.president.go.kr/petitions/best?page=" + str(i) )
    html = driver.page_source
    soup = BeautifulSoup( html, 'html.parser' )

    for j in soup.select("#cont_view > div.cs_area > div > div > div.board.text > div.b_list.category > div.bl_body > ul > li"):
        #print( i.text )
        print( j.find("div", class_ = "bl_subject" ).text[3:].strip() )
        result_list.append( j.find("div", class_ = "bl_subject" ).text[3:].strip() )
    time.sleep(3)
    
driver.close()

write_workbook = Workbook()
write_cell = write_workbook.active
for i in range(1, len(result_list) + 1 ):
    write_cell.cell( i, 1, result_list[i-1] )

write_workbook.save("blue.xlsx")    
write_workbook.close()



# 엑셀에 저장된 결과값 조회

from openpyxl import load_workbook

read_workbook = load_workbook("./blue.xlsx")
read_cell = read_workbook.active
write_list = []

for i in range(1, 150) :
    write_list.append( read_cell.cell(i,1).value )
#print( write_list )    

for i in write_list:
    print(i)
"""

# 자연어 분석
#JDK설치 후 Anaconda Prompt 오픈
#conda install -c conda-forge jpype1
#pip install konlpy

from konlpy.tag import Kkma

kkma = Kkma()
print( kkma.sentences("네 안녕하세요. 반갑습니다. 저는 회사에 다닙니다") )

















