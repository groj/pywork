import time

# decorator definition
class timer:
    # singleton 
    register = {}
    def __init__(self, param):
        print("timer: init, param:", param)
        self.param = param
        
    def __call__(self, func):
        print("timer: call, func:", func)
        def inner(*args):
            print("timer: call: inner, args:", args)
            
            ts = time.time()
            ret = func(*args)            
            d = time.time() - ts
            print("timer: delta:", d)
            
            try:
                self.register[self.param].append(d)                
            except KeyError:
                self.register[self.param] = [d]

            return ret
        return inner

# product model definition
class product:
    def __init__(self, value):
        self.__counter = int(value)
        print("product: init, value:", value)
        
    @timer("increment time")
    def increment(self, value):
        print("product: increment, value:", value)
        for _ in range(value):
            self.__counter += 1
            time.sleep(0.01)
        return self.__counter

    @timer("decrement time")
    def decrement(self):
        print("product: decrement")
        self.__counter -= 1
        time.sleep(0.01)
        return self.__counter


# product simulation
print("----")
p = product(12)
p.increment(30)
p.decrement()
p.decrement()
p.decrement()
p.decrement()
p.increment(20)
cnt = p.decrement()

# result analysis
print("----")
print("counter:", cnt)
for key in timer.register.keys():
    print(key, timer.register[key])
