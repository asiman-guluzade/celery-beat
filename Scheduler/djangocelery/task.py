from  Scheduler.celery import app
from time import sleep

@app.task(name="mod", bind=True, default_retry_delay=10, max_retries=5)
def mod(self):
    y=5
    x=3
    try:
        z = x % y
        print(f'{x} % {y} = {x%y}')
        return z
    except :
        mod.retry()
        print(f'Error with mod')

@app.task(name="test")
def test(a:int,b:int):
    g = a*b
    print(f'{a} % {b} = {a%b}')
    print(g)
    sleep(15)
    return g

@app.task(name="jack")
def test3(c:int,b:int):
    g = c*b
    print(f'{c} % {b} = {c%b}')
    print(g)
    return g