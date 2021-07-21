import time, sys
# you will need to add panda (pip3 install panda)

def findName(id):
    # search in the excel file to find name based on id in the excel file
    print(f'Hi,your entered {id}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        try:
            id=input("enter an ID #:")
            findName(id)
            # do something time-cosnuming
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("Bye")
            sys.exit()

    sys.exit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
