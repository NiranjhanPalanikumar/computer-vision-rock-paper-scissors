# Computer Vision RPS

## Description
Teachable Machines was used to collect the images and train the model. Teachable Machines is Google's online tool for computer vision applications, where you can capture images using a web camera for each class in your use-case. The images are then used to train a model which can recognise the different classes based on confidence percentage.

There are a total of four classes:
1. Rock
2. Paper
3. Scissor
4. Nothing

After capturing the images and training the model it can be exported as a tensorflow "keras_model.h5" file and the names of the different classes used are stored in the "labels.txt" file. 

Firstly we install all the required dependencies in a newly created environment so that it will not have any affects on the working of other programs. The required denpenencies are listed in the "requirements.txt" file, and you can install all of them together by typing "pip install requirements.txt" in your new environment.

The file "task_4_check_model_works" is a basic code to verify the working of our exported model from Techable Machines. The prediction has the output in the form [[r, p, s, n]], where each variable stands for their respective class [[Rock, Paper, Scissors, Nothing]] and represents the confidence percentage in the video capture. 

## manual_rps.py description
This python file is a program written to get a user choice and select a random option for the computer from the list [Rock, Paper, Scissors] defined through get_computer_choice() and get_user_choice() functions. Another function named get_winner() is defined which takes in the computer_choice and user_choice as inputs and runs a seris of if-else statements to check for the winner.

Finally, a function play() is executed that simulates the game and prints the winner on the screen.

## camera_rps.py
This python file is the compiled version of all the algorithms used earlier into methods and attributes of a class for ease of use and better readability. 

The class RockPaperScissors takes in the input for number of rounds to be played (with a default value of 5), and has 3 atrributes in total "user_wins" which keeps tracks of user's win score, and similaryly "computer_wins" for computer's win score along with "rounds". 

The method "get_computer_choice()" selects an option randomly from the list using random.choice(). The "get_prediction()" method uses the webcamera of the system to predict user input through the video feed and assigns the user's choice accordingly. The "get_winner()" method compares both the user's and computer's choice and determines the winner and allocates the score accordingly.

Finally, the function "play_rps()" runs a loop till the number of rounds is met or either the user or computer reaches the required score to win the seires. The "get_computer_choice()" and "get_prediction()" methods are called from the instance of the class RockPaperScissors and are then compared through the "get_winner()" method. A score is completed from proceeding to the next round. 

## Further improvements
The next improvement for this project would be to have a continuously running game screen using the web camera which takes in the input from the user and displays each round result and the final winner result on the screen.

