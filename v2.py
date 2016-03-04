class PPMimage():

    def __init__(self,infile,outfile):

        infile = open(image_file)
        thefile = infile.read()
        thefile = thefile.split()

        self.in_name = infile
        self.out_name = outfile
        self.magic_number = thefile[0]
        self.columns = int(thefile[1])
        self.rows = int(thefile[2])
        self.max_colour_num = int(thefile[3])
        self.values = thefile[4:]

    def make_row(self,row_num):
        num_elements_in_row = self.columns * 3
        starting_row = row_num * num_elements_in_row
        temp_slice = self.values[int(starting_row): int(starting_row + num_elements_in_row)]
        return " ".join(temp_slice)

    def write_all_to_out(self):
        theoutfile = open(self.out_name, "w")
        self.write_variables_to_out()
        for num in range(self.rows):
            theoutfile.write(self.make_row(num) + "\n")
        theoutfile.close()

    def write_variables_to_out(self):
        theoutfile = open(self.out_name, "w")
        theoutfile.write("%s \n %s \n %d \n" % ((self.magic_number), (str(self.columns) + " " + str(self.rows)), int(self.max_colour_num)))

    def write_row_to_out(self, row):
        theoutfile = open(self.out_name, "w")
        theoutfile.write(row + "\n")

    def negate_red(self):
        #for loop every 3rd element in row. Take value & subtract from 255. New value.
        for num in range(self.rows, 3):
            pass

    def flip_horizontal(self):
        #crashing and burning

        for num in range(self.rows):
            temp_row = (self.make_row(num)).split()
            #gotta split into groups of 3s
            temp_row = " ".join(temp_row[::-1])
            self.write_row_to_out(temp_row)
        theoutfile.close()

    def grey_scale(self):
        #for every 3 elements in row, add together divide by 3, each element becomes that value
        pass
    def flatten_red(self):
        #every 3rd element in row, make it 00
        pass
image_file = input("Enter the name of the image file: ")
output_file = input("Enter the name of the output file: ")

picture = PPMimage(image_file, output_file)
picture.flip_horizontal()


