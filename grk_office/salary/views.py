from django.shortcuts import render
from .models import Salary,monthly_salary
from main.models import Person
import time,psycopg2,os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

total = 0
year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())

# Create your views here.
def show_salary(request):
    people=Person.objects.filter(status='yes')
    sal = Salary.objects.all()
    #print(type(people))
    return render(request,'salary.html',{'lists' : sal,'rowlist.append(salloyees' : people,'c_year' : int(year)})

def monthly(request):    
    req_month = request.POST['current_month']
    req_year = int(request.POST['current_year'])
    total = int(request.POST['present'])
    emp_det = []
    print(req_month)
    try:
        connection = psycopg2.connect(user="postgres",password="1234",port="5432",database="office_database")
        cursor = connection.cursor()
        query = "select * from salary_monthly_salary where month = %s and year = %s"
        cursor.execute(query,(req_month,req_year))
        records = cursor.fetchall()
        print(2)
        print(records)
        for row in records:
            print(row)
            rowlist = []
            tot_sal = 0
            sal = Salary.objects.get(person_id= row[2])
            rowlist.append(sal.person.name)
            rowlist.append(round((sal.basicpay * int(row[1])/int(total)),2))
            rowlist.append(round((sal.hra * int(row[1])/int(total)),2))
            rowlist.append(round((sal.transport * int(row[1])/int(total)),2))
            rowlist.append(round((sal.medical * int(row[1])/int(total)),2))
            rowlist.append(round((sal.prof_update * int(row[1])/int(total)),2))
            rowlist.append(round((sal.special_allowance  * int(row[1])/int(total)),2))          
            rowlist.append(round((sal.prof_tax * int(row[1])/int(total)),2))
            rowlist.append(round((sal.variable_pay * int(row[1])/int(total)),2))
            rowlist.append(round((sal.PF * int(row[1])/int(total)),2))
            rowlist.append(round((sal.ESI * int(row[1])/int(total)),2))
            tot_sal = sal.basicpay * int(row[1])/int(total) + sal.hra * int(row[1])/int(total)+sal.transport * int(row[1])/int(total)+sal.medical * int(row[1])/int(total)+sal.prof_update * int(row[1])/int(total)+sal.special_allowance  * int(row[1])/int(total)+sal.prof_tax * int(row[1])/int(total)+sal.variable_pay * int(row[1])/int(total)+sal.PF * int(row[1])/int(total)+sal.ESI * int(row[1])/int(total)
            rowlist.append(round(tot_sal,2))
            emp_det.append(rowlist)
        #print(emp_det)

    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
        df = pd.DataFrame(emp_det,columns=['Person','Basic Pay','HRA','Transport Allowance','Medical Allowance','Profesional Update','Special Allowance','Professional Tax','Variable Pay','PF','ESI','Total'])
        df.to_excel("D:/Acad/djangoprojects/grk_office/excel_sheets/"+req_month + "_" + str(req_year) + "_Salary_Details.xlsx")
    return render(request,'month_sal.html',{'lists' : emp_det})