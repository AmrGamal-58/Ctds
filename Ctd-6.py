import cv2
import random

def display_result(winner):
    if winner== "user":
        background = cv2.imread("D:\pissed-off-face-winner-meme.jpg")
        text=username+" Won!"
       
    elif winner== "computer" :
        background = cv2.imread("D:\Dark_Souls_You_Died_Screen_-_Completely_Black_Screen_0-2_screenshot.jpg")
        text = "You lost."

    background = cv2.resize(background, (500, 500))

    cv2.putText(background, text, (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

    cv2.imshow("Result", background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




def play_game(username):
    bags = [10, 10, 10]
    turn = 'user'
    
    while sum(bags) > 0:
        if turn == 'user':
            print(f'Bags: {bags}')
            bag_choice = -1
            while bag_choice not in [0, 1, 2] or bags[bag_choice] == 0:
                try:
                    bag_choice = int(input('Choose a bag (1, 2, or 3): ')) - 1
                    if bag_choice not in [0, 1, 2]:
                        print('Invalid bag choice. Please choose a valid bag number (1, 2, or 3).')
                    elif bags[bag_choice] == 0:
                        print('Bag is already empty. Please choose another bag.')
                except ValueError:
                    print('Invalid bag choice. Please enter a number (1, 2, or 3).')
            num_objects = -1
            while num_objects < 1 or num_objects > 5 or num_objects > bags[bag_choice]:
                try:
                    num_objects = int(input('Choose the number of objects to remove (1-5): '))
                    if num_objects < 1 or num_objects > 5:
                        print('Invalid number of objects. Please enter a number between 1 and 5 (inclusive).')
                    elif num_objects > bags[bag_choice]:
                        print(f'Not enough objects in the bag. Please enter a number between 1 and {bags[bag_choice]}.')
                except ValueError:
                    print('Invalid number of objects. Please enter a number (1-5).')
            bags[bag_choice] -= num_objects
            if sum(bags) == 0:
                return 'user'
            turn = 'computer'
        else:
            bag_choice = random.randint(0, 2)
            while bags[bag_choice] == 0:
                bag_choice = random.randint(0, 2)
            num_objects = random.randint(1, min(5, bags[bag_choice]))
            print(f'Computer removed {num_objects} from bag {bag_choice + 1}')
            bags[bag_choice] -= num_objects
            if sum(bags) == 0:
                return 'computer'
            turn = 'user'

username = input('Enter your username: ')
result = play_game(username)
display_result(result)