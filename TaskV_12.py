stack = []

while True:
    comm = input().strip()
    if comm.startswith('push_front'):
        number = int(comm.split()[1])
        stack.insert(0, number)
        print("ok")
    elif comm.startswith('push_back'):
        number = int(comm.split()[1])
        stack.append(number)
        print("ok")
    elif comm == "pop_front":
        if len(stack) == 0:
            print("error")
        else:
            print(stack[0])
            del stack[0]
    elif comm == "pop_back":
        if len(stack) == 0:
            print("error")
        else:
            print(stack[-1])
            del stack[-1]
    elif comm == "front":
        if len(stack) == 0:
            print("error")
        else:
            print(stack[0])
    elif comm == "back":
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
