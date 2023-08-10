import pandas as pd


df=pd.read_csv('adult.data.csv')
print(df.head())



#race count
race_count=pd.Series(df['race'].value_counts())


#average age of male
avg_age_male=df[df['sex']=='Male']['age'].mean()


#peercentage of people who have a bachelor degree
bachelor_degree=(df['education']=='Bachelors').mean()*100


#percentage people with advanced education (bachelors,masters,doctorate) make more than 50k
adv_education=['Bachelors','Masters','Doctorat']
num_adv_education=df[df['education'].isin(adv_education)]
num_non_adv=df[~df['education'].isin(adv_education)]
num_non_adv2=(~df['education'].isin(adv_education)).value_counts()


percentage_adv_education=round((num_adv_education['salary']=='>50K').mean()*100)

percentage_non_adv=round((num_non_adv['salary']=='>50K').mean()*100)

#minimun number of hours a person work per week

min_hours_per_week=df['hours-per-week'].min()

min_hours_higf_salary=(df[df['hours-per-week']==min_hours_per_week]['salary']=='>50K').mean()*100

#identify the country with the highest percentage of >50k earners and the percentage
country_high_salary=df[df['salary']=='>50K']['native-country'].value_counts(normalize=True).idxmax()
percentage_high_salary_country=round(df[df['native-country']==country_high_salary]['salary'].value_counts(normalize=True)['>50K']*100)

#identify the most popular occupation for >50K earners in india
indian_high_salary_data=df[(df['native-country']=='india')&(df['salary']=='>50K')]
if indian_high_salary_data.empty:
    print('indian has not >50K salary')
else:
    indian_high_salary_occupations=indian_high_salary_data['occupation'].value_counts().idxmax()
    print(indian_high_salary_occupations)







