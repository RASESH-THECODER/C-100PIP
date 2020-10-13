class Car(object):

    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.model=model
        self.company=company
        self.speed_limit=speed_limit
    
    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating")

    def gear(self):
        print("gear_changed")
    
audi=Car("a6","red","audi","80")
print(audi.start())

print(audi.stop())
print(audi.accelerate())
print(audi.gear())