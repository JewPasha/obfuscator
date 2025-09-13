# obfuscator

## USE ONLY ON VIRTUAL MACHINE

## Objective



The objective of this project is to explore the concept of polymorphic encryption. This technique, commonly used by malicious software, alters the program's signature each time it runs, making it more challenging for signature-based detection methods to recognize it. The goal is to develop a self-modifying program that changes its form while retaining its essential functionalities, specifically a basic SSH reverse shell.
## Polymorphic Encryption

Polymorphic encryption is a technique used to mask the true identity of a program. It involves altering the program's "signature" or external characteristics, often by modifying its code in ways that change its appearance without altering its actual functionality.
## Explanation of the Code

The program is written in Python and is meant to be used on Linux.

    Prints the signature (SHA-256) of the program.
    Connects to specified server, acts as SSH reverse shell.
    On exit self modifies in form (a new comment with random content is added at a different location, effectively modifying the code each time it executes).

## Usage

    Update the SERVER_IP and, if needed, SERVER_PORT variables with the IP and port of the server to which the reverse shell will connect.
    nc -lvp 4444 on host machine.
    Run the code in client machine (SHA-256 signature prints on each run).

## Result

### Host
if you put in terminal
``nc -lvp 4444 ``
![image](https://github.com/JewPasha/obfuscator/blob/main/images/host.png)

### Client
![image](https://github.com/JewPasha/obfuscator/blob/main/images/client.png)

