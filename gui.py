import os
import sys
import tkinter as tk
import datetime
from automation import automation
from serial_number import get_client_serial_number
from getUser import getUser
from customerData import expiry_date,CLIENT_SERIAL_NUMBER,get_serial_only
import time


class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()
    def flush(self):
        for f in self.files:
            f.flush()

class LogWidget(tk.Text):
    def __init__(self, master, *args, **kwargs):
        tk.Text.__init__(self, master, *args, **kwargs)
        self.config(bg='white', fg='black')
        self.yscroll = tk.Scrollbar(master, orient='vertical', command=self.yview)
        self.configure(yscrollcommand=self.yscroll.set)
        self.yscroll.pack(side='right', fill='y')
        self.pack(side='left', fill='both', expand=True)
        self.tag_config("INFO", foreground="black")
        self.tag_config("ERROR", foreground="red")

    def write(self, text, tag="INFO"):
        self.insert(tk.END, text, tag)
        self.see(tk.END)
    def flush(self):
        pass

def run_function(function, log_widget):
    # Code to run the selected function
    log_widget.write(f"Running function: {function.__name__}\n")
    try:
        if CLIENT_SERIAL_NUMBER != get_client_serial_number():
            get_user_btn.config(state=tk.DISABLED)
            get_serial_number_btn.config(state=tk.DISABLED)
            start_automation_btn.config(state=tk.DISABLED)
            log_widget.write(f"Error: Client serial number is not valid.\n", tag="ERROR")
        else:
            function()

    except Exception as e:
        log_widget.write(f"Error: {e}\n", tag="ERROR")

# Define a function to update the time label
def update_time():
    global remaining_time
    remaining_time = expiry_date - datetime.datetime.now()
    if remaining_time.total_seconds() > 1:
        time_label.config(text=f"Time left: {remaining_time.days} days {remaining_time.seconds // 3600} hours {remaining_time.seconds % 3600 // 60} minutes {remaining_time.seconds % 60} seconds")
        time_label.after(1000, update_time)
    else:
        time_label.config(text="Time is over")
        get_user_btn.config(state=tk.DISABLED)
        get_serial_number_btn.config(state=tk.DISABLED)
        start_automation_btn.config(state=tk.DISABLED)
        time.sleep(1)
        sys.exit()


# Create the GUI window
root = tk.Tk()







# Create a Label widget to display the remaining time
time_label = tk.Label(root, text="", font=("Helvetica", 16))
time_label.pack(pady=10)

# Create a LogWidget to display the output of the functions
log_text = LogWidget(root)
sys.stdout = Tee(sys.stdout, log_text)

# Get the path to the current directory
dir_path = os.path.dirname(os.path.realpath(__file__))












# Define a function to update the time label
update_time()


# Create buttons for each function
if not get_serial_only:
    get_user_btn = tk.Button(root, text="Get User", state=tk.DISABLED)
    get_serial_number_btn = tk.Button(root, text="Get Serial Number", command=lambda: run_function(get_client_serial_number, log_text))
    start_automation_btn = tk.Button(root, text="Automation", state=tk.DISABLED)
else:
    get_user_btn = tk.Button(root, text="Get User", command=lambda: run_function(getUser, log_text))
    get_serial_number_btn = tk.Button(root, text="Get Serial Number", command=lambda: run_function(get_client_serial_number, log_text))
    start_automation_btn = tk.Button(root, text="Automation", command=lambda: run_function(automation, log_text))

get_user_btn.pack(pady=10)
get_serial_number_btn.pack(pady=10)
start_automation_btn.pack(pady=10)


def print_remaining_time():
    print(remaining_time.total_seconds())
example_btn = tk.Button(root, text="get time now", command=lambda: run_function(print_remaining_time, log_text))
example_btn.pack(pady=10)



# Start the GUI event loop
root.mainloop()

#pyinstapyinstaller --onefile gui.py