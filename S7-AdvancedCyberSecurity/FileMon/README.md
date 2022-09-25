# FileMon

A filemonitor written in python with Watchdog.<br>
To use this program, please follow the following steps:
- Download the content of this (the `FileMon`) folder;
- Create a virtual environment[^1];
    - On Windows: `py -m venv .venv`
    - On Linux: `python3 -m venv .venv`
- Install the requirements with the command: `pip install -r requirements.txt`;
- Change the configuration to contain the **folders** that you want monitored;
    - Open the `__main__.py;
    - Search for the line which contains the lines below;
        ```
        paths = [
            "path/to/file",
        ]
        ```
    - Replace `path/to/file` with the desired directory;
- Run the script using the command: `py __main__.py`;


[^1]: It is possible that the environment needs te be enabled, to do this, run the activate script in the `.venv/scripts/` folder!