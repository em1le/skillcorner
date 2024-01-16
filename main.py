from log import Log
from reader import Reader

if __name__ == '__main__':
    file_path = input("Enter the file path : ")
    data = Reader.extract_data(file_path)
    log = Log(data)
    for line in log.lines:
        new_data = line.process_line()
        print(f"{line.position} : {new_data}")
