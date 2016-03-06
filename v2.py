import itertools


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

    def negate_red(self): #THIS WORKS
        for num,value in enumerate(self.values):
            if num % 3 == 0:
                self.values[num] = str(self.max_colour_num - int(value))

    def flatten_red(self): #THIS WORKS TOO
        for num,value in enumerate(self.values):
            if num % 3 == 0:
                self.values[num] = str(0)

    def split_into_RBG(self,a_list):
        temp_matrix = []
        for n in range(0, len(a_list), 3):
            temp_matrix.append(a_list[n:(n+3)])
        return temp_matrix

    def flip_horizontal(self):
        pass

    def grey_scale(self): #This works but its kinda ugly...
        temp_matrix = self.split_into_RBG(self.values)
        for l in temp_matrix:
            average = (int(l[0])+int(l[1])+int(l[2])) / 3
            for x in range(3):
                l[x] = str(int(average))
        temp_matrix = list(itertools.chain(*temp_matrix))
        self.values = temp_matrix

print ("Welcome to the Portable Pixmap (PPM) Image Editor!")
image_file = input("Please enter the name of the image file: ")
output_file = input("Please enter the name of the output file: ")
picture = PPMimage(image_file, output_file)
print ("Using the editor you can convert the image to greyscale, flip the image horizontally, negate red colour of image, and remove red colour from image. Please enter y or n for each question below.")
if input("Would you like to convert to greyscale?: ") == "y":
    picture.grey_scale()
if input("Would you like to flip image horizontally?: ") == "y":
    picture.flip_horizontal()
if input("Would you like to negate red colour of image?: ") == "y":
    picture.negate_red()
if input ("Would you like to remove red colour from image?: ") == "y":
    picture.flatten_red()

picture.write_to_out()