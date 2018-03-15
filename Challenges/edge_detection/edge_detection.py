"""
codewars.com
Challenge Fun #20: Edge Detection
challenge written by: myjinxin2015

Task

IONU Satellite Imaging, Inc. records and stores very large images using run
length encoding. You are to write a program that reads a compressed image,
finds the edges in the image, as described below, and outputs another
compressed image of the detected edges.

A simple edge detection algorithm sets an output pixel's value to be the
maximum absolute value of the differences between it and all its surrounding
pixels in the input image. Consider the input image below:

image looks like:

15  15  15  15  100 100 100
100 100 100 100 100 100 100
100 100 100 100 100 25  25
175 175 25  25  25  25  25
175 175 25  25  25  25  25

the result looks like:

85  85 85  85 85  0  0
85  85 85  85 85 75 75
75  75 75  75 75 75 75
75 150 150 75 75 75  0
 0 150 150  0  0  0  0

 The upper left pixel in the output image is the maximum of the values
 |15-15|,|15-100|, and |15-100|, which is 85. The pixel in the 4th row,
 2nd column is computed as the maximum of
 |175-100|, |175-100|, |175-100|, |175-175|, |175-25|, |175-175|,|175-175|,
 and |175-25|, which is 150.

Images contain 2 to 1,000,000,000 (10^9) pixels. All images are encoded using
run length encoding (RLE). This is a sequence of pairs, containing pixel value
(0-255) and run length (1-10^9). Input images have at most 1,000 of these
pairs. Successive pairs have different pixel values. All lines in an image
contain the same number of pixels.

For the iamge as the example above, the RLE encoding string is
"7 15 4 100 15 25 2 175 2 25 5 175 2 25 5"

Each image starts with the width, in pixels(means the first number 7)
 This is followed by the RLE pairs(two number is a pair).
 7      ----> image width
 15 4   ----> a pair(color value + number of pixel)
 100 15       ...........ALL.......................
 25 2         ..........THESE......................
 175 2        ...........ARE.......................
 25 5         ..........PAIRS......................
 175 2        ...........LIKE......................
 25 5         ..........ABOVE......................


Your task is to calculate the result by using the edge detection algorithm
above. Returns a encoding string in the same format as the input string.

Exaple

Please see examples in the example test block.
Input/Output

    [input] string image

    A RLE string of image.

    [output] a string

    A RLE string calculate by using the edge detection algorithm.

"""

"""
TODO:
Done    1. generate image pixlel string
Done    2. write code to navigate adjacent pixles and return them
Done    3. evaluate adjacent pixels and return the max absolute difference
        4. return new image
Done    5. print the image
"""


def edge_detection(image):
    width, input_image = gen_input_image(image)
    output_image = get_output_image(width, input_image)
    out_img = gen_rle_output(width, output_image)
    return out_img


def gen_input_image(image):
    img_description = [int(x) for x in image.split(" ")]
    width = img_description[0]
    img = []
    for i in range(1, len(img_description), 2):
        for _ in range(img_description[i + 1]):
            img.append(img_description[i])

    return width, img


def print_img(width, pixels):
    for i in range(len(pixels)):
        print("%4s" % pixels[i], end="")
        if i % width == width - 1:
            print("\n")


def get_adjacent_pixels(index, width, pix):
    # strore value of len(pix) to optimize performance
    pix_len = len(pix)
    # first special cases
    # the 4 corners
    if index == 0:  # top left corner
        return [pix[1], pix[width], pix[width + 1]]
    elif index == width - 1:  # top right corner
        return [pix[index - 1], pix[index + width - 1], pix[index + width]]
    elif index == pix_len - width:  # bottom left corner
        return [pix[pix_len - width * 2], pix[pix_len - width * 2 + 1], pix[pix_len - width + 1]]
    elif index == pix_len - 1:  # bottom right corner
        return [pix[pix_len - 2], pix[pix_len - width - 2], pix[pix_len - width - 1]]
    # the edges
    elif 0 < index < width:  # top edge
        return [pix[index - 1], pix[index + 1],
                pix[index + width],
                pix[index + width - 1], pix[index + width + 1]]
    elif 0 < index < pix_len - width and index % width == 0:  # left edge
        return [pix[index - width], pix[index - width + 1],
                pix[index + 1],
                pix[index + width], pix[index + width + 1]]
    elif pix_len - width < index < pix_len - 1:  # bottom edge
        return [pix[index - width - 1], pix[index - width + 1],
                pix[index - width],
                pix[index - 1], pix[index + 1]]
    elif width - 1 < index < pix_len - 1 and index % width == width - 1:  # right edge
        return [pix[index - width - 1], pix[index - width],
                pix[index - 1],
                pix[index + width - 1], pix[index + width]]
    # general/average case
    else:
        return [pix[index - width - 1], pix[index - width], pix[index - width + 1],
                pix[index - 1], pix[index + 1],
                pix[index + width - 1], pix[index + width], pix[index + width + 1]
                ]


def get_output_pixel(pixel_index, width, pixels):
    ad_pixels = get_adjacent_pixels(pixel_index, width, pixels)
    # for i in range(len(ad_pixels)):
    #     ad_pixels[i] = abs(ad_pixels[i] - pixels[pixel_index])
    k = max([abs(i - pixels[pixel_index]) for i in ad_pixels])
    return k


def get_output_image(width, input_image):
    return [get_output_pixel(x, width, input_image) for x in range(len(input_image))]


def gen_rle_output(width, output_image):
    key = [str(width)]
    cur_pix = output_image[0]
    count = 0
    for i in range(len(output_image)):
        if output_image[i] == cur_pix:
            count += 1
            if i == len(output_image) - 1:
                key.append(str(cur_pix))
                key.append(str(count))
        else:
            key.append(str(cur_pix))
            key.append(str(count))
            cur_pix = output_image[i]
            count = 1
    return " ".join(key)


def test():
    ex_in = "7 15 4 100 15 25 2 175 2 25 5 175 2 25 5"
    ex_img = gen_input_image(ex_in)
    img = [_ for _ in range(25)]
    width = 7
    print_img(width, pixels=img)
    print(f"top left corner: {get_adjacent_pixels(0, width, img)}")
    print(f"top right corner:{get_adjacent_pixels(width - 1, width, img)}")
    print(f"bottom left corner:{get_adjacent_pixels(len(img) - width, width, img)}")
    print(f"bottom right corner:{get_adjacent_pixels(len(img) - 1, width, img)}")
    print("-" * 30)
    print(f"top edge:{get_adjacent_pixels(width//2, width, img)}")
    print(f"left edge:{get_adjacent_pixels((len(img)//2)-(width//2), width, img)}")
    print(f"bottom edge:{get_adjacent_pixels(len(img)-(width//2), width, img)}")
    print(f"right edge:{get_adjacent_pixels((len(img)//2)+(width//2), width, img)}")
    print("-" * 30)
    print(f"average case:{get_adjacent_pixels(len(img)//2, width, img)}")
    print("-" * 30)
    print(get_output_pixel(0, width, img))
    print("-" * 30)
    out = get_output_image(width, ex_img)
    print_img(width, out)
    print("-" * 30)
    print(gen_rle_output(width, out))


if __name__ == '__main__':
    image = '7 15 4 100 15 25 2 175 2 25 5 175 2 25 5'
    result = '7 85 5 0 2 85 5 75 10 150 2 75 3 0 2 150 2 0 4'
    print(edge_detection(image) == result)
