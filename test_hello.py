from hello import hello
def test_hello():
    #return print(hello("David"))
    assert hello("David") == "hello, David"

test_hello()

