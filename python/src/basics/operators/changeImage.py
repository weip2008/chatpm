from PIL import Image

def makeTransparent(fileIn, fileOut):
    r,g,b=54,105,148
    img = Image.open(fileIn)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []

    # print(f'The total pixel of this image is {len(datas)}.')
    with open('data.txt', '+w') as f:
        for item in datas:
            f.write(f'{item[0]},{item[1]},{item[2]}\n')

    for item in datas:
        if item[0] == r and item[1]==g and item[2]==b:
            newData.append((255,255,255,0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(fileOut, "PNG")
    print("Successful")

if __name__ == '__main__':
    # makeTransparent("fighter.png", "fighter5.png")
    makeTransparent("python.png", "python1.png")
