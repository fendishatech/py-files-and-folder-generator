import os

class FileGenerator:
    pass

class FolderGenerator:
    def __init__(self, folders = None, sub_folders =None, files =None, files_ext_name = "txt", template= None) -> None:
        self.folders = folders or []
        self.sub_folders = sub_folders or []
        self.files = files or []
        self.files_ext_name = files_ext_name
        self.template = template

    def generate(self):
        if not self.folders and self.files :
            self.create_files(self.files, self.files_ext_name)

        if self.folders:
            self.create_folders(self.folders)

    def create_folders(self, folders):
        # create folder, subfolder, sub files 
        for folder in folders:
            if not os.path.exists(folder):
                os.makedirs(folder)

    def create_files(self, files, ext):
        # Just a file or files with extension names and template
        for file in files:
            open(file + '.' + ext, 'a').close()

    def template(file, ext, template):
        if template:
            with open(file + ext, 'w') as f:
                f.write(template)






# class FileGenerator:
#     def __init__(self, folders=None, subfolders=None, files=None, extension='.txt', template=None, template_file=None):
#         self.folders = folders or []
#         self.subfolders = subfolders or []
#         self.files = files or []
#         self.extension = extension
#         self.template = template
#         self.template_file = template_file

#     def create_folders(self):
#         if not self.folders:
#             for file in self.files:
#                 filename = file + self.extension
#                 with open(filename, 'a') as f:
#                     if self.template:
#                         f.write(self.template)
#                     elif self.template_file:
#                         with open(self.template_file) as tf:
#                             templates = json.load(tf)
#                             if self.extension in templates and file in templates[self.extension]:
#                                 f.write(templates[self.extension][file])
#         else:
#             for folder in self.folders:
#                 os.makedirs(folder, exist_ok=True)
#                 for subfolder in self.subfolders:
#                     os.makedirs(os.path.join(folder, subfolder), exist_ok=True)
#                     for file in self.files:
#                         filename = os.path.join(folder, subfolder, file + self.extension)
#                         with open(filename, 'a') as f:
#                             if self.template:
#                                 f.write(self.template)
#                             elif self.template_file:
#                                 with open(self.template_file) as tf:
#                                     templates = json.load(tf)
#                                     if self.extension in templates and file in templates[self.extension]:
#                                         f.write(templates[self.extension][file])