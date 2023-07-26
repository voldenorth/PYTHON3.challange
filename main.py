import pandas as pd 



file_path='D:\data analis\data saham\stock_18_juli_2023.csv'
#load csv file

df=pd.read_csv(file_path)


                 
#mengganti missing value dengan 0
df=df.fillna(0)

#mencari harga saham dengan rumus graham number 
#22.5 adalah 1.5 pbv X 15 per 
#1.5 dan 15 adalah batas maksimal pbv & per

df['harga_wajar']=(22.5*df['bvps']*df['eps'])**(1/2)
df['harga_wajar']=df['harga_wajar'].round(2) #membulatkan decimal menjadi 2 angka dibelakang koma




#menghitung potensi keuntungan 
df['pot_gnl']=((df['harga_wajar']-df['harga'])/df['harga'])*100
df['pot_gnl']=df['pot_gnl'].round(2)


#membandingka return saham dengan return IHSG

IHSG_3m=0.31
IHSG_6m=(-0.08)
IHSG_ytd=(-0.30)

m3=df['3m_return']>IHSG_3m
m6=df['6m_return']>IHSG_6m
ytd=df['ytd_return']>IHSG_ytd
hasil=[m3,m6,ytd]
df['buy_or_no']=m3&m6&ytd

print(df.columns)
#filtered dataframe
df_feature=['saham','harga','deviden_yield','harga_wajar','pot_gnl','buy_or_no']
df=df[df_feature]

df=df[df['buy_or_no']==True]
df=df[df['pot_gnl']>0]














