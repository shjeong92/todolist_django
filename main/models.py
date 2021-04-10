from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    #CASCADE -> ForeignKey 가 바라보는 값이 삭제될때 ForeignKey를 포함하는 모델 인스턴스도 삭제된다
    #PROTECT -> 설정시 ForeignKey가 바라보는 값이 삭제되지 않도록 ProtectedError을 발생시킨다
    #SET_NULL -> ForeignKey가 바라보는 값이 삭제될때 ForeignKey를 null로 바꾼다
    #SET_DEFAULT -> ForeignKeyField 값을 defualt 값으로 바꾼다. (defualt 값이 있을때만 가능)
    #SET() -> ForeignKeyField가 바라보는 값이 삭제될때 ForeignKeyField값을 SET에 설정된 함수 등에 의해 설정된다.
    #DO_NOTHING -> 아무런 행동을 취하지 않는다. 참조무결성을 해칠 위험이 있다.
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def  __str__(self):
        return self.text