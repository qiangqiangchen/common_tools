

class MySingleton:
    #����ģʽ
    __obj=None
    __init_flag=True

    def __new__(cls, *args, **kwargs):
        if cls.__obj==None:
            cls.__obj=object.__new__(cls)
        return cls.__obj

    def __init__(self,name):
        if MySingleton.__init_flag:
            print('----init----')
            self.name=name
            MySingleton.__init_flag=False
            
            
            
            
# -*- coding:utf-8 -*-

#����ģʽ
#��һ�֣�ʹ�ú���װ����ʵ��

def singleton(cls):
    print(cls)
    _instance={}
    def inner():
        if cls not in _instance:
            _instance[cls]=cls()
        return _instance[cls]
    return inner
@singleton
class Cls(object):
    def __init__(self):
        pass
print('ʹ�ú���װ����ʵ��')
cls1=Cls()
cls2=Cls()
print(id(cls1)==id(cls2))

#�ڶ��֣�ʹ����װ����ʵ��

class Singleton2(object):
    def __init__(self,cls):
        self._cls=cls
        self._instance={}
    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls]=self._cls()
        return self._instance[self._cls]

@Singleton2
class Cls2(object):
    def __init__(self):
        pass
print('ʹ����װ����ʵ��')
cls3=Cls2()
cls4=Cls2()

print(id(cls3)==id(cls4))


#�����֣�ʹ��new�ؼ���ʵ�ֵ���
class Single(object):
    _instance=None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance=object.__new__(cls,*args,**kwargs)
        return cls._instance
    def __init__(self):
        pass

print('__new__�ؼ���ʵ��')
single1=Single()
single2=Single()
print(id(single1)==id(single2))

#�����֣�ʹ��metaclass �ؼ���ʵ�ֵ���
class Singleton2(type):
    _instance={}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls]=super(Singleton2,cls).__call__(*args,**kwargs)
        return cls._instance[cls]

class Cls4(metaclass=Singleton2):
    pass

print('ʹ��metaclass �ؼ���')
cls5=Cls2()
cls6=Cls2()

print(id(cls5)==id(cls6))

if __name__=='__main__':
    pass

if __name__=='__main__':
    a=MySingleton('a')
    b=MySingleton('b')
    print(a)
    print(b)