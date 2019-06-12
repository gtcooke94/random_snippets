def receive_and_print():
    print("Starting...")
    try:
        while True:
            # This yield will "pause" excution when next is called and wait until
            # the send is called
            payload = (yield)
            print("RECEIVED: " + payload)
    except GeneratorExit:
        print("CLOSING")
        raise

# could also do this with a finally block
def receive_and_print2():
    print("Starting...")
    try:
        while True:
            # This yield will "pause" excution when next is called and wait until
            # the send is called
            payload = (yield)
            print("RECEIVED: " + payload)
    finally:
        print("CLOSING")


receiver = receive_and_print()
# Prime it, because generators are lazy so it won't get to the yield yet
next(receiver)
# Send sends data into the generator function resuming where the yield is
receiver.send("val1")
receiver.send("val2")
# Make it so you can't send anything anymore, will throw GeneratorExit
receiver.close()


# Generators also have a throw
def receive_and_print3():
    print("Starting...")
    try:
        while True:
            try:
                # This yield will "pause" excution when next is called and wait until
                # the send is called
                payload = (yield)
            except ValueError:
                payload = "[INVALID]"
            print("RECEIVED: " + payload)
    except GeneratorExit:
        print("CLOSING")
        raise

receiver = receive_and_print3()
next(receiver)
receiver.send("Test1")
receiver.throw(ValueError)
receiver.send("Test2")
receiver.close()


#  # This is bad
#  def receive_and_yield():
#      print("Starting")
#      while True:
#          #  payload = (yield)
#          #  print("Line 61")
#          #  yield payload + "Hey"
#          #  print("Line 62")
#          yield (yield) + "Hey"

#  sender_receiver = receive_and_yield()
#  print("calling next")
#  next(sender_receiver)
#  print("calling send")
#  print(sender_receiver.send("val1"))
#  print("calling next")
#  next(sender_receiver)
#  print("calling send")
#  print(sender_receiver.send("val2"))

#  next(sender_receiver)
#  next(sender_receiver)

def make_dog():
    message = "Dog wants a treat"
    while True:
        bark = "BARK " + message.upper() + " BARK"
        message = (yield bark)

dog = make_dog()
next(dog)
print(dog.send("Hello"))
print(dog.send("Hi"))


# Delegating with "yield from" (This is one keyword)
# Delegates to a generator inside another generator

def gen_evens(limit):
    i = 0
    while i <= limit:
        if i % 2 == 0:
            yield i
        i += 1

def gen_evens_to_10():
    yield from gen_evens(10)

print(list(gen_evens(10)))
print(list(gen_evens_to_10()))





