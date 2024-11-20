import time, mysql.connector as con 
 
print(''' _ _ _ 
|LOGIN| 
 ‾‾‾‾‾ 
Please login to access the database system.\n''') 
username=input("Enter your username: ") 
password=input("Enter your password: ") 
time.sleep(1) 
db=con.connect(host='localhost',user=username,password=password) 
if db.is_connected(): 
    print("\nLogged In successfully!") 
else: 
    print("Please check your details once again.") 
 
def connected(): 
  db=con.connect(host='localhost',user=username,password=password) 
  if db.is_connected(): 
    print("\nConnection is successfully established.") 
  else: 
    print("No, connection failed to connect.") 
       
def createDatabase(): 
  db=con.connect(host='localhost',user=username,password=password) 
  cur=db.cursor() 
  ds=input("Enter name of your database: ") 
  cur.execute("create database {}".format(ds)) 
  db.commit() 
  db.close() 
 
def createTable(): 
   
  db=con.connect(host='localhost',user=username,password=password,database=ds) 
  cur=db.cursor() 
  table=input("Enter name of your table: ") 
  cur.execute("create table {}(eno int(5),name varchar(30),age int(3),salary float(9,2),allowance float(9,2),doj date,department varchar(15),designation varchar(15),address varchar(30))".format(table)) 
  db.commit() 
  db.close() 
 
def createSalTable(): 
   
  db=con.connect(host='localhost',user=username,password=password,database=ds) 
  cur=db.cursor() 
 
  table=input("Enter name of your table: ") 
  cur.execute("create table {}(eno int(5), epf int(5),insurance int(5),proftax int(5))".format(table)) 
  db.commit() 
  db.close() 
 
def salinsert(): 
  db=con.connect(host='localhost',user=username,password=password,database=ds) 
  cur=db.cursor() 
  table=input("Enter name of your employee table : ") 
  eno=int(input("Enter the eno of employee: ")) 
  cur.execute("select * from {}".format(table)) 
  r=cur.fetchall() 
  for i in r: 
       if i[0]==eno: 
          sal=i[3] 
  table1=input("Enter name of your deduction table: ") 
  epf=sal*(12/100) 
  insurance=int(input("Enter insurance of employee: ")) 
  pt=int(input("Enter Professional Tax(%) of employee: ")) 
  prof=sal*(pt/100) 
  cur.execute("insert into {} values({},{},{},{})".format(table1,eno,epf,insurance,prof)) 
  db.commit() 
  db.close() 
 
def grosssal(): 
   
  db=con.connect(host='localhost',user=username,password=password,database=ds) 
  cur=db.cursor() 
  table1=input("Enter name of your first table to be joined: ") 
  table2=input("Enter the name of your second table to be joined: ") 
  cur.execute("select {}.eno,{}.name,({}.salary+{}.allowance)({}.epf+{}.insurance+{}.proftax) 'gross salary' from {},{} where {}.eno={}.eno".format(table1,table1,table1,table1,table2,table2,table2,table1,table2,table1,table2)) 
  r=cur.fetchall() 
  print("x","-"*80,"x") 
  print("\t Eno\t\t\tName of Employee\t\tGross Salary") 
  print("x","-"*80,"x") 
  for i in r: 
    print("\t",i[0],"\t\t\t",i[1],"\t\t\t",i[2]) 
    print("x","-"*80,"x") 
  db.commit() 
  db.close() 
 
def insert(): 
   
 
  db=con.connect(host='localhost',user=username,password=password,database=ds) 
  cur=db.cursor() 
  table=input("Enter name of your table: ") 
  eno=int(input("Enter Eno of employee: ")) 
  name=input("Enter Name of employee: ") 
  age=input("Enter Age of employee: ") 
  sal=int(input("Enter Salary of employee: ")) 
  allowance=int(input("Enter Special Allowances of employee: ")) 
  doj=input("Enter Date of Joining of employee (YYYY-MM-DD): ") 
  department=input("Enter Department of employee: ") 
  designation=input("Enter Designation of employee: ") 
  address=input("Enter Address of employee: ") 
  cur.execute("insert into {} values({},'{}',{},{},{},'{}','{}','{}','{}')".format(table,eno,name,age,sal,allowance,doj,department,designation,address)) 
  db.commit() 
  db.close() 
 
