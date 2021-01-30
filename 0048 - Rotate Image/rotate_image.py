def rotate(image):
        """
        Do not return anything, modify matrix in-place instead.
        """
        image[:] = list(zip(*image[::-1]))