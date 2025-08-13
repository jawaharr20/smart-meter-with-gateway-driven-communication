import serial
import time
import smbus2
import re

# Define some device parameters for I2C LCD
I2C_ADDR = 0x27  # I2C device address, check with i2cdetect
LCD_WIDTH = 16   # Maximum characters per line

LCD_CHR = 1  # Mode - Sending data
LCD_CMD = 0  # Mode - Sending command

LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line

LCD_BACKLIGHT = 0x08  # On
ENABLE = 0b00000100   # Enable bit
E_PULSE = 0.0005
E_DELAY = 0.0005

# I2C bus (1) initialization
bus = smbus2.SMBus(0)

def lcd_init():
    """ Initialize the LCD """
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)
    time.sleep(E_DELAY)

def lcd_byte(bits, mode):
    """ Send byte to data pins """
    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)

    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    """ Toggle enable pin """
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(E_DELAY)

def lcd_string(message, line):
    """ Send string to display """
    message = message.ljust(LCD_WIDTH, " ")  # Pad message to 16 characters
    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

# Initialize LCD
lcd_init()

# Serial Port Configuration for UART3 on A5D2X
SERIAL_PORT_3 = "/dev/ttyS3"
BAUD_RATE = 115200

def extract_voltage_current(data):
    """ Extracts voltage and current from the received string using regex """
    voltage = re.search(r"Voltage: (\d+\.\d+)V", data)
    current = re.search(r"Current: (\d+\.\d+)A", data)
    
    if voltage and current:
        return voltage.group(1), current.group(1)
    return None, None

def read_uart3():
    """ Reads UART3 data (on A5D2X) and prints voltage and current on LCD """
    ser = serial.Serial(SERIAL_PORT_3, BAUD_RATE, timeout=5)
    ser.reset_input_buffer()

    print("UART3 Receiver Started. Waiting for data...")

    while True:
        raw_data = ser.read(ser.in_waiting or 1)  # Read available data or 1 byte if none
        if raw_data:
            try:
                # Decode the received data
                decoded_data = raw_data.decode('utf-8', errors='replace')
                print("Received Data:", decoded_data)

                # Extract voltage and current using regex
                voltage, current = extract_voltage_current(decoded_data)
                
                if voltage and current:
                    # Display the extracted voltage and current on the I2C LCD
                    lcd_string("Voltage: {}V".format(voltage), LCD_LINE_1)  # Display voltage on lin1
                    lcd_string("Current: {}A".format(current), LCD_LINE_2)  # Display current on lin2

            except Exception as e:
                print("Error decoding data:", str(e))

        time.sleep(1)

try:
    read_uart3()
except KeyboardInterrupt:
    print("Program interrupted by user.")

root@rugged-board-a5d2x-sd1:~/project/success# cat success1.py 
import serial
import time
import smbus2
import re

# Define some device parameters for I2C LCD
I2C_ADDR = 0x27  # I2C device address, check with i2cdetect
LCD_WIDTH = 16   # Maximum characters per line

LCD_CHR = 1  # Mode - Sending data
LCD_CMD = 0  # Mode - Sending command

LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line

LCD_BACKLIGHT = 0x08  # On
ENABLE = 0b00000100   # Enable bit
E_PULSE = 0.0005
E_DELAY = 0.0005

# I2C bus (1) initialization
bus = smbus2.SMBus(0)

def lcd_init():
    """ Initialize the LCD """
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)
    time.sleep(E_DELAY)

def lcd_byte(bits, mode):
    """ Send byte to data pins """
    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)

    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    """ Toggle enable pin """
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(E_DELAY)

def lcd_string(message, line):
    """ Send string to display """
    message = message.ljust(LCD_WIDTH, " ")  # Pad message to 16 characters
    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

# Initialize LCD
lcd_init()

# Serial Port Configuration for UART3 on A5D2X
SERIAL_PORT_3 = "/dev/ttyS3"
BAUD_RATE = 115200

def extract_voltage_current(data):
    """ Extracts voltage and current from the received string using regex """
    voltage = re.search(r"Voltage: (\d+\.\d+)V", data)
    current = re.search(r"Current: (\d+\.\d+)A", data)
    
    if voltage and current:
        return voltage.group(1), current.group(1)
    return None, None

def read_uart3():
    """ Reads UART3 data (on A5D2X) and prints voltage and current on LCD """
    ser = serial.Serial(SERIAL_PORT_3, BAUD_RATE, timeout=5)
    ser.reset_input_buffer()

    print("UART3 Receiver Started. Waiting for data...")

    while True:
        raw_data = ser.read(ser.in_waiting or 1)  # Read available data or 1 byte if none
        if raw_data:
            try:
                # Decode the received data
                decoded_data = raw_data.decode('utf-8', errors='replace')
                print("Received Data:", decoded_data)

                # Extract voltage and current using regex
                voltage, current = extract_voltage_current(decoded_data)
                
                if voltage and current:
                    # Display the extracted voltage and current on the I2C LCD
                    lcd_string("Voltage: {}V".format(voltage), LCD_LINE_1)  # Display voltage on lin1
                    lcd_string("Current: {}A".format(current), LCD_LINE_2)  # Display current on lin2

            except Exception as e:
                print("Error decoding data:", str(e))

        time.sleep(1)

try:
    read_uart3()
except KeyboardInterrupt:
    print("Program interrupted by user.")
