

class PPMimage():

    def __init__(self,infile,outfile):

        infile = open(infile)
        thefile = infile.read()
        thefile = thefile.split()

        self.in_name = infile
        self.out_name = outfile
        self.magic_number = thefile[0]
        self.columns = int(thefile[1])
        self.rows = int(thefile[2])
        self.max_colour_num = int(thefile[3])
        self.values = thefile[4:]

    def write_to_out(self):
        the_out_file = open(self.out_name, "w")
        the_out_file.write("%s \n %s \n %d \n" % (self.magic_number, (str(self.columns) + " " + str(self.rows)), int(self.max_colour_num)))
        for num in range(self.rows):
            the_out_file.write(" ".join(self.get_row(num)) + "\n")
        the_out_file.close()

    def get_row(self, row_num):
        num_elements_in_row = self.columns * 3
        start_of_row = row_num * num_elements_in_row
        temp_slice = self.values[int(start_of_row): int(start_of_row + num_elements_in_row)]
        return temp_slice

    def get_start(self, row_num):
        num_elements_in_row = self.columns * 3
        start_of_row = row_num * num_elements_in_row
        return int(start_of_row)

    def get_end(self,row_num):
        num_elements_in_row = self.columns * 3
        start_of_row = row_num * num_elements_in_row
        return int(start_of_row + num_elements_in_row)

    def negate_red(self):
        for num in range(0, len(self.values), 3):
                self.values[num] = str(self.max_colour_num - int(self.values[num]))

    def flatten_red(self):
        for num in range(0,len(self.values),3):
                self.values[num] = str(0)

    def flip_horizontal(self):
        for num in range(self.rows):
            row = self.get_row(num)
            count = 0
            for x in range(0, int(len(row)/2), 3):
                a = row[x]
                row[x] = row[len(row)-(3*(count+1))]
                row[len(row)-(3*(count+1))] = a
                b = row[x+1]
                row[x+1] = row[len(row)-((3*(count+1))-1)]
                row[len(row)-((3*(count+1))-1)] = b
                c = row[x+2]
                row[x+2] = row[len(row)-((3*(count+1))-2)]
                row[len(row)-((3*(count+1))-2)] = c
                count += 1
            self.values[self.get_start(num):self.get_end(num)] = row

    def grey_scale(self):
        for x in range(0, (len(self.values)), 3):
            y = x+1
            z = x+2
            average = int((int(self.values[x]) + int(self.values[y]) + int(self.values[z])) / 3)
            self.values[x] = str(average)
            self.values[y] = str(average)
            self.values[z] = str(average)

print ("Welcome to the Portable Pixmap (PPM) Image Editor!")
image_file = input("Please enter the name of the image file: ")
output_file = input("Please enter the name of the output file: ")
picture = PPMimage(image_file, output_file)

print ("Using the editor you can convert the image to greyscale, flip the image horizontally, negate red colour of image, and remove red colour from image.")
print ("Please enter y or n for each question below.")
if input("Would you like to convert to greyscale?: ") == "y":
    picture.grey_scale()
if input("Would you like to flip image horizontally?: ") == "y":
    picture.flip_horizontal()
if input("Would you like to negate red colour of image?: ") == "y":
    picture.negate_red()
if input ("Would you like to remove red colour from image?: ") == "y":
    picture.flatten_red()

picture.write_to_out()