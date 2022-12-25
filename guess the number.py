import random

class guess:

    
    def chances_count_message(self,count,chances):
        count+=1
        chances-=1
        print(f'\nYou have {chances} left!!!')
    
    def messages(self):
        lst=[
            'Hang in there\n',
            'Don\'t give up\n',
            'Keep pushing\n',
            'Keep fighting!\n',
            'Stay Strong\n',
            'Come on! You can do it!\n'
        ]
        return random.choice(lst)
    def check_guessed_number(self):
        count=1
        chances = 5
        user_guess_number=int(input('Guess a number from 1 and 100\n '))
        print(f'You have {chances} left!!\n')
        rand=random.randint(1,100)
        self.messages()
        
        while True:
            if user_guess_number==rand:
                return f'Hurray! You got it in {count} steps'
            elif user_guess_number>rand and chances >=1 and user_guess_number<100:
                self.messages()
                user_guess_number=int(input('Your number is greater than the random number \n Enter again: '))
                self.chances_count_message(count,chances)
            elif user_guess_number<rand and chances>=1 and user_guess_number<100:
                self.messages()
                user_guess_number=int(input('Your number is smaller than random number\n Enter again:'))  
                self.chances_count_message(count,chances)
            elif user_guess_number>100 and chances>=1:
                self.messages()
                print(f'\nYou have {chances} left!!!')
                self.chances_count_message(count,chances)
            else: 
                return 'You have failed to guess the number'

numberGuessingGame = guess()
print(numberGuessingGame.check_guessed_number())


