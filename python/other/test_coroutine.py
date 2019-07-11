def coroutine(arg):
    print(f"coroutine started, input arg: {arg}")
    while True:
        data = (yield)
        print(f"received data: {data}")
    print(f"coroutine finished.")
    # return in a coroutine would finish it too


c = coroutine("start")
next(c)  # make it to the first yield
c.send("another data")
c.send("stop")
c.close()
