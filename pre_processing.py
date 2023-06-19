import cv2

img = cv2.imread("img01_aug_256.jpg")


# Define the preprocess_image function
def preprocess_image(image):
    # Get the current size of the image
    height, width, channels = image.shape
    #print('Original image size:', height, 'x', width)

    # Resize the image while preserving the aspect ratio
    if width >= height:
        new_width = 256
        new_height = int(height * (256 / width))
    else:
        new_width = int(width * (256 / height))
        new_height = 256
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

    # Pad the resized image to 256 x 256
    pad_left = int((256 - new_width) / 2)
    pad_right = 256 - new_width - pad_left
    pad_top = int((256 - new_height) / 2)
    pad_bottom = 256 - new_height - pad_top
    padded_image = cv2.copyMakeBorder(resized_image, pad_top, pad_bottom, pad_left, pad_right, cv2.BORDER_CONSTANT, value=[255,255,255])

    # Get the size of the padded image
    height, width, channels = padded_image.shape
    #print('Padded image size:', height, 'x', width)
    return padded_image

output = preprocess_image(img)
cv2.imwrite("preprocessed_129.jpg", output)

img2 = cv2.resize(img,(256,256))
output2 = cv2.imwrite("resize_129.jpg",img2)