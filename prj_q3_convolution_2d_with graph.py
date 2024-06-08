import matplotlib as pl
def convolve2d(image, kernel):
    if len(image) == 0 or len(image[0]) == 0:
        raise ValueError("تصویر ورودی نباید خالی باشد.")
    
    image_height = len(image)
    image_width = len(image[0])
    kernel_height = len(kernel)
    kernel_width = len(kernel[0])
    
    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1

    if output_height <= 0 or output_width <= 0:
        raise ValueError("ابعاد کرنل بزرگتر از ابعاد تصویر است.")
    
    output = [[0 for _ in range(output_width)] for _ in range(output_height)]
    
    for i in range(output_height):
        for j in range(output_width):
            sum = 0
            for ki in range(kernel_height):
                for kj in range(kernel_width):
                    sum += image[i + ki][j + kj] * kernel[ki][kj]
            output[i][j] = sum
    
    return output

sobel_x = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

sobel_y = [
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
]

def edge_detection(image):
    edge_x = convolve2d(image, sobel_x)
    edge_y = convolve2d(image, sobel_y)
    
    output_height = len(edge_x)
    output_width = len(edge_x[0])
    
    edge_magnitude = [[0 for _ in range(output_width)] for _ in range(output_height)]
    
    for i in range(output_height):
        for j in range(output_width):
            edge_magnitude[i][j] = int((edge_x[i][j]**2 + edge_y[i][j]**2) ** 0.5)
    
    return edge_magnitude

rows = int(input())
cols = int(input())

image = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = input().split()
        row.append(element)
    image.append(row)

if rows < len(sobel_x) or cols < len(sobel_y[0]):
    raise ValueError("ابعاد تصویر باید بزرگتر یا مساوی ابعاد کرنل باشد.")

edge_image = edge_detection(image)

for row in edge_image:
    print(row)


pl.plot(edge_image)
plt.title()
plt.axis(off)
pl.show()