#Mathplot 라이브러리, 데이터 프레임 라이브러리 호출
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame
#자동차 색상의 선호도에 대한 도수분포표
data = {'Preference':[180,60,75,45,50,90]}
#총 합계구하기
total = sum(data['Preference'])
#numpy로 도수를 합계로 나눔 (상대도수 구하기)
reldatas = np.divide(data['Preference'],total)
#DATE 라벨 LIST 생성 데이터 프레임 생성하면서 라벨도 같이 입력
ColorCategory = ['White','Black','Silve','Red','DarkGreen','Gray']

plt.pie(
    # using data total)arrests
    reldatas,
    # with the labels being officer names
    labels=ColorCategory,
    # with no shadows
    shadow=False
    )
# View the plot drop above
plt.axis('equal')
plt.title('Pie Chart')
# View the plot
plt.tight_layout()
plt.show()