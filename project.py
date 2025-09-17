import os
import shutil
import datetime
import socket
import sys

def list_files():
    for f in os.listdir():
        if os.path.isfile(f):
            print(f)

def list_dirs():
    for f in os.listdir():
        if os.path.isdir(f):
            print(f)

def show_date():
    today = datetime.date.today()
    print(today.strftime("%d-%b-%Y").lower())

def show_time(option=None):
    now = datetime.datetime.now()
    if option == "-hours":
        print(now.hour)
    elif option == "-mins":
        print(now.minute)
    elif option == "-secs":
        print(now.second)
    else:
        print(now.strftime("%H:%M:%S"))

def cat_file(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: File not found.")

def head_file(filename, n=5):
    try:
        with open(filename, "r") as f:
            for i, line in enumerate(f):
                if i >= n:
                    break
                print(line, end="")
    except FileNotFoundError:
        print("Error: File not found.")

def tail_file(filename, n=5):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines[-n:]:
                print(line, end="")
    except FileNotFoundError:
        print("Error: File not found.")

def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"File copied from {src} to {dest}")
    except FileNotFoundError:
        print("Error: Source file not found.")

def remove_file(filename):
    try:
        os.remove(filename)
        print(f"File {filename} deleted.")
    except FileNotFoundError:
        print("Error: File not found.")

def empty_file(filename):
    try:
        open(filename, "w").close()
        print(f"File {filename} emptied.")
    except Exception as e:
        print("Error:", e)

def show_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        print("IP Address:", ip)
    except Exception as e:
        print("Error getting IP:", e)

def pwd():
    print(os.getcwd())

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    print("Welcome to Mini Unix-like Shell (Python). Type 'exit' to quit.")

    while True:
        try:
            cmd = input("shell> ").strip().split()

            if not cmd:
                continue

            command = cmd[0]

            # ---- FILE & DIR COMMANDS ----
            if command == "list":
                list_files()
            elif command == "dirs":
                list_dirs()
            elif command == "date":
                show_date()
            elif command == "time":
                if len(cmd) > 1:
                    show_time(cmd[1])
                else:
                    show_time()
            elif command == "cat":
                if len(cmd) > 1:
                    cat_file(cmd[1])
                else:
                    print("Usage: cat <filename>")
            elif command == "head":
                if len(cmd) > 2 and cmd[1].startswith("-"):
                    head_file(cmd[2], int(cmd[1][1:]))
                elif len(cmd) > 1:
                    head_file(cmd[1])
                else:
                    print("Usage: head -n <filename>")
            elif command == "tail":
                if len(cmd) > 2 and cmd[1].startswith("-"):
                    tail_file(cmd[2], int(cmd[1][1:]))
                elif len(cmd) > 1:
                    tail_file(cmd[1])
                else:
                    print("Usage: tail -n <filename>")
            elif command == "copy_file":
                if len(cmd) == 3:
                    copy_file(cmd[1], cmd[2])
                else:
                    print("Usage: copy_file <src> <dest>")
            elif command == "remove_file":
                if len(cmd) > 1:
                    remove_file(cmd[1])
                else:
                    print("Usage: remove_file <filename>")
            elif command == "empty_file":
                if len(cmd) > 1:
                    empty_file(cmd[1])
                else:
                    print("Usage: empty_file <filename>")

            # ---- SYSTEM COMMANDS ----
            elif command == "ifconfig":
                show_ip()
            elif command == "pwd":
                pwd()
            elif command == "clear":
                clear()
            elif command == "exit":
                print("Shell exiting...")
                sys.exit(0)

            else:
                print("Invalid command!")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
    print("Shell has been invoked successfully.")