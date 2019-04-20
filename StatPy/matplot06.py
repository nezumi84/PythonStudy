import math
#통계학개론 수강생들의 40명의
data =[184,167,164,155,180,176,168,160,161,157,
       180,183,170,170,185,170,165,170,168,154,
       173,152,173,165,163,160,163,178,151,171,
       168,163,165,178,165,170,168,187,150,174]

#최소값 구하기
minvalue = min(data)
maxvalue = max(data)
#계층 및 최초 시작점 정하기
rank = 6
rangeValue = math.ceil((maxvalue - minvalue)/rank)
startPoint = minvalue - (1/2 * 1)

rankArray = []
rankValueArray =[0,0,0,0,0,0]
accumvalue = startPoint

#계층별 시작점 정해서 list에 입력
for x in range(6):
    rankArray.append(accumvalue)
    accumvalue = accumvalue + rangeValue
count = 1
#자료의 도수정리
for x in range(len(data)):
    for y in range(len(rankArray)):
        minLimit = rankArray[y]
        maxLimit = rankArray[y] + rangeValue
        if float(data[x]) >= minLimit and float(data[x]) < maxLimit:
            rankValueArray[y] = rankValueArray[y] + 1

#자료의 출력
print(data)
#계층별 범위출력
print(rankArray)
#계층별 도수집계 출력
print(rankValueArray)
