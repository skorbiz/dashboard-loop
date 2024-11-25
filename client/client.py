import os
import subprocess

def register_and_run_as_service():
    # Copy the resources to the correct location
    shutil.copytree("resources", "/")

    # Set the correct permissions
    subprocess("chmod 644 /resources/etc/systemd/system/dashboard-client.service", check=True)

    # Register the service
    subprocess("systemctl enable dashboard-client.service", check=True)

    # Start the service
    subprocess("systemctl start dashboard-client.service", check=True)

    # Check the status of the service
    subprocess("systemctl status dashboard-client.service", check=True)

    # Check the logs of the service
    subprocess("journalctl -u dashboard-client.service", check=True)

def take_screenshot():
    from datetime import datetime
    from PIL import ImageGrab
    from PIL import Image
    from PIL import ImageDraw
    
    # Get the current time    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    # Get a screenshot
    screenshot = ImageGrab.grab()
 
    # Write the current time on the screenshot
    draw = ImageDraw.Draw(img) 
    draw.text((28, 36), current_time, fill=(255, 0, 0))
 
    # Display edited image
    # img.show()
 
    # Save and close
    screenshot.save("output/temp.png")
    screenshot.close()



if __name__ == '__main__':
    register_and_run_as_service()
    take_screenshot()









# Check if the process is already running starting

# Start the screenshot process

# Start the dashboard

# Check the checksum of files and update if nessesary

# 