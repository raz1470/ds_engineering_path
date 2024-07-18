Contents
==
- [Contents](#contents)
- [What is a logging?](#what-is-a-logging)
- [Viewing logs](#viewing-logs)

<!--intro-start-->
# What is a logging?
Logging allows us to track events and errors when code runs. Logging useful data in the right places makes debugging errors easier. 

**Python provides a logging system as part of its standard library:**
- You can collect logs in the console (StreamHandler)
- Or you can collect logs in a file (FileHandler)
- Different messages can be logged: DEBUG, INFO, WARNING, ERROR and CRITICAL
- WARNING, ERROR and CRITICAL are logged by default
- Whereas DEBUG and INFO aren't logged by default

# Viewing logs
Navigate to the location of this markdown file in the terminal and run the following command:

`python3 logging_example.py`

You will be able to see both the StreamHandler and FileHandler logs in the terminal but you will only see the FileHandler logs in the log file which is created.

<!--intro-end-->
