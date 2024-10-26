# imgtool

An advanced Python image processing tool using OpenCV. Provides functionality for resizing, filtering, noise reduction, face detection, histogram equalization, metadata extraction, and batch processing.

## Installation

```bash
pip install imgtool
```

## Usage

```python
from imgtool.image_processor import ImageProcessor

processor = ImageProcessor('path_to_image.jpg')
# Adjust brightness and contrast
adjusted_image = processor.adjust_brightness_contrast(brightness=30, contrast=50)

# Reduce noise
denoised_image = processor.reduce_noise(method="median")

# Detect faces
face_detected_image = processor.detect_faces()

processor.save_image('output_image.jpg', face_detected_image)
```
