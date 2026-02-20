import os

class ioHelpers:

    def __init__(self, autoresponse_path):
        self.autoresponse_path = autoresponse_path
        self.file_list = []
        self.file_types_list = []
        self.file_name_list = []

    def load_responses(self):
        self.file_list = os.listdir(self.autoresponse_path)
        for file in self.file_list:
            file, filetype = os.path.splitext(file)
            self.file_name_list.append(file)
        print(self.file_name_list)