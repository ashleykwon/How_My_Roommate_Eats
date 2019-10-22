def help_jessie_eat(liquid_type, food_type):
        unit_bite = 0
        unit_gulp = 0
        total_liquid = 0
        total_food = 0
        if food_type == 'jj':
            total_food = 132
            unit_bite  = 132 / 22
        if liquid_type == 'smart water':
            total_liquid = 591
            unit_gulp = 591 / 6
            print('unit gulp '+ str(unit_gulp))
        phase  = 'start'
        while phase != 'done':
            phase =  input("what phase of eating are you at? Here are your options: just opened the sandwich / eating the first half / eating the first bacon / eating the second half / eating the second bacon / eating remaining bacons/ done: ")
            if phase == 'just opened the sandwich':
                total_liquid -= unit_gulp
                print('\n')
                print('enter the next phase')
                
            elif phase == 'eating the first half':
                amt_food = total_food
                num_bites = 0
                while num_bites != 11:
                    num_bites = int(input('how many bites of the first half have you had? '))
                    print('this is the number of bites of the first half you had so far: '+ str(num_bites))
                    amt_food = amt_food - unit_bite
                    print(amt_food)
                if num_bites  == 11:
                    total_liquid -= unit_gulp
                    liquid_left = float(input('how much liquid is left? Enter the proportion of (amount left)/(total amount) that ranges from 0 to 1: '))
                    if liquid_left * total_liquid < total_liquid - unit_gulp:
                        print('in this phase you drank ' + str(total_liquid - unit_gulp - (liquid_left *total_liquid)) + ' ml more than you were supposed to drink')
                    elif liquid_left * total_liquid > total_liquid - unit_gulp:
                        print('in this phase you drank ' + str((liquid_left *total_liquid) - (total_liquid - unit_gulp)) + ' ml less than you were supposed to drink')
                    else:
                        print('you are doing fine!')
                    print('\n')
                    print('enter the next phase')
                    
                

            elif phase == 'eating the first bacon':
                if amt_food != 11*unit_bite:
                    print('Mmm... are you sure? Its likely that you fogot to enter some detail')
                total_liquid -= unit_gulp
                liquid_left = float(input('how much liquid is left? Enter the proportion of (amount left)/(total amount) that ranges from 0 to 1: '))
                if liquid_left * total_liquid < total_liquid - unit_gulp:
                    print('in this phase you drank ' + str(total_liquid - unit_gulp - (liquid_left *total_liquid)) + ' ml more than you were supposed to drink')
                elif liquid_left * total_liquid > total_liquid - unit_gulp:
                    print('in this phase you drank ' + str((liquid_left *total_liquid) - (total_liquid - unit_gulp)) + ' ml less than you were supposed to drink')
                else:
                    print('you are doing fine!')
                print('\n')
                print('enter the next phase')
                


            elif phase == 'eating the second half':
                num_bites = 0
                while num_bites != 11:
                    num_bites = int(input('how many bites of the second half have you had? '))
                    print('this is the number of bites of the second half you had so far '+ str(num_bites))  
                    amt_food = amt_food - num_bites
                    print(amt_food)
                if num_bites  == 11:
                    total_liquid -= unit_gulp
                    liquid_left = float(input('how much liquid is left? Enter the proportion of (amount left)/(total amount) that ranges from 0 to 1: '))
                    if liquid_left * total_liquid < total_liquid - unit_gulp:
                        print('in this phase you drank ' + str(total_liquid - unit_gulp - (liquid_left *total_liquid)) + ' ml more than you were supposed to drink')
                    elif liquid_left * total_liquid > total_liquid - unit_gulp:
                        print('in this phase you drank ' + str((liquid_left *total_liquid) - (total_liquid - unit_gulp)) + ' ml less than you were supposed to drink')
                    else:
                        print('you are doing fine!')
                    print('\n')
                    print('enter the next phase')
                    

            elif phase == 'eating the second bacon':
                if amt_food != 0:
                    print(amt_food)
                    print('Mmm... are you sure? Its likely that you fogot to enter some detail')
                total_liquid -= unit_gulp
                liquid_left = float(input('how much liquid is left? Enter the proportion of (amount left)/(total amount) that ranges from 0 to 1: '))
                if liquid_left * total_liquid < total_liquid - unit_gulp:
                    print('in this phase you drank ' + str(total_liquid - unit_gulp - (liquid_left *total_liquid)) + ' ml more than you were supposed to drink')
                elif liquid_left * total_liquid > total_liquid - unit_gulp:
                    print('in this phase you drank ' + str((liquid_left *total_liquid) - (total_liquid - unit_gulp)) + ' ml less than you were supposed to drink')
                else:
                    print('you are doing fine!')
                print('\n')                
                print('enter the next phase')
                

            elif phase == 'eating remaining bacons':
                if total_liquid < 0.9*unit_gulp:
                    print('you have less water than you should')
                elif total_liquid > 1.1*unit_gulp:
                    print('you have excess water')
                else:
                    print('well done!')
                print('\n')
                print('enter the next phase')  

            else:
                print('If the function stopped running before you entered done, you did something wrong. Otherwise its fine.')
                break

        return 'lol'

    
        


if __name__ == "__main__":
    liquid_type = 'smart water'
    food_type = 'jj'
    help_jessie_eat(liquid_type, food_type)