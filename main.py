from subprocess import Popen, PIPE
import os
import time
def run_sub(coms):    
    with Popen(coms, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True) as proc:
        stdout, stderr = proc.communicate()
        if proc.returncode == 1:
            print(stderr.decode("utf-8"))  

def get_full_path(rel_path):
    return os.path.join(os.getcwd(),rel_path)

def main():            
    file = input("Paste full file path of the file you're downloading:\n").strip("\"'")
    ofw_path = get_full_path("OpenedFilesView\\OpenedFilesView.exe")
    while True:
        run_sub([ofw_path, "/scomma", "opened_files.txt", "/filefilter", file])            
        with open("opened_files.txt",encoding="utf-8") as f:
            opened_files = f.read()
        if opened_files.encode() == b'\xef\xbb\xbf':
            print("file isn't downloading. shutting down pc")
            os.system('shutdown /s /t 300')
            return
        else:
            print("file is downloading")
            print(opened_files.split(',')[0])
        time.sleep(60)
if __name__ == "__main__":
    main()  