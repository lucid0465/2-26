from django.db import models

class MyBoard(models.Model) :
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=1000)
    mydate = models.DateField()

    def __str__(self):    #MyBoard의 object(row)를 출력할 때 메모리 출력대신에 정의된 것이 출력
        return self.mytitle

class MyMember(models.Model):
    myname = models.CharField(max_length=100)
    mypassword = models.CharField(max_length=100)
    myemail = models.CharField(max_length=100)

    def __str__(self):
        return str({'myname':self.myname,'myemail':self.myemail})

        




