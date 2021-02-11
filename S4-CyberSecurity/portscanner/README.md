## Working Port Scanner!

## Info
- Python3 Script
- Make sure you have installed all the imports!
- To use this code open the Command Prompt (or terminal on Linux and macOS) and run portscanner.py with the arguments, see examples for extra details.
- A file will be created with the name of the target host (.txt file) in this file will be a small summary.

## How to use?
### Windows
- py portscanner.py **{target} {minport} {maxport} {debug}**
    - **Target:** IP or domainname of the system to check
    - **Minport:** Start port to check (Must be between 1 and 65535)
    - **Maxport:** Last port to check (Must be between 1 and 65535)
    - **Debug:** Enable or Disable Debug mode, this will output some extra data in the Command Prompt or Terminal (Must be y or n)
- run portscanner.py -h for extra info!

### MacOS / Linux
- python3 portscanner.py **{target} {minport} {maxport} {debug}**
    - **Target:** IP or domainname of the system to check
    - **Minport:** Start port to check (Must be between 1 and 65535)
    - **Maxport:** Last port to check (Must be between 1 and 65535)
    - **Debug:** Enable or Disable Debug mode, this will output some extra data in the Command Prompt or Terminal (Must be y or n)
- run portscanner.py -h for extra info!
