class MyFile():
    def __init__(self, name, content):
        self.name = name
        self.content = content


class SystemDirectories():
    def __init__(self, name):
        self.name = name
        self.directories = {}
        self.files = {}

    def file_exist(self, key):
        return key in self.files

    def get_file_content(self, key):  ###########################
        return self.files[key].content

    def add_file_content(self, key, content):  ################################
        if key in self.files:
            self.files[key].content += content
        else:
            self.files[key] = MyFile(key, content)

    def get_dir(self, key):  ####################
        if key not in self.directories:
            self.directories[key] = SystemDirectories(key)
        return self.directories[key]


class FileSystem:

    def __init__(self):
        self.head = SystemDirectories('head')

    def ls(self, path: str) -> List[str]:
        data = self.last_node(path)
        node = data[0]
        arr_path = data[1]
        if len(arr_path) > 0 and node.file_exist(arr_path[-1]):
            return [arr_path[-1]]
        result = []

        for key, value in node.directories.items():
            result.append(key)
        for key, value in node.files.items():
            result.append(key)

        result.sort()
        return result

    def mkdir(self, path: str) -> None:
        self.last_node(path)

    def last_node(self, path) -> SystemDirectories:
        arr_path = None
        if type(path) == str:
            arr_path = path.split("/")
        else:
            arr_path = path
        while ('' in arr_path):
            arr_path.remove('')

        node = self.head
        for i in arr_path:
            if node.file_exist(i):
                break
            node = node.get_dir(i)
        return [node, arr_path]

    def get_file_path(self, filePath):
        arr_path = filePath.split("/")
        arr_path.pop(0)
        file_to_add = arr_path[-1]
        arr_path.pop(-1)
        return [arr_path, file_to_add]

    def addContentToFile(self, filePath: str, content: str) -> None:
        data = self.get_file_path(filePath)
        arr_path = data[0]
        file_to_add = data[1]
        node = self.last_node(arr_path)[0]
        node.add_file_content(file_to_add, content)

    def readContentFromFile(self, filePath: str) -> str:
        data = self.get_file_path(filePath)
        arr_path = data[0]
        file_to_read = data[1]
        node = self.last_node(arr_path)[0]
        result = node.get_file_content(file_to_read)
        return result

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)