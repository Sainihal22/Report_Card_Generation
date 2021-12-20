import mysql.connector as a

def add():
    mydb=a.connect(host="localhost",user="root",password="123456",database="files")
    mycursor=mydb.cursor()
    mycursor.execute("select * from marksheet")
    result=mycursor.fetchall()
    print()
    rollno=int(input("   ENTER THE ROLL NO : "))
    for i in result:
        if i[0]==rollno:
            print("\n  ROLL NO ALREADY EXISTS \n")
            mydb.close()
            break
    else :
        mydb.close()
        mydb=a.connect(host="localhost",user="root",password="123456",database="files")
        mycursor=mydb.cursor()
        sql1="insert into marksheet (ROLL_NO,NAME,ENGLISH,PHYSICS,CHEMISTRY,MATHS,BIOLOGY,COMPUTER) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        rno=rollno
        name=input("\n   ENTER THE STUDENT'S NAME : ")
        eng=float(input("\n   ENTER MARKS IN ENGLISH : "))
        chem=float(input("\n   ENTER MARKS IN CHEMISTRY : "))
        phy=float(input("\n   ENTER MARKS IN PHYSICS : "))
        print("\n \t 1. MATHS and BIO ")
        print("\n \t 2. BIO and COMP ")
        print("\n \t 3. MATHS and COMP \n")
        cho=int(input("  ENTER YOUR CHOICE DEPENDING ON STUDENT's COMBINATION : "))

        if cho>3:
            print("\n  ENTER VALID OPTION \n")
            mydb.close()
        
        else :

            if cho==1:
                maths=float(input("\n   ENTER MARKS IN MATHS : "))
                bio=float(input("\n   ENTER MARKS IN BIOLOGY : "))
                comp=0
                val=(rno,name,eng,phy,chem,maths,bio,comp)
                mycursor.execute(sql1,val)
                mydb.commit()
                    
            elif cho==2:
                bio=float(input("\n   ENTER MARKS IN BIOLOGY : "))
                comp=float(input("\n   ENTER MARKS IN COMPUTER : "))
                maths=0
                val=(rno,name,eng,phy,chem,maths,bio,comp)
                mycursor.execute(sql1,val)
                mydb.commit()
                    
            elif cho==3:
                maths=float(input("\n   ENTER MARKS IN MATHS : "))
                comp=float(input("\n   ENTER MARKS IN COMPUTER : "))
                bio=0
                val=(rno,name,eng,phy,chem,maths,bio,comp)
                mycursor.execute(sql1,val)
                mydb.commit()

            print("\n  *****************************")
            print("\n  ENTERED SUCCESSFULLY !!!!!! \n")
            print("  *****************************")

            mydb.close()

def display():
    print()
    print("\n  CLASS 12 MARKSHEET RECORD !!!!! \n")
    mydb=a.connect(host="localhost",user="root",password="123456",database="files")
    mycursor=mydb.cursor()
    sql1="update marksheet set TOTAL_MARKS=ENGLISH+PHYSICS+CHEMISTRY+MATHS+BIOLOGY+COMPUTER"
    mycursor.execute(sql1)
    mydb.commit()

    sql1="UPDATE MARKSHEET SET AVERAGE=TOTAL_MARKS/5"
    mycursor.execute(sql1)
    mydb.commit()
    sql1="UPDATE MARKSHEET SET GRADES=IF(AVERAGE>= 90 AND AVERAGE<=100 ,'S',IF(AVERAGE>= 80 AND AVERAGE<90 ,'A',IF(AVERAGE>= 70 AND AVERAGE<80 ,'B',IF(AVERAGE >=60 AND AVERAGE <70 ,'C',IF(AVERAGE >=50 AND AVERAGE<60 ,'D',IF(AVERAGE>= 40 AND AVERAGE<50,'E','F'))))))"
    mycursor.execute(sql1)
    mydb.commit()
    mycursor.execute("select * from marksheet order by ROLL_NO ASC")
    result=mycursor.fetchall()
    
    for i in result:
        print("  ROLL NO         : ", i[0])
        print("  NAME            : ", i[1])
        print("  ENGLISH MARKS   : ", i[2])
        print("  PHYSICS MARKS   : ", i[3])
        print("  CHEMISTRY MARKS : ", i[4])

        if (i[5] == 0):
            print("  BIOLOGY MARKS   : ", i[6])
            print("  COMPUTER MARKS  : ", i[7])
        elif (i[6] == 0):
            print("  MATHS MARKS     : ", i[5])
            print("  COMPUTER MARKS  : ", i[7])
        elif (i[7] == 0):
            print("  MATHS MARKS     : ", i[5])
            print("  BIOLOGY MARKS   : ", i[6])

        print("  GRADES          : ", i[10])
        print()
   
    mydb.close()

