global glb

class Test:
    def __init__(self):
        pass

def main():
    a = 1
    t = 2
    print(dir())
    print(locals().keys())
    print(globals().keys())

if __name__ == '__main__':
    main()
    t = Test()
    print(help(locals))