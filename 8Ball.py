# Allow the user to input their question.
# Show an in progress message.
# Create 5 to 10 responses, and show a random response.
# Allow the user to ask another question/advice or quit the game.


# First, we can define a function to start the 8ball game.
def eight_ball():

    # Then, we import random to later be able to use the randint method to pull a random integer out of a range.
    import random

    # To ensure that the 8ball game loops to the user's discretion, we can use a while loop.
    # The initial condition can be anything, but I chose to use numbers.
    # I chose to write the numbers as strings to simplify the code, as an input method will later be used.
    count = '1'
    while count == '1':
        question = input('Please, ask away: ')

        print('System is in progress...')

        # We can use a dictionary to attach values to certain keys. Since I am using the randint method,
        # I decided to use a dictionary with keys as numbers to easily and randomly choose a response.
        responses = {
            0 : 'Not a chance!',
            1 : 'The future is unclear...',
            2 : 'Definitely.',
            3 : 'In your dreams, perhaps.',
            4 : 'If you give a small sum of $100 to the man next door, then yes!',
            5 : 'More than likely.',
            6 : 'Fear not! The answer is a resounding yes.',
            7 : 'You must still be sleeping! Of course not!',
            8 : 'This world is a confusing one...',
            9 : 'There is a 99.999% chance.'
        }

        # Here is where we randomly save one of the dictionary's values to a variable.
        response = random.randint(0, 9)

        # Now we print that response.
        print(responses[response])

        # Over here we want the user's input to determine whether the while loop should continue or not.
        count = input('Want to ask me something else? Type 1 to continue, type 0 to quit: ')

        # In case the user enters an invalid number, we can nest another while loop so that the user will keep trying.
        while count != '1' and count != '0':
            print('Error. Invalid input! Please try again.')
            count = input('Want to ask me something else? Type 1 to continue, type 0 to quit: ')

# Let's test the code!
eight_ball()

