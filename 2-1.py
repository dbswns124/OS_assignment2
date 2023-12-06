
# 1번 문제
print("OSS 과제 2-1, 문제(1)")
import pandas as pd
from pandas import Series,DataFrame
td = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
df = pd.DataFrame(td)
# 안타기반
print('안타 top 10, 2015~2018')
for j in range (4):
    df2=df[df['year']==(2015+j)][['batter_name','H']]
    df3=df2.sort_values(by='H',ascending=False)
    print()
    print(2015+j)
    for i in range (10):
        print(df3.iloc[i]['batter_name'])

# 타율 기반

print('\n\n타율 top 10 2015~2018')
for j in range (4):
    df2=df[df['year']==(2015+j)][['batter_name','avg']]
    df3=df2.sort_values(by='avg',ascending=False)
    print()
    print(2015+j)
    for i in range (10):
        print(df3.iloc[i]['batter_name'])

# 홈런
print('\n\n홈런 top 10 2015~2018')
for j in range (4):
    df2=df[df['year']==(2015+j)][['batter_name','HR']]
    df3=df2.sort_values(by='HR',ascending=False)
    print()
    print(2015+j)
    for i in range (10):
        print(df3.iloc[i]['batter_name'])

# 출루율
print('\n\n출루율 top 10 2015~2018')
for j in range (4):
    df2=df[df['year']==(2015+j)][['batter_name','OBP']]
    df3=df2.sort_values(by='OBP',ascending=False)
    print()
    print(2015+j)
    for i in range (10):
        print(df3.iloc[i]['batter_name'])


# 2번문제
print("\n\nOSS 과제 2-1, 문제(2)")

df = pd.DataFrame(td)
#포수
print('\n2018 포수 승리기여도 가장 높은 선수')
df2=df[df['year']==2018][['war','cp','batter_name']]
ans1=df2[df2['cp']=='포수']
ans1.sort_values(by='war')
print(ans1.iloc[len(ans1)-1]['batter_name'])
# 1루수
print('\n2018 1루수 승리기여도 가장 높은 선수')
df2=df[df['year']==2018][['war','cp','batter_name']]
ans1=df2[df2['cp']=='1루수']
ans1.sort_values(by='war')
print(ans1.iloc[len(ans1)-1]['batter_name'])
#2루수
print('\n2018 2루수 승리기여도 가장 높은 선수')
df2=df[df['year']==2018][['war','cp','batter_name']]
ans1=df2[df2['cp']=='2루수']
ans1.sort_values(by='war')
print(ans1.iloc[len(ans1)-1]['batter_name'])
#3루수
print('\n2018 3루수 승리기여도 가장 높은 선수')
df2=df[df['year']==2018][['war','cp','batter_name']]
ans1=df2[df2['cp']=='3루수']
ans1.sort_values(by='war')
print(ans1.iloc[len(ans1)-1]['batter_name'])
#유격수
print('\n2018 유격수 승리기여도 가장 높은 선수')
df2=df[df['year']==2018][['war','cp','batter_name']]
ans1=df2[df2['cp']=='유격수']
ans1.sort_values(by='war')
print(ans1.iloc[len(ans1)-1]['batter_name'])
#좌익수
print('\n2018 좌익수 승리기여도 가장 높은 선수')
df2=df[df['year']==2018][['war','cp','batter_name']]
ans1=df2[df2['cp']=='좌익수']
ans1.sort_values(by='war')
print(ans1.iloc[len(ans1)-1]['batter_name'])
#중견수
print('\n2018 중견수 승리기여도 가장 높은 선수')
df2=df[df['year']==2018][['war','cp','batter_name']]
ans1=df2[df2['cp']=='중견수']
ans1.sort_values(by='war')
print(ans1.iloc[len(ans1)-1]['batter_name'])
#우익수
print('\n2018 우익수 승리기여도 가장 높은 선수')
df2=df[df['year']==2018][['war','cp','batter_name']]
ans1=df2[df2['cp']=='우익수']
ans1.sort_values(by='war')
print(ans1.iloc[len(ans1)-1]['batter_name'])


#3번 문제

print("\n\nOSS 과제 2-1, 문제(3)")

import pandas_datareader.data as web
df = pd.DataFrame(td)
all_data = df[['R','H','HR','RBI','SB','war','avg','OBP','SLG','salary']]
result=all_data.corr()
df1 = pd.DataFrame(result)
max=0.0
max_val=0.0
for i in range (len(df1) -1):

    if df1.iloc[i]['salary'] > max_val:
        max_val=df1.iloc[i]['salary']
        max=i
print("max_correlation  : ", max_val)
print("max_coreelation with salary : ",df1.columns[max])