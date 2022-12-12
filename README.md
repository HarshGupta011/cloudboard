# cloudboard

#### Summary:

Our idea is to make a cloud based clipboard to which the user can seamlessly copy objects (text, images and files) on one device and then paste the same objects on any of their other devices. We plan to work on the following components in our project:

    A client application that logs a user in and allow them to send copy and paste requests [API interfaces]

    A server that serves an API that listens for any copy and paste requests from the clients [Virtual Machines, API interfaces]

    A storage system for storing and indexing copied objects for retrieval later [Storage services, Databases, Key-Value Stores]

    User authentication so that users cannot access each other’s clipboards

    Data encryption on the copied objects for privacy

Some stretch goals that we may work on are: 

    Ways to lock objects so that users cannot accidentally delete items that are being currently accessed

    A website for users to create new accounts and fetch access tokens from

    A way for users to clear their clipboard and/or view their copy history

We will initially work on getting the service working on Linux machines and will support the copying of text, and will later expand it to other types of data and other operating systems.

#### Team members:
Aditya Srivastava, Aishwarya Jayaramu, Harsh Gupta

## Notes

1. start sending data to the cloud only when the use has selected paste (otherwise you'd be sending data to the cloud all the time for no reason). Most copies are still going to be pasted locally.
2. Use https://github.com/mhammond/pywin32 for clipboard functionality on Windows. Use xclip or xsel on Linux and other X11 based Unix systems.
3. First build baseline working model with pyperclip.