def search():
    print()
    mydb=a.connect(host="localhost",user="root",password="123456",database="files")
    mycursor=mydb.cursor()
    sql1="update marksheet set TOTAL_MARKS=ENGLISH+PHYSICS+CHEMISTRY+MATHS+BIOLOGY+COMPUTER"
    mycursor.execute(sql1)
    mydb.commit()

    sql1="UPDATE MARKSHEET SET AVERAGE=TOTAL_MARKS/5"
    mycursor.execute(sql1)
    mydb.commit()
    sql1="UPDATE MARKSHEET SET GRADES=IF(AVERAGE>= 90 AND AVERAGE<=100 ,'S',IF(AVERAGE>= 80 AND AVERAGE<90 ,'A',IF(AVERAGE>= 70 AND AVERAGE<80 ,'B',IF(AVERAGE >=60 AND AVERAGE <70 ,'C',IF(AVERAGE >=50 AND AVERAGE<60 ,'D',IF(AVERAGE>= 40 AND AVERAGE<50,'E','F'))))))"
    mycursor.execute(sql1)
    mydb.commit()
    mycursor.execute("select * from marksheet")
    result=mycursor.fetchall()
    rollno=int(input("  ENTER THE ROLL NO TO SEARCH :"))
 
    for i in result:
        if i[0]==rollno:
            print()
            print("  ROLL NO         : ",i[0])
            print("  NAME            : ", i[1])
            print("  ENGLISH MARKS   : ", i[2])
            print("  PHYSICS MARKS   : ", i[3])
            print("  CHEMISTRY MARKS : ", i[4])
            
            if(i[5] == 0):
                print("  BIOLOGY MARKS   : ", i[6])
                print("  COMPUTER MARKS  : ", i[7])
            elif(i[6] == 0):
                print("  MATHS MARKS     : ", i[5])
                print("  COMPUTER MARKS  : ", i[7])
            elif(i[7] == 0):
                print("  MATHS MARKS     : ", i[5])
                print("  BIOLOGY MARKS   : ", i[6])
            
            print("  GRADES          : ", i[10])
                
            break
    else :
        print("\n  NO SUCH RECORD \n")
    mydb.close()
    

def delete():
    print()

    mydb=a.connect(host="localhost",user="root",password="123456",database="files")
    mycursor=mydb.cursor()
    mycursor.execute("select * from marksheet")
    result=mycursor.fetchall()
    
    rollno=int(input("   ENTER THE ROLL NO TO DELETE : "))
    for i in result:
        
        if i[0]==rollno:
            
            sql2="select * from marksheet where roll_no=%s"
            val1=(rollno,)
            mycursor.execute(sql2,val1)
            
            myresult=mycursor.fetchall()
            print()
            
            for i in myresult:
                print("  ROLL NO         : ", i[0])
                print("  NAME            : ", i[1])
                print("  ENGLISH MARKS   : ", i[2])
                print("  PHYSICS MARKS   : ", i[3])
                print("  CHEMISTRY MARKS : ", i[4])

                if (i[5] == 0):
                    print("  BIOLOGY MARKS   : ", i[6])
                    print("  COMPUTER MARKS  : ", i[7])
                elif (i[6] == 0):
                    print("  MATHS MARKS     : ", i[5])
                    print("  COMPUTER MARKS  : ", i[7])
                elif (i[7] == 0):
                    print("  MATHS MARKS     : ", i[5])
                    print("  BIOLOGY MARKS   : ", i[6])

                print("  GRADES          : ", i[10])
            
            print()
            ch=input("  DO YOU WANT TO DELETE THIS RECORD (Y/N) ? : ")
            
            if ch=='y' or ch=='Y':
                sql1="delete from marksheet where roll_no= %s"
                val1=(rollno,)
                mycursor.execute(sql1,val1)
                mydb.commit()
                mydb.close()
                print("\n  DELETED SUCCESSFULLY !!!!!! \n")
            
            else:
                mydb.close()
                print("\n  DATA NOT DELETED \n")
            
            break
    else:
        print("\n  ROLL NO DOESNT EXISTS \n")
        mydb.close()

                
