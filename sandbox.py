#compound interest

#How many Hydra will I have depending on how I feed them?

#input starting number
s=10

#number of weeks
w=1

#input feedings per week
f=3

#exponential factor
e=f*2

#rate of hydra buds
r=2

#bud frequency in a week
b=2

#number of Hydra after x week

hymulti=(s*(1+(r/b)))**(b*w)
print(hymulti)