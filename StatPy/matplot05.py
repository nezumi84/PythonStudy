#Mathplot 라이브러리, 데이터 프레임 라이브러리 호출
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame
#불량항목별 불량품의 수 (SCRAP GOODS)
data = {'scrap':[150,72,51,18,9]}
#총 합계구하기
total = sum(data['scrap'])
#numpy로 도수를 합계로 나눔 (상대도수 구하기)
reldatas = np.divide(data['scrap'],total)
#누적상대도수 구하기
accumrel = np.cumsum(reldatas)
#도수변환
accumrelMultiply = np.multiply(accumrel,100)

defects = ['thk','scratch','poor finish','figure','air']
dataTable = DataFrame(accumrelMultiply,index = defects)
dataTable.plot(kind = 'bar')
plt.show()