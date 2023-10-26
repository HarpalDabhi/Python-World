def hack_msg(fx):
    def dist_msg():
        print("Hi..Sent")
        fx()
        print("Hi..Received")
    return dist_msg

@hack_msg
def midd_ms():
    print("I am Deslecting crypted msg..")
# print(hack_msg(midd_ms()))

midd_ms()

def maha(fx):
    def small():
        print("Start..")
        fx()
        print("End..")
    return small

@maha
def mid():
    print("I am the Midddle")

mid()

def inputi(fx):
    def interupt():
        print("Input ..")
        fx()
        print("Output ..")
    return interupt

@inputi
def process():
    print("Processing")

# print(inputi(process()))
process()
