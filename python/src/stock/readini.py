import configparser
import os

# Get the absolute path to the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Combine with the filename to get the full path
config_file_path = os.path.join(script_directory, 'example.ini')

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the INI file
config.read(config_file_path)

# Read the INI file
# config.read('example.ini')

print(config.sections())
# Access values from the sections
value1 = config.get('Section1', 'key1')
value2 = config.get('Section1', 'key2')
value3 = config.get('Section2', 'key3')
value4 = config.get('Section2', 'key4')

# Print the values
print(f"value1: {value1}")
print(f"value2: {value2}")
print(f"value3: {value3}")
print(f"value4: {value4}")
