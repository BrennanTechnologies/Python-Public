def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def test_nonlocal():
        spam = "test_nonlocal spam"
        print("test_nonlocal: " + spam)

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    # print("After local assignment:", spam)
    # do_nonlocal()
    print("After nonlocal assignment:", spam)
    test_nonlocal()
    # do_global()
    # print("After global assignment:", spam)


scope_test()
# print("In global scope:", spam)
