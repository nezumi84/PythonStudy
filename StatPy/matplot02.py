#Mathplot 라이브러리, 데이터 프레임 라이브러리 호출
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
#4월 8일 KDI 경제동향 2019.4 를 기반으로 데이터 입력
datas = {'AllIndustry':[2.5, 1.4, 1.8, -0.1, 2.6,0, 0.8,-1.4,0],
           'Industry':[2.4, 1.3, 2.0,  0.1, 4.3,0,-0.2,-2.7,0],
           'Service' :[1.9, 2.1, 2.2,  0.8, 2.7,0, 2.3, 0.0,0],
           'Retail': [1.9, 4.3, 5.0,  3.8, 3.0,0, 4.1,-2.0,0]}

#DATE 라벨 LIST 생성 데이터 프레임 생성하면서 라벨도 같이 입력
date = ['2017', '2018', '2018-ii', '2018-iii', '2018-iv','2019-i','2019-1','2019-2','2019-3']
MajorEcoIdx = DataFrame(datas, columns=['AllIndustry', 'Industry', 'Service', 'Retail'], index=date)

#데이터 프레임 출력
print(MajorEcoIdx)
#그림크기 12 인치 5 인치 사이즈로 생성
fig = plt.figure(figsize=(12,5))

plt.rcParams['lines.linewidth'] = 2 #선의두께
plt.rcParams['lines.color'] = 'r' #선의색상
plt.rcParams['axes.grid'] = True #그리드 여부

plt.plot(MajorEcoIdx['AllIndustry'], label = 'All Industry' ) #AllIndustry 선 그리기
plt.plot(MajorEcoIdx['Industry'], label = 'Industry Production') #Industry 선 그리기
plt.plot(MajorEcoIdx['Service'], label = 'Service Production') #Service 선 그리기
plt.plot(MajorEcoIdx['Retail'], label = 'Retail Production') #Retail 선 그리기
plt.ylabel('Year-on-Year % Change') # y축 라벨 그리기
plt.xlabel('Quarter') #x축 라벨 그리기
plt.title('Major Economic Indicators') #제목 그리기
plt.legend(loc="best") #범례를 최상의 장소에 이동하여 보이기
plt.show() #그래프 화면에 표시