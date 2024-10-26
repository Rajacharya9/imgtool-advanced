import cv2
import numpy as np
import exifread

class ImageProcessor:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)

    def resize(self, width, height):
        return cv2.resize(self.image, (width, height))

    def to_grayscale(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def rotate(self, angle):
        (h, w) = self.image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        return cv2.warpAffine(self.image, M, (w, h))

    def apply_filter(self, filter_type="gaussian"):
        if filter_type == "gaussian":
            return cv2.GaussianBlur(self.image, (5, 5), 0)
        elif filter_type == "edge":
            return cv2.Canny(self.image, 100, 200)
        else:
            raise ValueError("Invalid filter type")

    def adjust_brightness_contrast(self, brightness=0, contrast=0):
        new_image = np.int16(self.image)
        new_image = new_image * (contrast/127+1) - contrast + brightness
        new_image = np.clip(new_image, 0, 255)
        return np.uint8(new_image)

    def reduce_noise(self, method="median"):
        if method == "median":
            return cv2.medianBlur(self.image, 5)
        elif method == "bilateral":
            return cv2.bilateralFilter(self.image, 9, 75, 75)
        else:
            raise ValueError("Invalid noise reduction method")

    def histogram_equalization(self):
        img_yuv = cv2.cvtColor(self.image, cv2.COLOR_BGR2YUV)
        img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
        return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    def detect_faces(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(self.image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        return self.image

    def extract_metadata(self, image_path):
        with open(image_path, 'rb') as img_file:
            tags = exifread.process_file(img_file)
        return tags

    def save_image(self, output_path, image):
        cv2.imwrite(output_path, image)
