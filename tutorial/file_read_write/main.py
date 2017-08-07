import os


def run():
    with open('jiang_jin_jiu.txt', 'r') as file:
        for line in file:
            print line

run()


def normal_run():
    file = open('jiang_jin_jiu.txt')

    for line in file:
        print line

    file.close()


def write_model():
    file = open('jiang_jin_jiu.txt', 'w')
    for line in file:
        print line

    file.close()


def other_write_model_append():
    append_write = open('jiang_jin_jiu.txt', 'a')
    print 'current:{}'.format(append_write.tell())
    append_write.write('hello in the end')
    print 'current:{}'.format(append_write.tell())
    append_write.seek(0)
    append_write.write('hello in the start')
    append_write.flush()
    append_write.close()


def other_write_model_rw():
    read_write = open('jiang_jin_jiu.txt', 'r+')
    print 'current:{}'.format(read_write.tell())
    read_write.write('hello in the start')
    read_write.close()
