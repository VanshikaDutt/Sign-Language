# from function import *
# from time import sleep
# import os
# import cv2
# import numpy as np

# for action in actions: 
#     for sequence in range(no_sequences):
#         try: 
#             os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
#         except:
#             pass

# frame = cv2.imread('Image/{}/{}.jpg'.format(action, sequence))
# if frame is None:
#     print(f"Error: Unable to load image from Image/{action}/{sequence}.jpg")
#     continue  # Skip this frame and continue the loop

# test_image = cv2.imread('path/to/a/sample/image.jpg')
# if test_image is None:
#     print("Error loading test image!")
# else:
#     cv2.imshow("Test Image", test_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# image_path = 'Image/{}/{}.jpg'.format(action, sequence)
# print(f"Trying to load image from: {image_path}")
# frame = cv2.imread(image_path)


# with mp_hands.Hands(
#     model_complexity=0,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as hands:
    
#     for action in actions:
#         for sequence in range(no_sequences):
#             for frame_num in range(sequence_length):
#                 frame=cv2.imread('Image/{}/{}.jpg'.format(action,sequence))
#                 image, results = mediapipe_detection(frame, hands)
#                 draw_styled_landmarks(image, results)

#                 if frame_num == 0:
#                     cv2.putText(image, 'STARTING COLLECTION', (120,200), 
#                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
#                     cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
#                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
#                     cv2.imshow('OpenCV Feed', image)
#                     cv2.waitKey(200)
#                 else: 
#                     cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
#                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
#                     cv2.imshow('OpenCV Feed', image)
                
#                 keypoints = extract_keypoints(results)
#                 npy_path = os.path.join(DATA_PATH, action, str(sequence), str(frame_num))
#                 np.save(npy_path, keypoints)

#                 if cv2.waitKey(10) & 0xFF == ord('q'):
#                     break
                    

#     cv2.destroyAllWindows()




# from function import *
# from time import sleep
# import os
# import cv2
# import numpy as np


# for action in actions: 
#     for sequence in range(no_sequences):
#         try: 
#             os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
#         except:
#             pass

# # Set mediapipe model 
# with mp_hands.Hands(
#     model_complexity=0,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as hands:
    
#     # Loop through actions
#     for action in actions:
#         # Loop through sequences aka videos
#         for sequence in range(no_sequences):
#             # Loop through video length aka sequence length
#             for frame_num in range(sequence_length):
#                 # Construct the image path
#                 image_path = 'Image/{}/{}.jpg'.format(action, sequence)
                
#                 # Read the image
#                 frame = cv2.imread(image_path)

#                 # Check if the image was loaded successfully
#                 if frame is None:
#                     print(f"Error: Unable to load image from {image_path}")
#                     continue  # Skip this frame and continue to the next one
                
#                 # Make detections
#                 image, results = mediapipe_detection(frame, hands)
                
#                 # Draw landmarks on the image
#                 draw_styled_landmarks(image, results)

#                 # Display a message for the first frame
#                 if frame_num == 0:
#                     cv2.putText(image, 'STARTING COLLECTION', (120,200), 
#                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
#                     cv2.putText(image, f'Collecting frames for {action} Video Number {sequence}', (15,12), 
#                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
#                     # Show the image
#                     cv2.imshow('OpenCV Feed', image)
#                     cv2.waitKey(200)
#                 else: 
#                     cv2.putText(image, f'Collecting frames for {action} Video Number {sequence}', (15,12), 
#                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
#                     # Show the image
#                     cv2.imshow('OpenCV Feed', image)
                
#                 # Export the keypoints to a file
#                 keypoints = extract_keypoints(results)
#                 npy_path = os.path.join(DATA_PATH, action, str(sequence), str(frame_num))
#                 np.save(npy_path, keypoints)

#                 # Break gracefully if 'q' is pressed
#                 if cv2.waitKey(10) & 0xFF == ord('q'):
#                     break                    
#     cv2.destroyAllWindows()













from function import *
from time import sleep
import os
import cv2
import numpy as np

# Base path to the "Image" directory
BASE_PATH = r'C:\Users\vansh\Desktop\Vanshika\IGDTUW\SEMESTER 7\Minor Project\ThirdCodeFile'

# Set the main data path where images are located
DATA_PATH = os.path.join(BASE_PATH, 'Image')

# Define actions based on your directory structure (A to Z)
actions = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # This will generate ['A', 'B', 'C', ..., 'Z']

# Set the sequence length (images per action)
sequence_length = 10  # 10 images per action folder (1.jpg to 10.jpg)

# Set mediapipe model 
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    
    # Loop through actions (A, B, C, ..., Z)
    for action in actions:
        # Loop through sequences (if you have more sequences for each action, adjust as needed)
        for sequence in range(1):  # Here we assume 1 sequence per action (for simplicity)
            # Create directory for each sequence (if not exists)
            try:
                os.makedirs(os.path.join(BASE_PATH, 'npy', action, str(sequence)))
            except FileExistsError:
                pass

            # Loop through video length aka sequence length (10 images)
            for frame_num in range(sequence_length):
                # Construct the image path based on the directory structure
                image_path = os.path.join(DATA_PATH, action, f'{frame_num + 1}.jpg')
                
                # Check if the image exists
                if not os.path.exists(image_path):
                    print(f"Error: Unable to find image at {image_path}")
                    continue  # Skip this frame and continue to the next one
                
                # Read the image
                frame = cv2.imread(image_path)

                # Check if the image was loaded successfully
                if frame is None:
                    print(f"Error: Unable to load image from {image_path}")
                    continue  # Skip this frame and continue to the next one
                
                # Make detections
                image, results = mediapipe_detection(frame, hands)
                
                # Draw landmarks on the image
                draw_styled_landmarks(image, results)

                # Display a message for the first frame
                if frame_num == 0:
                    cv2.putText(image, 'STARTING COLLECTION', (120,200), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
                    cv2.putText(image, f'Collecting frames for {action} Video Number {sequence}', (15,12), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    # Show the image
                    cv2.imshow('OpenCV Feed', image)
                    cv2.waitKey(200)
                else: 
                    cv2.putText(image, f'Collecting frames for {action} Video Number {sequence}', (15,12), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    # Show the image
                    cv2.imshow('OpenCV Feed', image)
                
                # Export the keypoints to a file
                keypoints = extract_keypoints(results)
                npy_path = os.path.join(BASE_PATH, 'npy', action, str(sequence), f'{frame_num + 1}.npy')
                
                # Ensure the directory for npy file exists
                os.makedirs(os.path.dirname(npy_path), exist_ok=True)

                # Save the keypoints to a .npy file
                np.save(npy_path, keypoints)

                # Break gracefully if 'q' is pressed
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break                    

    # Destroy all windows after processing
    cv2.destroyAllWindows()
