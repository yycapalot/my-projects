#assignment#
#####


#stock start
#variables with 'initial' word are to display the initial stock in report
#variables with 'Sales' word are to count the number of products sold from the system
#variables with 'Restock' word are to count the number of products restocked to the system
#'global' = to modify variable inside function
F1=200
S1=150
V1=100
T1=90
H1=80
initialF1=200
initialS1=150
initialV1=100
initialT1= 90
initialH1= 80
F1Sales=0
S1Sales=0
V1Sales=0
T1Sales=0
H1Sales=0
F1Restock=0
S1Restock=0
V1Restock=0
T1Restock=0
H1Restock=0
unit={}

#menu
def menuDisplay():
    print('\n\n\t**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**')
    print('\t**                                       **')
    print('\t**       Welcome to ----- Pharmacy       **')
    print('\t**                                       **')
    print('\t**      1. Check inventory               **')
    print('\t**      2. Sales                         **')
    print('\t**      3. Restock item                  **')
    print('\t**                                       **')
    print('\t**      5. End of Day (Sales Report)     **')
    print('\t**      9. Quit                          **')
    print('\t**                                       **')
    print('\t**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**')

    option=str(input('\nPlease enter your option:'))
    menuSelection(option)

#selection
def menuSelection(option):
        if option=='1':
            inventory()
        elif option=='2':
            sales()
        elif option=='3':
            restock()
        elif option=='5':
            report()
        elif option=='9':
            leave()
        else:
            error()
        
#inventory
def inventory():
    print('\n\t            Inventory Status              ')
    print('\n\t============================================')
    print('\t:      Item               |     Stock      :')
    print('\t============================================')
    print('\t:  Face Mask  (50pieces)  |    ',F1,'units   :')
    print('\t:  Hand Senitizer (50ml)  |    ',S1,'units   :')
    print('\t:  Vaseline (100g)        |    ',V1,'units   :')
    print('\t:  Toothpaste             |    ',T1,'units   :')
    print('\t:  Hansaplast (100strips) |    ',H1,'units   :')
    print('\t============================================')

    choice=str(input('\nEnter 1 to continue or 0 to exit:'))
    if choice=='1':
        menuDisplay()
    elif choice=='0':
        leave()
    else:
        error()

#sales
#F1(change)=F1(initial)-units
def sales():
    global F1
    global S1
    global V1
    global T1
    global H1
    global F1Sales
    global S1Sales
    global V1Sales
    global T1Sales
    global H1Sales
    
    print('\n\t                    Sales Menu                       ')
    print()
    print('\t===============================================================')
    print('\t:       Item              |       Stock      |      Price     :')
    print('\t===============================================================')
    print('\t:  Face Mask  (50pieces)  |    ',F1,' units   |     RM 30.00   :')
    print('\t:  Hand Senitizer (50ml)  |    ',S1,' units   |     RM  7.00   :')
    print('\t:  Vaseline (100g)        |    ',V1,' units   |     RM 13.00   :')
    print('\t:  Toothpaste             |    ',T1,' units   |     RM 10.90   :')
    print('\t:  Hansaplast (100strips) |    ',H1,' units   |     RM 13.50   :')
    print('\t===============================================================')
    print()
    print('\tEnter F for face mask.')
    print('\tEnter S for hand senitizer.')
    print('\tEnter V for vaseline.')
    print('\tEnter T for toothpaste.')
    print('\tEnter H for handsaplast.')

    item_description=input('\nEnter the name of the item:')

    c=item_description
    
    if(c=='F' or c=='f'):
        units=input('Units of Face Mask customer want to purchase:')
        if (units.isnumeric()== True):   #if units=integer then process
            if F1 < int(units):                 #stock<units
                print('\nSorry we dont have sufficient stock now, we only have',F1,'units.')
                choice=str(input('\nEnter 1 back to sales menu or 0 to main manu:'))
                if choice=='1':         
                    sales()
                elif choice=='0':
                    menuDisplay()
            else:
                price=30
                F1=F1-int(units)
                F1Sales=F1Sales+int(units)
        else:                            #if units!=integer then error
            salesError()    
    elif(c=='S' or c=='s'):
        units=input('Units of Hand Senitizer customer want to purchase:')
        if (units.isnumeric()== True):
            if S1<int(units):                 
                print('\nSorry we dont have sufficient stock now, we only have',S1,'units.')
                choice=str(input('\nEnter 1 back to sales menu or 0 to main menu:'))
                if choice=='1':         
                    sales()
                elif choice=='0':
                    menuDisplay()
            else:
                price=7
                S1=S1-int(units)
                S1Sales=S1Sales+int(units)
        else:                            
            salesError()  
    elif(c=='V' or c=='v'):
        units=input('Units of Vaseline customer want to purchase:')
        if (units.isnumeric()== True):
            if V1<int(units):                 
                print('\nSorry we dont have sufficient stock now, we only have',V1,'units.')
                choice=str(input('\nEnter 1 back to sales menu or 0 to main menu:'))
                if choice=='1':         
                    sales()
                elif choice=='0':
                    menuDisplay()
            else:
                price=13
                V1=V1-int(units)
                V1Sales=V1Sales+int(units)
        else:
            salesError()
    elif(c=='T' or c=='t'):
        units=input('Units of Toothpaste customer want to purchase:')
        if (units.isnumeric()== True):
            if T1<int(units):                 
                print('\nSorry we dont have sufficient stock now, we only have',T1,'units.')
                choice=str(input('\nEnter 1 back to sales menu or 0 to main menu:'))
                if choice=='1':         
                    sales()
                elif choice=='0':
                    menuDisplay()
            else:
                price=10.9
                T1=T1-int(units)
                T1Sales=T1Sales+int(units)
        else:
            salesError()
    elif(c=='H' or c=='h'):
        units=input('Units of Hansaplast customer want to purchase:')
        if (units.isnumeric()== True):
            if H1<int(units):                 
                print('\nSorry we dont have sufficient stock now, we only have',H1,'units.')
                choice=str(input('\nEnter 1 back to sales menu or 0 to main menu:'))
                if choice=='1':         
                    sales()
                elif choice=='0':
                    menuDisplay()
            else:
                price=13.5
                H1=H1-int(units)
                H1Sales=H1Sales+int(units)
        else:
            salesError()
    else:
        salesError()

    totalPrice=int(units)*price
    print('\nTotal price:RM','%.2f'% totalPrice)
    print('Recorded successfully !')

    choice=str(input('\nEnter 1 to continue or 0 to exit:'))
    if choice=='1':
        menuDisplay()
    elif choice=='0':
        leave()
    else:
        error()
        sales()
    
