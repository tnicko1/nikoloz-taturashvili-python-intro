from datetime import datetime

class TimeStampMixin:
    def __init__(self):
        self._created_at = datetime.now()
        self._modified_at = self._created_at

    def get_creation_time(self):
        return self._created_at

    def get_modification_time(self):
        return self._modified_at

    def update_modification_time(self):
        self._modified_at = datetime.now()


class File(TimeStampMixin):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def update_file_name(self, new_file_name):
        self.file_name = new_file_name
        self.update_modification_time()


class User(TimeStampMixin):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def update_name(self, new_name):
        self.name = new_name
        self.update_modification_time()


def main():
    file = File("document.txt")
    print("File created at:", file.get_creation_time())
    print("File modified at:", file.get_modification_time())

    file.update_file_name("new_document.txt")
    print("File name updated. Modified at:", file.get_modification_time())

    user = User("john_doe")
    print("\nUser created at:", user.get_creation_time())
    print("User modified at:", user.get_modification_time())

    user.update_name("jane_doe")
    print("Username updated. Modified at:", user.get_modification_time())


if __name__ == '__main__':
    main()