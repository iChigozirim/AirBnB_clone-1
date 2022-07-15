# AirBnB clone
## Description
This repository contains the second version of the project to build a clone of the [AirBnB](https://www.airbnb.com/)  website.

In this version, the front-end is designed using HTML5/CSS3 and is served using Python Flask. The application is configured on a distributed system - two webservers and one load balancer - with Nginx and HAProxy. Also, it integrates file and database (MySQL) storage in a back-end API.

![AirBnB clone; version 2 data flow image](https://user-images.githubusercontent.com/88312276/179292409-6d32da52-d5a5-4e97-b840-e4618a186170.png)


---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
<br>

## Static
The front-end of this AirBnB clone was designed from scratch using HTML/CSS3 pages integrated using Flask. While the front-end has not yet been officially deployed, screenshots are viewable in the README of the [web_flask](https://github.com/iChigozirim/AirBnB_clone_v2/tree/master/web_flask) directory.

## Storage
All classes are handled by one of either two abstracted storage engines, depending on the call - [FileStorage](https://github.com/iChigozirim/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) or [DBStorage](https://github.com/iChigozirim/AirBnB_clone_v2/blob/master/models/engine/db_storage.py).

### FileStorage
The default mode.

In `FileStorage` mode, every time the backend is initialized, the program instantiates an instance of `FileStorage` called `storage`. The `storage` object is loaded/re-loaded from any class instances stored in the JSON file `file.json`. As class instances are created, updated, or deleted, the storage object is used to register corresponding changes in the `file.json`.

### DBStorage
Run by setting the environmental viriables `HBNB_TYPE_STORAGE=db`.

In `DBStorage` mode, every time the back-end is initialized, the program intantiates an instance of `DBStorage` called `storage`. The `storage` object is loaded/re-loaded from the MySQL database specified in the environmental variable `HBNB_MYSQL_DB`, using the user `HBNB_MYSQL_USER`, password `HBNB_MYSQL_PWD`, and host `HBNB_MYSQL_HOST`. As class instances are created, updated, or deleted, the `storage` object is used to register changes in the corresponding MySQL database. Connecion and querying is achieved using SQLAlchemy.

Note that the databases specified for `DBStorage` to connect to must already be defined on the MySQL server. This repository includes scripts [setup_mysql_dev.sql](https://github.com/iChigozirim/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql) and [setup_mysql_test.sql](https://github.com/iChigozirim/AirBnB_clone_v2/blob/master/setup_mysql_test.sql) to set up `hbnb_dev_db` and `hbnb_test_db` databases in a MySQL server, respectively.

## Console
The console is a command line interpreter that allows the manipulation of all classes utilized by the application by making calls on the `storage` object defined above.

## Using the console
The command interpreter can be started by running `./console.py` in your terminal.
```
$ ./console.py
(hbnb)
```
To quit the console, enter the command `quit`, or input an EOF signal (`ctr-D`)
```
$ ./console.py
(hbnb) quit
$
```
```
$ ./console.py
(hbnb) EOF
```
## The Console Commands
- ### create
  - Usage: `create <class>

Creates a new instance of a given class. The ID of the created instance is printed and instance is saved to `file.json`.
```
$ ./console.py
(hbnb) create BaseModel
ecbf544f-649b-477f-a88f-c69abf904948
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.ecbf544f-649b-477f-a88f-c69abf904948": {"id": "ecbf544f-649b-477f-a88f-c69abf904948", "created_at": "2022-06-09T19:55:16.143429", "updated_at": "2022-06-09T19:55:16.143437", "__class__": "BaseModel"}}
```
* ### show
  * Usage: `show <class> <id> or <class>.show(id)`

Prints the string repesentation of an instance based on the class name and id
 ```
$ ./console.py
(hbnb) create User
90665eb5-b6eb-4777-b1bb-2cf0e8233f6e
(hbnb) 
(hbnb) show User 90665eb5-b6eb-4777-b1bb-2cf0e8233f6e
[User] (90665eb5-b6eb-4777-b1bb-2cf0e8233f6e) {'id': '90665eb5-b6eb-4777-b1bb-2cf0e8233f6e', 'created_at': datetime.datetime(2022, 6, 9, 20, 4, 51, 116437), 'updated_at': datetime.datetime(2022, 6, 9, 20, 4, 51, 116442)}
(hbnb)
(hbnb) User.show(90665eb5-b6eb-4777-b1bb-2cf0e8233f6e)
[User] (90665eb5-b6eb-4777-b1bb-2cf0e8233f6e) {'id': '90665eb5-b6eb-4777-b1bb-2cf0e8233f6e', 'created_at': datetime.datetime(2022, 6, 9, 20, 4, 51, 116437), 'updated_at': datetime.datetime(2022, 6, 9, 20, 4, 51, 116442)}
(hbnb)
```
* ### destroy
  * Usage: `destroy <class> <id> or <class>.destroy(<id>)`

Deletes an instance based on the class name and id (saves the change into the JSON file)
 ```
$ ./console.py
(hbnb) create City
29977f37-38da-4461-a1f5-ceeadcb6aebc
(hbnb) create Place
f2d996d4-5e1f-416a-8c3a-bc2de9fd49b2
(hbnb) destroy City 29977f37-38da-4461-a1f5-ceeadcb6aebc
(hbnb) Place.destroy(f2d996d4-5e1f-416a-8c3a-bc2de9fd49b2)
```
* ### all
  * Usage: `all or all <class> or <class>.all()`

Prints all string representation of all instances based or not on the class name.
```
$ ./console.py
(hbnb) create BaseModel
5156be80-1c2d-490c-a00d-7dba39ffa652 
(hbnb) create BaseModel
4bd6266f-25de-41e6-8605-2639f8785719
(hbnb) create User
64b0693d-c571-4811-b328-b88e27141184
(hbnb) create User
854da6b1-2c09-4cbc-8352-c7249618021b
(hbnb)
(hbnb) all BaseModel
[BaseModel] (5156be80-1c2d-490c-a00d-7dba39ffa652) {'id': '5156be80-1c2d-490c-a00d-7dba39ffa652', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 32, 595393), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 32, 595409)}
[BaseModel] (4bd6266f-25de-41e6-8605-2639f8785719) {'id': '4bd6266f-25de-41e6-8605-2639f8785719', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 42, 417303), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 42, 417309)}
(hbnb)
(hbnb) User.all()
[User] (64b0693d-c571-4811-b328-b88e27141184) {'id': '64b0693d-c571-4811-b328-b88e27141184', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 49, 454662), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 49, 454668)}
[User] (854da6b1-2c09-4cbc-8352-c7249618021b) {'id': '854da6b1-2c09-4cbc-8352-c7249618021b', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 50, 769454), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 50, 769463)}
(hbnb)
(hbnb) all
[BaseModel] (5156be80-1c2d-490c-a00d-7dba39ffa652) {'id': '5156be80-1c2d-490c-a00d-7dba39ffa652', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 32, 595393), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 32, 595409)}
[BaseModel] (4bd6266f-25de-41e6-8605-2639f8785719) {'id': '4bd6266f-25de-41e6-8605-2639f8785719', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 42, 417303), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 42, 417309)}
[User] (64b0693d-c571-4811-b328-b88e27141184) {'id': '64b0693d-c571-4811-b328-b88e27141184', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 49, 454662), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 49, 454668)}
[User] (854da6b1-2c09-4cbc-8352-c7249618021b) {'id': '854da6b1-2c09-4cbc-8352-c7249618021b', 'created_at': datetime.datetime(2022, 6, 9, 20, 23, 50, 769454), 'updated_at': datetime.datetime(2022, 6, 9, 20, 23, 50, 769463)}
(hbnb)
```

* ### count
  * Usage: `count <class> or <class>.count()`

Retrieves the number of instances of a given class.
```
(hbnb) create BaseModel
952c8aed-061f-4851-8292-1d478f7c7aa0
(hbnb) create BaseModel
b6ae2de6-9bad-48ca-b7e3-bc573cfd62aa
(hbnb) create BaseModel
1f34c43e-31c6-4a15-89f1-9ff2735c51ac
(hbnb) create User
91b88604-74ce-40ea-b41c-006a95794524
(hbnb) create User
e36222ff-7717-44d8-a88c-011de3e411fd
(hbnb)
(hbnb) count BaseModel
3
(hbnb) User.count()
2
(hbnb) 
```
* ### update
  * Usage: `update <class> <id> <attribute name> "<attribute value>" or <class>.update(<id>, <attribute name>, <attribute value>) or <class>.update( <id>, <attribute dictionary>)`

Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs. If update is called with a single key/value attribute pair, only "simple" attributes can be updated (ie. not id, created_at, and updated_at). However, any attribute can be updated by providing a dictionary.
```
$ ./console.py
(hbnb) create User
6f74c68f-97d0-42a5-9c3b-cc06e665d6c4
(hbnb) 
(hbnb) update User 6f74c68f-97d0-42a5-9c3b-cc06e665d6c4 last_name "Betty"
(hbnb) show User 6f74c68f-97d0-42a5-9c3b-cc06e665d6c4
[User] (6f74c68f-97d0-42a5-9c3b-cc06e665d6c4) {'id': '6f74c68f-97d0-42a5-9c3b-cc06e665d6c4', 'created_at': datetime.datetime(2022, 6, 9, 20, 51, 38, 583962), 'updated_at': datetime.datetime(2022, 6, 9, 20, 51, 38, 583979), 'last_name': 'Betty'}
(hbnb) 
(hbnb) User.update(6f74c68f-97d0-42a5-9c3b-cc06e665d6c4, email, "betty@example.com")
(hbnb) show User 6f74c68f-97d0-42a5-9c3b-cc06e665d6c4
[User] (6f74c68f-97d0-42a5-9c3b-cc06e665d6c4) {'id': '6f74c68f-97d0-42a5-9c3b-cc06e665d6c4', 'created_at': datetime.datetime(2022, 6, 9, 20, 51, 38, 583962), 'updated_at': datetime.datetime(2022, 6, 9, 20, 51, 38, 583979), 'last_name': 'Betty', 'email': 'betty@example.com'}
(hbnb) 
(hbnb) User.update(6f74c68f-97d0-42a5-9c3b-cc06e665d6c4, {"address": "57 Ikenga BQ"})
(hbnb) show User 6f74c68f-97d0-42a5-9c3b-cc06e665d6c4
[User] (6f74c68f-97d0-42a5-9c3b-cc06e665d6c4) {'id': '6f74c68f-97d0-42a5-9c3b-cc06e665d6c4', 'created_at': datetime.datetime(2022, 6, 9, 20, 51, 38, 583962), 'updated_at': datetime.datetime(2022, 6, 9, 20, 51, 38, 583979), 'last_name': 'Betty', 'email': 'betty@example.com', 'address': '57 Ikenga BQ'}
(hbnb)
```

# Testing
Unittest for this progrem are defined in the [test](https://github.com/iChigozirim/AirBnB_clone/tree/master/tests) folder. To run the entire test suite simultaneously, execute the following command:
```
$ python3 unittest -m discover tests
```
Alternatively, you can specify a single test file to run at a time:
```
$ python3 -m unittest tests/test_models/test_engine/test_file_storage.py
```
