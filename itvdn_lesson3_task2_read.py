import time
import gevent
from gevent.event import Event


def check_if_string_in_file(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False


def reader(file_name, string_to_search):
    try:
        check_if_string_in_file(file_name, string_to_search)
    except FileNotFoundError:
        print('no file - function is asleep')
        time.sleep(5)
        return False
    else:
        event.set()
        print('The word was found')
        return True


def deleter(file_name):
    event.wait()
    del file_name
    print('File deleted')


while True:
    event = Event()

    name = str(input('Enter file name: '))
    if not reader(name, "Wow!"):
        continue
    deleter(name)
