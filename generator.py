import os

class FileGenerator:
    pass

class FolderGenerator:
    def __init__(self, folders = None, sub_folders =None, files =None, files_ext_name = ".txt", template= None) -> None:
        self.folders = folders or []
        self.sub_folders = sub_folders or []
        self.files = files or []
        self.files_ext_name = files_ext_name
        self.template = template

    def create_folders(self):
        # Just a file or files with extension names and template
        if not self.folders and self.files :
            for file in self.files:
                open(file +self.files_ext_name, 'a').close()
                if self.template:
                    with open(file +self.files_ext_name, 'w') as f:
                        f.write(self.template)
        # create folder, subfolder, sub files 
        if self.folders : 
            for folder in self.folders:
                if not os.path.exists(folder):
                    os.makedirs(folder)
                if self.sub_folders :
                    for sub_folder in self.sub_folders:
                        if not os.path.exists(sub_folder):
                            os.makedirs(os.path.join(folder, sub_folder))
                        if sub_folder and self.files and self.files_ext_name :
                            for file in self.files:
                                if not os.path.exists(file) :
                                    filename = os.path.join(folder, sub_folder, file + self.files_ext_name)
                                    if self.template:
                                        with open(file +self.files_ext_name, 'w') as f:
                                            f.write(self.template)
                if self.files and self.files_ext_name :
                    for file in self.files:
                        if not os.path.exists(file) :
                            filename = os.path.join(folder, sub_folder, file + self.files_ext_name)
        else:
            pass


