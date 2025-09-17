
# Unix-Like Shell in Python

## 📌 Overview
This project implements a simple Unix-like shell using Python.  
It supports basic commands such as listing files, directories, showing date/time, file operations, and system info.

---

## 🚀 Features
- `list` → Show files in current directory
- `dirs` → Show directories in current directory
- `date` → Show system date (dd-mon-yyyy)
- `time` → Show time (HH:MM:SS)
  - `time -hours` → Show hours only
  - `time -mins` → Show minutes only
  - `time -secs` → Show seconds only
- `cat <file>` → Show file content
- `head -5 <file>` → Show first 5 lines
- `tail -5 <file>` → Show last 5 lines
- `copy_file <src> <dest>` → Copy file
- `remove_file <file>` → Delete file
- `empty_file <file>` → Empty file contents
- `ipconfig` → Show system IP
- `pwd` → Print working directory
- `clear` → Clear screen
- `exit` → Exit shell

---

## 🛠 How to Run
1. Install Python (>= 3.6).
2. Open terminal inside project folder.
3. Run:
   ```bash
   python myshell.py
   ```
4. Use commands at `myshell>` prompt.

---

## 📂 Example Usage
```
myshell> list
myshell> dirs
myshell> date
myshell> time
myshell> pwd
myshell> cat sample.txt
myshell> head -5 sample.txt
myshell> tail -5 sample.txt
myshell> exit
```

---

## 📜 Author
Developed as part of a Python shell project assignment.
