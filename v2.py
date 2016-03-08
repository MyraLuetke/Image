from random import randint

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

    def flip(self, count, n, row, x):
        a = row[x+n]
        row[x+n] = row[len(row)-((3*(count+1))-n)]
        row[len(row)-((3*(count+1))-n)] = a

    def flip_horizontal(self):
        for num in range(self.rows):
            row = self.get_row(num)
            count = 0
            for x in range(0, int(len(row)/2), 3):
                for n in range(3):
                    self.flip(count,n,row,x)
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

    def extreme_contrast(self):
        for num in range(len(self.values)):
            if int(self.values[num]) > (self.max_colour_num/2):
                self.values[num] = str(self.max_colour_num)
            else:
                self.values[num] = str(0)

    def random_noise(self):
        for num in range(len(self.values)):
            rand_number = randint(0, max(0,((int(self.values[num])-1))))
            add_or_subtract = randint(0,1)
            if add_or_subtract == 1:
                if (int(self.values[num]) + rand_number) > self.max_colour_num:
                    self.values[num] = str(self.max_colour_num)
                else:
                    self.values[num] = str(int(self.values[num]) + rand_number)
            else:
                if (int(self.values[num]) - rand_number) < 0:
                    self.values[num] = str(0)
                else:
                    self.values[num] = str(int(self.values[num]) - rand_number)

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