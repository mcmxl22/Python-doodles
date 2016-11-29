def front_porch():
    print '\nYou\'re on the porch. Choose a door.'
	
    dic = {'front', 'exit'}
    for d in dic:
        print '\n%s' % num
 
    choice = raw_input('\n> ')
		
    if choice == 'exit':
        quit()
			
    elif choice == 'front':
        living_room()

def stairs():
    print '\nYou\'re in the upstairs hall. There are 6 doors. Choose one.'
	
    doors = [range(1, 8)]
	
    for num in doors:
        print '\n%s' % num
      
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
    print '\nChoose a room.'
	
    dic = {'kitchen', 'stairs', 'porch', 'basement'}
	
    for d in dic:
        print '\n%s' % d
		
    choice = raw_input('\n> ')
	
    if choice == 'stairs':
        stairs()
		
    elif choice == 'porch':
        front_porch()
		
    elif choice == 'kitchen':
        print 'The kitchen is being remodeled. Come back later.'
        living_room()
		
    elif choice == 'basement':
        print 'Do you want to do laundry?'
		
        dic = {'yes', 'no'}
		
        for d in dic:
            print '\n%s' % d
        raw_input('\n> ')
		
front_porch()