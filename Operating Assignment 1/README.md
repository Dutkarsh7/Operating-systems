Linux Process Management Experiment

Python scripts demonstrating Linux process creation and control using the os module.

Contents

Child process creation

Running commands with exec()

Zombie and orphan process simulation

Reading process info from /proc

Priority adjustment with nice()

Files

task1_process_creation.py – child process management

task2_exec_command.py – execute Linux commands

task3_zombie_orphan.py – zombie & orphan demo

task4_inspect_proc.py – inspect /proc details

task5_priority.py – priority & scheduling

Requirements

Python 3

Linux environment (Ubuntu, WSL, etc.)

Usage

Run any script from terminal, e.g.:

python3 task1_process_creation.py

Notes

For Task 3, monitor zombies with ps -el | grep defunct in another terminal.

Scripts are Linux-specific and won’t run on Windows CMD.

Stop long processes with Ctrl+C.