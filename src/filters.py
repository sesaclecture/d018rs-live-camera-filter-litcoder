import cv2
import numpy as np


class Filters:
    # TODO: Image kernels
    Kernels = {
        "Original": np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
        "Blur": np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9,
        "Gaussian Blur": np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])/16,
        "Sharpen": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]),
        "Sobel (X)": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
        "Sobel (Y)": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),
        "Edge detection": np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]),
        "Emboss": np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
    }

    def __init__(self, kernels=Kernels):
        self.kernels = kernels

        # TODO: Implement internal variables
        self.filter_idx = 0
        self.filter_names = list(self.kernels.items())

    def apply_filter(self, frame, filter_name) -> np.array:
        # TODO: Apply the selected filter kernel to the frame
        kernel = self.kernels[filter_name]
        return cv2.filter2D(frame, -1, kernel)

    def get_current_filter_name(self) -> str:
        # TODO: Return currently set kernels's name
        return self.filter_names[self.filter_idx][0]

    def switch_next_filter(self):
        # TODO: Update currently selected kernel to the next
        self.filter_idx = (self.filter_idx + 1) % (len(self.kernels))

    def switch_previous_filter(self):
        # TODO: Update currently selected kernel to the previous
        self.filter_idx = (self.filter_idx - 1) % (len(self.kernels))
