import time

def red():
    for i in range(7):
        time.sleep(1)
        print "%s\r" % 'R',
    green()
    
def yellow():
    for i in range(4):
        time.sleep(1)
        print "%s\r" % 'Y',
    red()

def green():
    for i in range(7):
        time.sleep(1)
        print "%s\r" % 'G',	
    yellow()

# def north_south():
    # print 'North and south lights.'
    # red()

# def east_west():
    # print 'East and west lights'
    # green()

red()
