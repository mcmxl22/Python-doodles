import time

def count():
    for i in reversed(range(0, 6)):
        time.sleep(1)
        print "%s\r" %i,
		
if __name__ == "__main__":
    count()