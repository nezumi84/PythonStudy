#Mathplot 라이브러리, 데이터 프레임 라이브러리 호출
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
#자동차 색상의 선호도에 대한 도수분포표
data = {'Preference':[180,60,75,45,50,90]}
#DATE 라벨 LIST 생성 데이터 프레임 생성하면서 라벨도 같이 입력
ColorCategory = ['White','Black','Silve','Red','DarkGreen','Gray']
dataTable = DataFrame(data, columns=['Preference'], index=ColorCategory)
dataTable.plot(kind = 'bar')
plt.show()