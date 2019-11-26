from django.shortcuts import render
from .models import marks,insurence, age
import psycopg2
from django.http import HttpResponse
import datetime
from datetime import date
# Create your views here.
def index(request):
    return render(request,'index.html')

def result(request):
    if request.method == 'POST':
        data = marks.objects.all()
        eng = request.POST['eng']
        math= request.POST['math']
        sci = request.POST['sci']
        data.ENGLISH = int(eng)
        data.MATHS = int(math)
        data.SCIENCE = int(sci)
        data.TOTAL = ((data.ENGLISH+data.MATHS+data.SCIENCE)/300)*100
        d = round(data.TOTAL)
        dd = ('student got {} %'.format(d))
        e = data.ENGLISH
        m = data.MATHS
        s = data.SCIENCE
        mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='college')
        cursor = mydb.cursor()
        sql = "UPDATE MARKSS SET ENGLISH=%s,MATHS=%s,SCIENCE=%s,PERCENTAGE=%s WHERE id= %s"
        val = (e,m,s,d,1)
        cursor.execute(sql, val)
       # cursor.execute('INSERT INTO markss(ENGLISH,MATHS,SCIENCE,PERCENTAGE) VALUES (%s,%s,%s,%s)',(e,m,s,d))
        mydb.commit()
        mydb.close()
        return render(request,'index.html',{'dd':dd,'e':e, 'm':m, 's':s})
    return HttpResponse('not worked')

def insurenc(request):
    if request.method=="POST":
        name = request.POST['name']
        da = request.POST['date']
        dat = insurence.objects.all()
        dat.NAME = name
        dat.DATE = da
        mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='college')
        cursor = mydb.cursor()
        sql = "UPDATE insurence SET NAME = %s, DATE = %s WHERE id= %s"
        val = (name, da, 1)
        cursor.execute(sql, val)
        mydb.commit()
        mydb.close()

        b = (da.split('-'))
        year2 = int(b[0])
        month2 = int(b[1])
        dat = int(b[2])

        c = datetime.datetime(year2, month2, dat)
        date2 = int(c.strftime("%d"))
        month2 = int(c.strftime("%m"))
        year2 = int(c.strftime("%Y"))

        a = datetime.datetime.now()
        date1 = int(a.strftime("%d"))
        month1 = int(a.strftime("%m"))
        year1 = int(a.strftime("%Y"))

        if (month1==month2) and (year1==year2):
            days = date1 - date2
            if days<=5:
                last = ('Dear {} your insurence will expire in {} days'.format(name,days))
                return render(request, 'index.html', {'last': last,'n':name,'da':da})
            elif days==1:
                 last = ('Dear {} this is last day of insurence'.format(name))
                 return render(request, 'index.html', {'last': last,'n':name,'da':da})
            else:
                last = ('Dear {} your insurence will expire in {} days'.format(name,days))
                return render(request, 'index.html', {'last': last,'n':name,'da':da})
        else:
            mont = month1-month2
            last = ('Dear {} your insurence will expire in {} month(s)'.format(name, mont))
            return render(request, 'index.html', {'last': last,'n':name,'da':da})
    return HttpResponse('DEBUG')

def age(request):
    if request.method =='POST':
        age = request.POST['date']
        mydb = psycopg2.connect(host='localhost', user='postgres', password='pavanyadav123', database='college')
        cursor = mydb.cursor()
        sql = "UPDATE age SET DATE_OF_BIRTH = %s WHERE id= %s"
        val = (age, 1)
        cursor.execute(sql, val)
        mydb.commit()
        mydb.close()

        v = age.split('-')
        year1 = int(v[0])
        month1 = int(v[1])
        date1 = int(v[2])
        dat = datetime.datetime(year1,month1,date1)
        d1 = int(dat.strftime('%d'))
        m1 = int(dat.strftime('%m'))
        y1 = int(dat.strftime('%Y'))

        dat2 = datetime.datetime.now()
        d2 = int(dat2.strftime('%d'))
        m2 = int(dat2.strftime('%m'))
        y2 = int(dat2.strftime('%Y'))

        b1 = d2-d1
        b2 = m2-m1
        b3 = y2-y1

        a = ('You are {} years,{} months,{} days old'.format(b3,b2,b1))
        return render(request, 'index.html', {'a':a,'age': age})

