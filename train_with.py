import os
import errno
from contextlib import contextmanager

BASE_DIR = './files'
FILE_NAME = 'test_text_with.txt'


def manual_write_to_file(addr: str, message: str):
    """
     get the address and write the message to file
     NOTE: if directory not Exists raise FileNotFoundError
    :param addr: Address of the file
    :param message: message to write
    :return: None
    """
    try:
        file = open(addr, 'w')
        file.write(message)
        file.close()
    except IOError as e:
        raise e


def write_to_file(addr: str, message: str):
    """
    get the address and append the message to file
    :param addr:
    :param message:
    :return:
    """
    try:
        with open(addr, 'a') as file:
            file.write(message)
    except IOError as e:
        if e.errno == errno.EEXIST:
            raise FileNotFoundError(f"The file {addr} does not exist.")
        else:
            raise IOError(f"An error occurred while trying to write to the file: {e}")


class MessageWriter:
    def __init__(self, base_dir: str, file_name: str):
        """
        first check the base_dir exists, if not create it
        :param base_dir: address of the file
        :param file_name: name of the file
        """
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        self.file_addr = os.path.join(base_dir, file_name)

    def __enter__(self):
        """
        if new file write to file
        else append to file
        :return:
        """
        if os.path.exists(self.file_addr):
            self.file = open(self.file_addr, 'a')
        else:
            self.file = open(self.file_addr, 'w')
        return self.file

    def __exit__(self, *args):
        self.file.close()


def custom_write_to_file(base_dir: str, file_name: str, message: str):
    try:
        with MessageWriter(base_dir, file_name) as file:
            file.write(message)
    except IOError as e:
        raise IOError(f"An error occurred while trying to write to the file: {e}")


class ContextMessageWriter:
    def __init__(self, base_dir: str, file_name: str):
        self.file = None
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        self.file_addr = os.path.join(base_dir, file_name)

    @contextmanager
    def open_file(self):
        try:
            if os.path.exists(self.file_addr):
                self.file = open(self.file_addr, 'a')
            else:
                self.file = open(self.file_addr, 'w')

            yield self.file
        except IOError as e:
            raise IOError(f"An error occurred while trying to write to the file: {e}")
        finally:
            self.file.close()


def context_write_to_file(base_dir: str, file_name: str, message: str):
    message_writer = ContextMessageWriter(base_dir, file_name)
    with message_writer.open_file() as file:
        file.write(message)


if __name__ == '__main__':
    # manual_write_to_file(os.path.join(BASE_DIR, FILE_NAME), 'hello world')
    # write_to_file(os.path.join(BASE_DIR, FILE_NAME), '\n Hello World3')
    # custom_write_to_file(BASE_DIR, FILE_NAME, "Hello World")
    context_write_to_file(BASE_DIR, FILE_NAME, "Hello World2")
