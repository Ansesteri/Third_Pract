stack = []

while True:
    comm = input().strip()
    if comm.startswith('push'):
        number = int(comm.split()[1])
        stack.insert(0, number)
        print("ok")
    elif comm == "pop":
        if len(stack) == 0:
            print("error")
        else:
            print(stack.pop())
    elif comm == "front":
        if len(stack) == 0:
            print("error")
        else:
            print(stack[-1])
    elif comm == "size":
        print(len(stack))
    elif comm == "clear":
        stack.clear()
        print("ok")
    elif comm == "exit":
        print("bye")
        break
    else:
        print("error")
