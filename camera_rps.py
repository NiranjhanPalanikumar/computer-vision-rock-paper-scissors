import cv2
from keras.models import load_model
import numpy as np
import time
import random


class RockPaperScissors:
    def __init__(self, rounds=5):
        self.rounds = rounds
        self.user_wins = 0
        self.computer_wins = 0


    def get_computer_choice(self):
        option_list = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(option_list)
        
        return computer_choice
    

    def get_prediction(self):
        model = load_model('keras_model.h5')
        #cap = cv2.VideoCapture(0)  #value = 0 indicates default web camera
        cap = cv2.VideoCapture(1)  #value = 1 indicates usb web camera 
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        prediction_list = []

        start_time = time.time()
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)

            prediction_list.append(prediction[0])

            cv2.imshow('frame', frame)
            # Press q to close the window
            #print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                    
            end_time = time.time()
            elapsed = end_time - start_time
            if elapsed > 5:
                break

        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        #print(prediction_list)
        #return prediction_list
        mean_value_last_10_samples = np.mean(prediction_list[-10:], axis=0)
        max_index = np.argmax(mean_value_last_10_samples)

        if max_index == 0:
            return "Rock"
        elif max_index == 1:
            return "Paper"
        elif max_index == 2:
            return "Scissors"
        else:
            return "Nothing"


    def get_winner(self, computer_choice, user_choice):
        if user_choice == computer_choice:
            print("It is a tie!")

        elif user_choice == "Rock" and computer_choice == "Scissors":
            print("You won!")
            self.user_wins += 1

        elif user_choice == "Paper" and computer_choice == "Rock":
            print("You won!")
            self.user_wins += 1

        elif user_choice == "Scissors" and computer_choice == "Paper":
            print("You won!")
            self.user_wins += 1

        elif user_choice == "Nothing":
            print("You lost")
            self.computer_wins += 1

        else:
            print("You lost")
            self.computer_wins += 1


num_rounds = 5
rps = RockPaperScissors(num_rounds)

def play_rps():
    for round in range(1, num_rounds+1):
        computer_choice = rps.get_computer_choice()
        user_choice = rps.get_prediction()

        rps.get_winner(computer_choice, user_choice)

        if rps.user_wins == 3:
            print("You won the series")
            break
        elif rps.computer_wins == 3:
            print("Computer won the series")
            break
        elif round == num_rounds:
            print("The series score is a tie")
