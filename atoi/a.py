#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Last Modification : 2020.02.13.
"""
import time
import os
from PIL import Image
import sys

# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ������ ����� �������� �Է¹޽��ϴ�.
directory = sys.argv[1]

# ������ ��� ������ �Է¹޽��ϴ�.
background_color = sys.argv[2]

# ������� ������ ������ �����մϴ�.
out_dir ="squared_images"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# input_files�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
for filename in input_files:
    # ��Ȥ �̹��� ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    exp = filename.strip().split('.')[-1]
    if exp not in "JPG jpg JPEG jpeg PNG png BMP bmp":
        continue

    # �̹����� �ҷ��ɴϴ�.
    image = Image.open(directory + "/" + filename)

    # �̹����� ũ�⸦ �˾Ƴ��ϴ�.
    Xdim, Ydim = image.size

    # ���簢������ ����� �ֱ� ���� ������ �ʿ��մϴ�.
    # X��� Y�� �� ��� ���̰� �� ���� �˾Ƴ��ϴ�.
    if Xdim > Ydim:
        # X�� ���̰� �� �� ����� ����Դϴ�.
        new_size = Xdim
        x_offset = 0
        y_offset = int((Xdim - Ydim) / 2)
    else:
        # Y�� ���̰� �� �� ����� ����Դϴ�.
        new_size = Ydim
        x_offset = int((Ydim - Xdim) / 2)
        y_offset = 0

    # ���ο� �̹����� �����մϴ�. �� �� ���簢���̰� ������ background_color �Դϴ�.
    new_image = Image.new("RGBA", (new_size, new_size), background_color)

    # �� �� ��濡 ���� �̹����� �����ϴ�. ������ ��ġ�� ������.
    new_image.paste(image, (x_offset, y_offset))

    # ����� �̹����� �����մϴ�.
    new_image.save(out_dir + "/" + filename)

    # �̹������� �ݾ��ݴϴ�.
    image.close()
    new_image.close()


# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
