import os
import schedule
import time
import threading

 
directory_to_clear = ""
clear_interval = 0
running = True  

def clear_cache():
    """Function to clear the cache in the specified directory."""
    try:
        for filename in os.listdir(directory_to_clear):
            file_path = os.path.join(directory_to_clear, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # حذف فایل
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)  # حذف دایرکتوری
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
                
        print(f"Cache cleared successfully from {directory_to_clear}.")
    except Exception as e:
        print(f"Error occurred while clearing cache: {e}")

def setup_schedule():
    global directory_to_clear, clear_interval
    
    directory_to_clear = input("addrs file cache: ")
    
    if not os.path.isdir(directory_to_clear):
        print(f"The directory {directory_to_clear} does not exist. Creating the directory.")
        os.makedirs(directory_to_clear)

    try:
        clear_interval = int(input("time be sanie ast "))
        if clear_interval <= 0:
            raise ValueError("Interval must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a positive integer for seconds.")
        exit(1)
        
     
    schedule.every(clear_interval).seconds.do(clear_cache)

def background_task():
    """Runs the scheduler in the background."""
    while running:
        schedule.run_pending()
        time.sleep(1)

def command_listener():
    """Listens for user commands to stop or shutdown the script."""
    global running
    while True:
        command = input("Enter 'stop' to pause the cache clearing or 'shutdown' to exit: ")
        if command.lower() == "stop":
            running = False
            print("Cache clearing has been paused. Type 'shutdown' to exit completely.")
        elif command.lower() == "shutdown":
            running = False
            print("Shutting down...")
            break
        else:
            print("Invalid command. Please type 'stop' or 'shutdown'.")

if __name__ == "__main__":
    setup_schedule()
    print(f"Scheduled cache clearing every {clear_interval} second(s) for {directory_to_clear}.")
    
     
    scheduler_thread = threading.Thread(target=background_task, daemon=True)
    scheduler_thread.start()

     
    command_listener()
    
    print("Script terminated successfully.")
