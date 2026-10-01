# MM, 7th, Read and Writing to Files

with open("pratice.txt", "r+") as file: #lets you read and write and appending
    content = file.read()
    content = "Chapter 1: \n" +"And Christopher Robin was sitting on his doorstep putting on his big boots"
    file.write(content)

with open("pratice.txt", "a") as file:
    file.write("\nWinnie the Pooh and the Blustery Day")