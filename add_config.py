import shutil

def add_config_lines(file_path, new_settings):
    try:
        
        with open(file_path, 'a') as file:
            for setting in new_settings:
                file.write(setting + '\n')
        print(f"Settings successfully added to {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "/boot/firmware/config.txt"
new_settings = [
    "dtparam=i2c_arm=on",
    "dtparam=spi=on",
    "dtoverlay=tpm-slb9670",
    "dtoverlay=i2c0,pins_44_45",
    "dtoverlay=i2c-rtc,pcf85363,i2c0",
    "dtparam=ant2"
]

add_config_lines(file_path, new_settings)
