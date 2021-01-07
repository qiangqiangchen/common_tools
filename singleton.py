

class MySingleton:
    #单例模式
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

#单例模式
#第一种：使用函数装饰器实现

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
print('使用函数装饰器实现')
cls1=Cls()
cls2=Cls()
print(id(cls1)==id(cls2))

#第二种：使用类装饰器实现

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
print('使用类装饰器实现')
cls3=Cls2()
cls4=Cls2()

print(id(cls3)==id(cls4))


#第三种：使用new关键字实现单例
class Single(object):
    _instance=None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance=object.__new__(cls,*args,**kwargs)
        return cls._instance
    def __init__(self):
        pass

print('__new__关键字实现')
single1=Single()
single2=Single()
print(id(single1)==id(single2))

#第三种：使用metaclass 关键字实现单例
class Singleton2(type):
    _instance={}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls]=super(Singleton2,cls).__call__(*args,**kwargs)
        return cls._instance[cls]

class Cls4(metaclass=Singleton2):
    pass

print('使用metaclass 关键字')
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