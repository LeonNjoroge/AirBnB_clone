AirBnB_clone
The aim of this project is to deploy a simplified version of the AirBnB website onto your server.

AirBnB is a platform that operates as an online marketplace facilitating travel information and booking services. It offers various lodging options, home-stays, and tourism services through its websites and mobile applications, serving clients globally.

Introduction
What is a command interpreter?

A command interpreter, akin to the Shell, is a program that allows users to interact with the system by receiving and executing commands. In this project, our command interpreter enables users to manage project objects effectively:

Creating new objects (e.g., a new User or a new Place)
Retrieving objects from files, databases, etc.
Performing operations on objects (e.g., counting, computing stats, etc.)
Updating attributes of objects
Deleting objects
Execution
The shell should function in both interactive and non-interactive modes:

Interactive mode:

In interactive mode, users can directly input commands and receive immediate feedback.

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```


Non-interactive mode:

In non-interactive mode, commands are provided through input redirection or piping from files or other sources.

```
$ echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):
========================================

EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

  
Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$

```

Usage Examples

**Launching the console**
```
$ ./console.py
(hbnb) 
```
**Creating a new object**
```
(hbnb) create
** class name missing **
(hbnb) create User
670265eb-5982-489e-8b92-2dff054f0776
```
**Show an object**
```
(hbnb) show User
** instance id missing **
(hbnb) show User 670265eb-5982-489e-8b92-2dff054f0776
[User] (670265eb-5982-489e-8b92-2dff054f0776) {'created_at': datetime.datetime(2020, 2, 19, 18, 8, 58, 458246), 'id': '670265eb-5982-489e-8b92-2dff054f0776', 'updated_at': datetime.datetime(2020, 2, 19, 18, 8, 58, 458261)}
```

Test for Initial Commit