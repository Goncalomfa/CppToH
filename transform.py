import subprocess
from os import listdir
from os.path import isfile, join, splitext
from time import sleep

toConvertPath = "./toconvert"
convertedPath = "./converted"
exePath = "."

#def run(cmd):
#    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
#    return completed



def move(file):
    move_command = f"Move-Item -Path '{toConvertPath}/{file}' -Destination '{convertedPath}'"
    hello_info = subprocess.run(["powershell", "-Command", move_command], capture_output=True)
    if hello_info.returncode != 0:
        print("An error occured: %s", hello_info.stderr)
    else:
        print("Move command executed successfully!")
    print("-------------------------")


def test(file):
    fileWithoutT = file[1:]
    #hello_info = subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass"], capture_output=True)
    #sleep(2)
    #hello_info2 = subprocess.run(["powershell", "-Command", "Y"], capture_output=True)
    batch_command = f"{exePath}/Cpp2Java.ps1 {toConvertPath}/{file} {convertedPath}/{fileWithoutT}.java"
    #print("print ", batch_command)
    hello_info3 = subprocess.run(["powershell", "-Command", batch_command], capture_output=True)
    if hello_info3.returncode != 0:
        print("An error occured: %s", hello_info3.stderr)
    else:
        print("Batch command executed successfully!")
    print("-------------------------")



if __name__ == '__main__':
    files = [f for f in listdir(toConvertPath) if isfile(join(toConvertPath, f))]

    cpp = 0 #[]
    h = 0 #[]
    #nothing = 0
    for f in files:
        ext = splitext(f)[-1].lower()

        if ext == ".cpp":
            cpp+=1 #.append(f)
            #move(f)
            test(f)
        elif ext == ".h":
            h=+1 #.append(f)
            test(f)

        #else:
            #nothing+=1
    print(cpp, " cpp files")
    print(h, " h files")
    #print(nothing, " nope")
 
