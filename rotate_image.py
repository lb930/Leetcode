# https://stackoverflow.com/questions/29139350/difference-between-ziplist-and-ziplist/29139418
# * unpacks elements in a list into separate arguments for the zip function
m = [[1,2,3],[4,5,6],[7,8,9]]
print(*m)
print(list(zip(*m)))

def rotate_image(image):
    image[:] = list(zip(*image[::-1]))