#restock
def restock():
    global F1
    global S1
    global V1
    global T1
    global H1
    global F1Restock
    global S1Restock
    global V1Restock
    global T1Restock
    global H1Restock

    print('\n\t                Restock Menu                        ')
    print()
    print('\t==============================================================')
    print('\t:        Item             |       Stock      |      Price     :')
    print('\t==============================================================')
    print('\t:  Face Mask  (50pieces)  |    ',F1,' units   |     RM 30.00   :')
    print('\t:  Hand Senitizer (50ml)  |    ',S1,' units   |     RM  7.00   :')
    print('\t:  Vaseline (100g)        |    ',V1,' units   |     RM 13.00   :')
    print('\t:  Toothpaste             |    ',T1,' units   |     RM 10.90   :')
    print('\t:  Hansaplast (100strips) |    ',H1,' units   |     RM 13.50   :')
    print('\t==============================================================')
    print()
    print('\tEnter F for face mask.')
    print('\tEnter S for hand senitizer.')
    print('\tEnter V for vaseline.')
    print('\tEnter T for toothpaste.')
    print('\tEnter H for handsaplast.')
    
    restock=input('\nEnter the name of the item:')

    c=restock
    
    if(c=='F' or c=='f'):
        units=input('Units of Face Mask you want to restock:')
        if (units.isnumeric()== True):
            F1=F1+int(units)
            F1Restock=F1Restock+int(units)
        else:
            restockError()
    elif(c=='S' or c=='s'):
        units=input('Units of Hand Senitizer you want to restock:')
        if (units.isnumeric()== True):
            S1=S1+int(units)
            S1Restock=S1Restock+int(units)
        else:
            restockError()
    elif(c=='V' or c=='v'):
        units=input('Units of Vaseline you want to restock:')
        if (units.isnumeric()== True):
            V1=V1+int(units)
            V1Restock=V1Restock+int(units)
        else:
            restockError()
    elif(c=='T' or c=='t'):
        units=input('Units of Toothpaste you want to restock:')
        if (units.isnumeric()== True):
            T1=T1+int(units)
            T1Restock=T1Restock+int(units)
        else:
            restockError()
    elif(c=='H' or c=='h'):
        units=input('Units of Hansaplast you want to restock:')
        if (units.isnumeric()== True):
            H1=H1+int(units)
            H1Restock=H1Restock+int(units)
        else:
            restockError()
    else:
        restockError()
        
    print('Recorded successfully !')

    choice=str(input('\nEnter 1 to continue or 0 to exit:'))
    if choice=='1':
        menuDisplay()
    elif choice=='0':
        leave()
    else:
        error()
        restock()
    
#report
def report():
    print('\n\t                             Daily Sales report          ')
    print('\n\t========================================================================================================')
    print('\t:        Item             |    Initial Stock    |     Stock Out    |    Stock In    |   Closing Stock  :')
    print('\t========================================================================================================')
    print('\t:  Face Mask  (50pieces)  |     ',initialF1,' units     |     ',F1Sales,' units    |   ',F1Restock,' units    |    ',F1,' units   :')
    print('\t:  Hand Senitizer (50ml)  |     ',initialS1,' units     |     ',S1Sales,' units    |   ',S1Restock,' units    |    ',S1,' units   :')
    print('\t:  Vaseline (100g)        |     ',initialV1,' units     |     ',V1Sales,' units    |   ',V1Restock,' units    |    ',V1,' units   :')
    print('\t:  Toothpaste             |     ',initialT1,' units     |     ',T1Sales,' units    |   ',T1Restock,' units    |    ',T1,' units   :')
    print('\t:  Hansaplast (100strips) |     ',initialH1,' units     |     ',H1Sales,' units    |   ',H1Restock,' units    |    ',H1,' units   :')
    print('\t========================================================================================================')    
    print('\n\t(     NAME     )')
    print()
    print()
    print('\n\t_______________')

    choice=str(input('\nEnter 1 to continue or 0 to exit:'))
    if choice=='1':
        menuDisplay()
    elif choice=='0':
        leave()
    else:
        error()
        report()

#error
def error():
    key=str(input('\nInvalid input, please press Enter key to proceed.\n'))
    menuDisplay()

#sales error
def salesError():
    key=str(input('\nError input, please press Enter key to proceed.\n'))
    if (key==''):
        sales()

#restock error
def restockError():
    key=str(input('\nError input, please press Enter key to proceed.\n'))
    if(key==''):
        restock()
        
#exit
def leave():
    print('\nThank you for using this program. ^.^ ')
    print('-------- Pharmacy')
    exit()
    
menuDisplay()
