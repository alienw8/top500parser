from datetime import datetime


def log(*texts: str):
    string = str(datetime.now())
    for text in texts:
        string += f', {text}'
    print(string)
    with open('logs', 'a') as file:
        file.write(string+'\n')
