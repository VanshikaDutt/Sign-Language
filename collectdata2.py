import os
import cv2

# Open the camera (use 0 for the default camera)
cap = cv2.VideoCapture(0)

# Ensure the camera was opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Path where images will be saved
directory = 'Image/'

# Ensure that all directories for 'A' to 'Z' exist
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    folder_path = os.path.join(directory, letter)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Loop to capture frames
while True:
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret or frame is None:
        print("Error: Failed to capture image.")
        break  # Exit the loop if frame capture failed

    # Count the number of images in each folder
    count = {}
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        letter_path = os.path.join(directory, letter)
        if os.path.exists(letter_path):
            count[letter] = len(os.listdir(letter_path))
        else:
            # If the folder doesn't exist, initialize count as 0
            count[letter] = 0

    # Define a region of interest (ROI) to display and save
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame, (0, 40), (300, 400), (255, 255, 255), 2)

     # Check if the frame is valid before displaying
    if frame is not None:
        # Show the original frame and the ROI
        cv2.imshow("data", frame)
        cv2.imshow("ROI", frame[40:400, 0:300])

        # Crop the frame to the ROI for saving
        frame = frame[40:400, 0:300]

    # Capture key press and save the frame to the corresponding directory
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(os.path.join(directory, 'A', f'{count["A"]}.png'), frame)
    elif interrupt & 0xFF == ord('b'):
        cv2.imwrite(os.path.join(directory, 'B', f'{count["B"]}.png'), frame)
    elif interrupt & 0xFF == ord('c'):
        cv2.imwrite(os.path.join(directory, 'C', f'{count["C"]}.png'), frame)
    elif interrupt & 0xFF == ord('d'):
        cv2.imwrite(os.path.join(directory, 'D', f'{count["D"]}.png'), frame)
    elif interrupt & 0xFF == ord('e'):
        cv2.imwrite(os.path.join(directory, 'E', f'{count["E"]}.png'), frame)
    elif interrupt & 0xFF == ord('f'):
        cv2.imwrite(os.path.join(directory, 'F', f'{count["F"]}.png'), frame)
    elif interrupt & 0xFF == ord('g'):
        cv2.imwrite(os.path.join(directory, 'G', f'{count["G"]}.png'), frame)
    elif interrupt & 0xFF == ord('h'):
        cv2.imwrite(os.path.join(directory, 'H', f'{count["H"]}.png'), frame)
    elif interrupt & 0xFF == ord('i'):
        cv2.imwrite(os.path.join(directory, 'I', f'{count["I"]}.png'), frame)
    elif interrupt & 0xFF == ord('j'):
        cv2.imwrite(os.path.join(directory, 'J', f'{count["J"]}.png'), frame)
    elif interrupt & 0xFF == ord('k'):
        cv2.imwrite(os.path.join(directory, 'K', f'{count["K"]}.png'), frame)
    elif interrupt & 0xFF == ord('l'):
        cv2.imwrite(os.path.join(directory, 'L', f'{count["L"]}.png'), frame)
    elif interrupt & 0xFF == ord('m'):
        cv2.imwrite(os.path.join(directory, 'M', f'{count["M"]}.png'), frame)
    elif interrupt & 0xFF == ord('n'):
        cv2.imwrite(os.path.join(directory, 'N', f'{count["N"]}.png'), frame)
    elif interrupt & 0xFF == ord('o'):
        cv2.imwrite(os.path.join(directory, 'O', f'{count["O"]}.png'), frame)
    elif interrupt & 0xFF == ord('p'):
        cv2.imwrite(os.path.join(directory, 'P', f'{count["P"]}.png'), frame)
    elif interrupt & 0xFF == ord('q'):
        cv2.imwrite(os.path.join(directory, 'Q', f'{count["Q"]}.png'), frame)
    elif interrupt & 0xFF == ord('r'):
        cv2.imwrite(os.path.join(directory, 'R', f'{count["R"]}.png'), frame)
    elif interrupt & 0xFF == ord('s'):
        cv2.imwrite(os.path.join(directory, 'S', f'{count["S"]}.png'), frame)
    elif interrupt & 0xFF == ord('t'):
        cv2.imwrite(os.path.join(directory, 'T', f'{count["T"]}.png'), frame)
    elif interrupt & 0xFF == ord('u'):
        cv2.imwrite(os.path.join(directory, 'U', f'{count["U"]}.png'), frame)
    elif interrupt & 0xFF == ord('v'):
        cv2.imwrite(os.path.join(directory, 'V', f'{count["V"]}.png'), frame)
    elif interrupt & 0xFF == ord('w'):
        cv2.imwrite(os.path.join(directory, 'W', f'{count["W"]}.png'), frame)
    elif interrupt & 0xFF == ord('x'):
        cv2.imwrite(os.path.join(directory, 'X', f'{count["X"]}.png'), frame)
    elif interrupt & 0xFF == ord('y'):
        cv2.imwrite(os.path.join(directory, 'Y', f'{count["Y"]}.png'), frame)
    elif interrupt & 0xFF == ord('z'):
        cv2.imwrite(os.path.join(directory, 'Z', f'{count["Z"]}.png'), frame)

# Release the camera and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