def modify():

    print()
    mydb=a.connect(host="localhost",user="root",password="123456",database="files")
    mycursor=mydb.cursor()
    sql1="UPDATE marksheet set roll_no= %s, name= %s, english=%s, physics=%s, chemistry=%s, maths=%s, biology=%s, computer=%s  where roll_no= %s"
    rollno=int(input("  ENTER THE ROLL NO TO MODIFY : "))
    mycursor.execute("select * from marksheet")
    result=mycursor.fetchall()
    k=0

    for i in result:
        
        if i[0]==rollno:
            k=1
            sql2="select * from marksheet where roll_no=%s"
            val1=(rollno,)
            mycursor.execute(sql2,val1)
            
            myresult=mycursor.fetchall()
            print()
            
            for i in myresult:
                print("  ROLL NO         : ", i[0])
                print("  NAME            : ", i[1])
                print("  ENGLISH MARKS   : ", i[2])
                print("  PHYSICS MARKS   : ", i[3])
                print("  CHEMISTRY MARKS : ", i[4])

                if (i[5] == 0):
                    print("  BIOLOGY MARKS   : ", i[6])
                    print("  COMPUTER MARKS  : ", i[7])
                elif (i[6] == 0):
                    print("  MATHS MARKS     : ", i[5])
                    print("  COMPUTER MARKS  : ", i[7])
                elif (i[7] == 0):
                    print("  MATHS MARKS     : ", i[5])
                    print("  BIOLOGY MARKS   : ", i[6])

                print("  GRADES          : ", i[10])
                print()
            
            ch=input("  DO YOU WANT TO MODIFY (Y/N) ? : ")
            
            if ch=='y' or ch=='Y' :
                mycursor.execute("select * from marksheet")
                result=mycursor.fetchall()
                for i in result:
                    if i[0]==rollno:
                        print()
                        rno=int(input("  ENTER THE NEW ROLL NO : "))
                        name=input("   ENTER THE STUDENT'S NAME : ")
                        eng=float(input("   ENTER MARKS IN ENGLISH : "))
                        chem=float(input("   ENTER MARKS IN CHEMISTRY : "))
                        phy=float(input("   ENTER MARKS IN PHYSICS : "))
                        print("\n \t 1. MATHS and BIO ")
                        print("\n \t 2. BIO and COMP ")
                        print("\n \t 3. MATHS and COMP \n")
                        cho=int(input("  ENTER YOUR CHOICE DEPENDING ON STUDENT's COMBINATION : "))
                        if cho==1:
                            maths=float(input("\n   ENTER MARKS IN MATHS : "))
                            bio=float(input("   ENTER MARKS IN BIOLOGY : "))
                            comp=0
                            val=(rno,name,eng,phy,chem,maths,bio,comp,rollno)
                            mycursor.execute(sql1,val)
                            mydb.commit()
                                
                        elif cho==2:
                            bio=float(input("\n   ENTER MARKS IN BIOLOGY : "))
                            comp=float(input("   ENTER MARKS IN COMPUTER : "))
                            maths=0
                            val=(rno,name,eng,phy,chem,maths,bio,comp,rollno)
                            mycursor.execute(sql1,val)
                            mydb.commit()
                                
                        elif cho==3:
                            maths=float(input("\n   ENTER MARKS IN MATHS : "))
                            comp=float(input("   ENTER MARKS IN COMPUTER : "))
                            bio=0
                            val=(rno,name,eng,phy,chem,maths,bio,comp,rollno)
                            mycursor.execute(sql1,val)
                            mydb.commit()
                        print("\n  MODIFIED SUCCESSFULLY !!!!! \n")
                        break

    if k == 0:
        print("\n  NO SUCH RECORD")
    mydb.close()

 
def menu():
    while(1):
        print("\n   ********** WELCOME TO PROGRAM ********** ")
        print("\n       1. ADD RECORD")
        print("\n       2. DELETE ANY RECORD ")
        print("\n       3. MODIFY ANY RECORD ")
        print("\n       4. SEARCH ANY RECORD ")
        print("\n       5. DISPLAY ALL THE RECORDS  ")
        print("\n       6. EXIT ")
        print()
        ch=int(input("      ENTER YOUR CHOICE : "))

        if ch==1:
            add()

        elif ch==2:
            delete()
            
        elif ch==3:
            modify()
            
        elif ch==4:
            search()
    
        elif ch==5:
            display()

        elif ch==6:
            print("\n       OUT OF THE PROGRAM !!!")
            exit(0)

def login():
    username = "Admin"
    password = "Ab@123"
    print("\n  ********** WELCOME TO ADMIN SECTION ********** \n")
    Username = input("  ENTER THE USERNAME : ")
    Password = input("  ENTER THE PASSWORD : ")

    if Username == username and Password == password :
        print("\n        ****************** WELCOME TO MARKSHEET ******************")
        menu()
    else:
        print("\n   -------- Invalid Username/Password -------- \n")
        login()

login()