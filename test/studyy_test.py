# a=[1,2,3,4,5,6]
# print(a[-1])
# print(a[-1:])

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt+":")
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
ask_ok("dwdfd")
#
# def kk(a):
#     l=[]
#     l.append(a)
#     print(l)
# kk(3)
# kk(4)
