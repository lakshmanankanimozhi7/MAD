


class ReadAndWriteTextFileHelper:
    file_path = "/Users/kanimozhi/PycharmProjects/msd/src/tests/text_file/"


    def create_and_add_data_in_txt_file(self,file_name,data):
        text_file = open(self.file_path+"%s.txt"%file_name, "w+")
        text_file.write("%s\r\n" % data)
        text_file.close()

    def add_data_to_existing_file(self,file_name,data):
        text_file = open(self.file_path+"%s.txt"%file_name, "a+")
        text_file.write(data+"\r\n")
        text_file.close()

    def read_data_from_txt_file(self,file_name):
        file_path =self.file_path+"%s.txt" % file_name
        text_file = open(file_path, "r+")
        a = text_file.readlines()
        num_lines = 0
        with open(file_path, 'r') as text_file:
            for line in text_file:
                num_lines += 1

        return a,num_lines
