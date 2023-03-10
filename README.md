**0x00. AirBnB clone - The console**
This project is an implementation to manage AirBnB project

**First step: Write a command interpreter to manage your AirBnB objects.**
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

	1. put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
	2. create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
	3. create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
	4. create the first abstracted storage engine of the project: File storage.
	5. create all unittests to validate all our classes and storage engine

**What’s a command interpreter?**
A command interpreter allows the user interact with the program using commands
in the form of text lines. e.g. the shell
This project is exactly like the shell but limited to a specific use-case.
In our case, we want to be able to manage the objects of our project:
	1. Create a new object (ex: a new User or a new Place)
	2. Retrieve an object from a file, a database etc…
	3. Do operations on objects (count, compute stats, etc…)
	4. Update attributes of an object
	5. Destroy an object

**Execution**
Your shell should work like this in interactive mode:
	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb)
	(hbnb)
	(hbnb) quit
	$

But also in non-interactive mode: (like the Shell project in C)
	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$

**How to use the command interpreter**
To give a command, the name of the command is simply typed followed by the
object to act on if any.
1. To create an object:
	(hbnb) create User
2. To update an instance
	(hbnb) update User
3. To show an instance
	(hbnb) show User
4. To view available help
	(hbnb) help
5. To quit the interpreter
	(hbnb) quit
