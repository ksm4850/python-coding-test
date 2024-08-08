# from datetime import *
# today = list(map(int,input().split()))
# d_day = list(map(int,input().split()))

# if today[0] + 1000 < d_day[0]:
#     print('gg')
# elif today[0] + 1000 == d_day[0] and (today[1], today[2]) <= (d_day[1], d_day[2]):
#     print("gg")
# else:
#     today = date(*today)
#     d_day = date(*d_day)
#     print("D-"+str(d_day.toordinal() - today.toordinal()))


from datetime import date
strptime = lambda: date(**{k:int(v) for k,v in zip(['year','month','day'],input().split())})
today, dday = strptime(), strptime()
if dday >= today.replace(today.year+1000):
    print('gg')
else:
    print('D-'+str((dday-today).days))