def update(): 
   
  db=con.connect(host='localhost',user=username,password=password,database=ds) 
  cur=db.cursor() 
  table=input("Enter name of your table: ") 
  eno=int(input("Enter eno of employee: ")) 
  msg='''\nWhat do you want to update : 
 
1. Update Name 
2. Update Salary 
3. Update Age 
4. Update Date of Joining 
5. Update Department 
6. Update Designation 
7. Update Address 
8. Update Insurance (deduction table) 
9. Update ProfTax % (deduction table) 
 
 Enter your choice: ''' 
  r=int(input(msg)) 
  if r==1: 
    name=input("Enter name of employee: ") 
    cur.execute("update {} set name='{}' where eno={}".format(table,name,eno)) 
    db.commit() 
    db.close() 
  elif r==2: 
    sal=int(input("Enter salary of employee: ")) 
    cur.execute("update {} set salary={} where eno={}".format(table,sal,eno)) 
    db.commit() 
    db.close() 
 
  elif r==3: 
    age=input("Enter age of employee: ") 
    cur.execute("update {} set age={} where eno={}".format(table,age,eno)) 
    db.commit() 
    db.close() 
  elif r==4: 
    doj=input("Enter Date of joining of employee: ") 
    cur.execute("update {} set doj='{}' where eno={}".format(table,doj,eno)) 
    db.commit() 
    db.close() 
  elif r==5: 
    department=input("Enter department of employee: ") 
    cur.execute("update {} set department='{}' where eno={}".format(table,department,eno)) 
    db.commit() 
    db.close() 
  elif r==6: 
    designation=input("Enter designation of employee: ") 
    cur.execute("update {} set designation='{}' where eno={}".format(table,designation,eno)) 
    db.commit() 
    db.close() 
  elif r==7: 
    address=input("Enter address of employee: ") 
    cur.execute("update {} set address='{}' where eno={}".format(table,address,eno)) 
    db.commit() 
    db.close() 
  elif r==8: 
    insurance=int(input("Enter insurance of employee: ")) 
    cur.execute("update {} set insurance='{}' where eno={}".format(table,insurance,eno)) 
    db.commit() 
    db.close() 
  elif r==9: 
    pt=int(input("Enter Professional Tax(%) of employee: ")) 
    prof=sal*(pt/100) 
    cur.execute("update {} set address='{}' where eno={}".format(table,prof,eno)) 
    db.commit() 
    db.close() 
  else: 
    print("Enter a suitable option.") 
 
def delete(): 
   
  db=con.connect(host='localhost',user=username,password=password,database=ds) 
  cur=db.cursor() 
 
  table=input("Enter name of your table: ") 
  eno=int(input("Enter eno of employee: ")) 
  cur.execute("delete from {} where eno={}".format(table, eno)) 
  db.commit() 
  db.close() 
   
def display(): 
   
  db=con.connect(host='localhost',user=username,password=password,database=ds) 
  cur=db.cursor() 
  table=input("Enter name of your table: ") 
  cur.execute("select * from {}".format(table)) 
  r=cur.fetchall() 
  for i in r: 
    for j in i: 
      print(j,end=" ") 
  print() 
  db.commit() 
  db.close() 
 
mssg=''' 
 ==================================== 
| Employee Database Management System | 
 ==================================== 
1. Create a new Database 
2. Create Employee table 
3. Insert a Employee record 
4. Create Deductions Table 
5. Insert Deduction record 
6. Display records from given table 
7. Update a record from given table 
8. Delete a record from given table 
9. Calculate Gross Salary of employees 
10. Check if connection is established or not 
11. Exit the system 
 
Enter your choice: ''' 
ch='Y' 
time.sleep(2) 
c=input("\nDo you want to work on existing database? Y/N : ") 
if c in"Yy": 
    ds=input("Enter name of your existing database: ") 
while ch in "Yy": 
    n=int(input(mssg)) 
    if n==1: 
        db=con.connect(host='localhost',user=username,password=password) 
        cur=db.cursor() 
        ds=input("Enter name of your database: ") 
 
        cur.execute("create database {}".format(ds)) 
        db.commit() 
        db.close() 
    elif n==2: 
        createTable() 
    elif n==3: 
        insert() 
    elif n==4: 
        createSalTable() 
    elif n==5: 
        salinsert() 
    elif n==6: 
        display() 
    elif n==7: 
        update() 
    elif n==8: 
        delete() 
    elif n==9: 
        grosssal() 
    elif n==10: 
        connected() 
    elif n==11: 
        print("Thanks for using!") 
        break 
    else: 
        print("Enter a suitable option.") 
    ch=input("\nDo you want to continue? Y/N: ")
