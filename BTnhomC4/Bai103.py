def date(day, month, year):
    if (day*month)%100==year%100:
        return True
    else:
        return False
for year in range(1900,2000):
    if year%4==0:
        for month in range(1,13):
            if month==2:
                for day in range(1,30):
                    if date(day, month, year):
                        print(day,'/',month,'/',year,sep='')
    else:
        for month in range(1,13):
            if month==2:
                for day in range(1,29):
                    if date(day, month, year):
                        print(day,'/',month,'/',year,sep='')
            else:
                for day in range(1,32):
                    if date(day, month, year):
                        print(day,'/',month,'/',year,sep='')