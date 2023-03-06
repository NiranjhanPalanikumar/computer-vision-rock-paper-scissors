import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)  #value = 0 indicates default web camera
#cap = cv2.VideoCapture(1)  #value = 1 indicates usb web camera 
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def get_prediction():

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
    mean_value_last_10_samples = np.mean(full_list[-10:], axis=0)
    max_index = np.argmax(mean_value_last_10_samples)

    if max_index == 0:
        return "Rock"
    elif max_index == 1:
        return "Paper"
    elif max_index == 2:
        return "Scissors"
    else:
        return "Nothing"