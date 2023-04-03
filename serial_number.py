import subprocess
import platform

def get_client_serial_number():
    
    def get_serial_number():
        serial_number = None
        try:
            output = subprocess.check_output(["system_profiler", "SPHardwareDataType"])
            output = output.decode("utf-8")
            for line in output.split("\n"):
                if "Serial Number" in line:
                    serial_number = line.split(":")[1].strip()
                    break
        except Exception as e:
            print(f"Error: {e}")
        return serial_number


    if platform.system() == 'Darwin':
        serial_number = get_serial_number()
    elif platform.system() == 'Windows':
        try:
            import wmi
            c = wmi.WMI()
            for item in c.Win32_BIOS():
                serial_number = item.SerialNumber
                break
        except ModuleNotFoundError:
            print("wmi module not found")
    else:
        print('This is a different operating system.')

    print(serial_number)
    return serial_number

