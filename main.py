from update_installations_table import update_installations_table
from monitor_installations import monitor_installations

# Need to schedule this function to run daily
def main():
    update_installations_table()
    monitor_installations()
    
if __name__ == '__main__':
    main()