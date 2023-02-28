choice = ''
started = False

while choice != 'quit': #while TRUE

    choice=input('> ').lower()
    
    if choice == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit') 
        # print("""
        #start - to start the car
        #stop - to stop the car
        #quit - to exit
        # """)
    elif choice == 'start':
        if started == False:
            print('Çar started...Ready to go!')
            start = True
        else:
            print("Hey, car is already started")
    elif choice == 'stop':
        if start == True:
            print('Çar stopped.')
            start = False
        else:
            print('Car is not started')
    elif choice =='quit':
        break
    else:
        print ("I don't understand this command")
    
    
