# replace the contents of this comment with your full name

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!

def helloworld():
    print('Hello World!')
    print()
    print('What is your name?') #asks for users name
    yrName=input()
    print('')
    while True: # program loops until user picks 1 of 3
        print('Hey '+yrName+' please choose a language and I will greet you in that language?')
        print('')
        print('1.Portuguese')
        print('2.Italian')
        print('3.Japanese')
        print('')
        choice=input() #asks for user's choice language
        if(choice==str(1)):
           print('Olá,'+yrName+'!') #output Hello to screen in 1.Portugese
           break
        elif(choice==str(2)):
            print('Ciao, '+yrName+'!') #output Hello to screen in 2.Italian
            break
        elif(choice==str(3)):
            print('Konnichiwa, '+yrName+'!') #output Hello to screen in 3.Japanese
            break
    # program exits on breaks to exit
    print('Thank you!')
    # end
