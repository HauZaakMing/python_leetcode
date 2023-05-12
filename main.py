# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def example_dynamic_args(*args, **kwargs):
    '''动态参数'''
    print(args)
    print(kwargs)

example_dynamic_args(1,'2', True, name='xiaowu', age=18)
l = [1,'2',False]
d = {'name': 'xiaoming', 'age': 16}
example_dynamic_args(*l, **d)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
