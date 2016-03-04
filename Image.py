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

    def write_to_out(self):
        theoutfile = open(self.out_name, "w")
        theoutfile.write("%s \n %s \n %s \n" % (self.magic_number, (str(self.columns) + " " + str(self.rows)), self.max_colour_num))
        for num in range(self.rows):
            theoutfile.write(self.make_row(num) + "\n")
        theoutfile.close()

image_file = input("Enter the name of the image file: ")
output_file = input("Enter the name of the output file: ")

picture = PPMimage(image_file, output_file)
picture.write_to_out()