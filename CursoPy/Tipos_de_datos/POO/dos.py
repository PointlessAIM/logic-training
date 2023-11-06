import uno

print("Top level in dos.py")

uno.function()

if __name__ == "__main__":
    print("dos.py is being run directly")
else:
    print("dos.py has been imported")