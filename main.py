from win32com.client import Dispatch

file = "insert excel file directory"
wordlist = 'insert password compilation text file'

word = open(wordlist, 'r')
allpass = word.readlines()
word.close()

for password in allpass:
    password = password.strip()
    instance = Dispatch('Excel.Application')

    try:
        instance.Workbooks.Open(file, False, True, None, password)
        print("password is " + password)
        break
    except Exception as e:
        print("wrong pw: " + password)
        pass