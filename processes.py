"""Программа для работы с процессами"""

import subprocess
import os
import multiprocessing as mp
import time

def main():
    print("Starting")
    print(f"PID : {os.getpid()}")
    welcome()

def welcome():
    print("hello")
    print(f"PID : {os.getpid()}")
    work()

def work():
    print("working")
    print(f"PID : {os.getpid()}")
    finish()

def finish():
    print("finished")
    print(f"PID : {os.getpid()}")



if __name__ == '__main__':
    proc_main = mp.Process(target=main)
    proc_main.start()
    proc = mp.Process(target=welcome)
    proc.start()