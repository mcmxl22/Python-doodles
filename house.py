import subprocess

def front_porch():
    print '\nYou\'re on the porch. Choose a door.\n'
	
    dic = {'front', 'exit'}
    for d in dic:
        print '%s' % d
		
    choice = raw_input('\n> ')
	
    if choice == 'exit':
        quit()
			
    elif choice == 'front':
        living_room()

def stairs():
    print '\nYou\'re in the upstairs hall. There are 6 doors. Choose one.'
	
    doors = [range(1, 8)]
	
    for d in doors:
        print '\n%s' % d
      
    choice = raw_input('\n> ')
    
    if choice in {'1', '2', '3', '5'}:
        print 'This room is occupied. The door is locked.'
        stairs()

    elif choice in {'4', '6'}:
        print 'This room is empty.'
        stairs()
		
    elif choice == '7':
        living_room()
		
def living_room():
    print '\nYou\'re in the livingroom. Choose a room or activity.\n'
	
    list = ('kitchen', 'stairs', 'porch', 'basement', 'browse', 'rest')
	
    for l in list:
        print '%s' % l
		
    choice = raw_input('\n> ')
	
    if choice == list[1]:
        stairs()
		
    elif choice == list[2]:
        front_porch()
		
    elif choice == list[0]:
        print 'The kitchen is being remodeled. Come back later.'
        living_room()
		
    elif choice == list[3]:
        print 'Do you want to do laundry?'
		
        list = ('yes', 'no')
		
        for l in list:
            print '\n%s' % l
        choice = raw_input('\n> ')
        if choice == list[0]:
            print '\nYou\'ll have to wait.'
            living_room()
        elif choice == list[1]:
            living_room()
		
    elif choice == list[4]:
        subprocess.call('web.py', shell=True)
        living_room()
	
    elif choice == list[5]:
        print list[5]+'ing'
        subprocess.call('countd.py', shell=True)
        living_room()
		
if __name__ == "__main__":
    front_porch()
