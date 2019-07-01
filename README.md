DEVELOPMENT STARTER PACK
-------------------------

## Prerequisites

Ensure that you have the following applications in your local / laptop to proceed with the exercise.
* Git
* Python 3.x
* Visual Studio Code (recommended text editor)
* Postman

#### Git Installation

##### Windows

Follow the instructions for [Git for Windows stand-alone installer](https://www.atlassian.com/git/tutorials/install-git#windows).

You may also opt to do **Install Git with Atlassian Sourcetree**.

##### Mac OSX

* Install [iTerm2](https://www.iterm2.com/)
* Open iTerm2 and follow instructions to install [brew](https://brew.sh/)
* Upon installing brew, run the following command:
```
$> brew install git
```

#### Python 3.x Installation

Read and follow the instructions [here](https://realpython.com/installing-python/).

#### Visual Studio Code

You may opt to download other text editor / development IDE. This one is just a suggestion since majority of the team is using this.

#### Postman

Postman is an HTTP client for conducting HTTP requests. This tool is very useful for testing HTTP requests that you will develop. For one, it stores all your HTTP requests. For a brief discussion on HTTP and REST APIs, you may read this [article](https://enterprise-confluence.asurion.com/display/TS/Understanding+HTTP).

Download Postman [here](https://www.getpostman.com/downloads/).


## Installation Setup

* Download, or in `git` jargon, **clone** this repo via the command:
```
$> git clone ssh://git@enterprise-bitbucket.asurion.com:7999/pmnldo/development-starter-pack.git
```
NOTE: **Cloning via SSH is not default.** You may opt to clone via HTTPs for the meantime but moving forward, setup your SSH keys in your Bitbucket account to use SSH protocol.

* Open your preferred text editor and open the directory previously downloaded/cloned.

* Also open a command prompt/terminal (iTerm2 for Mac). Navigate to the location of the downloaded directory, or in `git` jargon, **repository**. From there, install the Python requirements via the command:
```
$> pip install -r requirements.txt
```

* Run the app via the command:
```
$> FLASK_APP=app.py python -m flask run
```


## Familiarizing with REST APIs

#### REST APIs vs HTTP Requests

REST APIs are not equivalent to HTTP requests. REST APIs pertain more to the **design** or **structure** or **organization** of the resources that is being accessed via HTTP requests. It is a standard/practice that many conform today to better organize their resources/HTTP endpoints.

To illustrate how REST APIs can be analogous to a function...

A function...
```
def multiple(x, y):
  ...implem here
```

REST API...
```
GET /v1/multiple?x=A&y=B
```

In Python, you name your function accordingly on what it performs. Say it performs a multiplication, one would think the function name would relate to "multiplication" hence `multiply()`. Same goes with REST APIs. If we want to translate multiply to a web service, we are **GET**ting the product and does the endpoint is designed to respond to an HTTP GET that will yield the product. To reiterate, REST API is a standard/practice for structuring/organizing your HTTP endpoints.


#### Hands-On Illustration

To illustrate this practice further, run the script and open Postman.

Define the following in your Postman and click send per resource to check the output:

##### GET /v1/users
* Method: **GET** 
* URL: http://localhost:3000/v1/users

##### POST /v1/users
* Method: **GET** 
* URL: http://localhost:3000/v1/users
* Headers: application/json
* Body (raw):
```
{
  "data": {
    "name": "Some Name",
    "age": 20
  }
}
```

NOTE: Try running **GET** again after **POST**.
##### GET /v1/users/1
* Method: **GET** 
* URL: http://localhost:3000/v1/users/1

Try playing around **GET**'s and **POST**'s or the whole source code itself to see how every part works.

## Exercises

Before starting any of the exercises below, execute the following commands first:
```
$> git checkout -b <provide any name here that will identify your `branch` in the repository>
```

This will ensure that all changes you do won't affect the **master** branch of the repository.

If an error is encountered, probably because you made changes prior to this, just execute `git checkout -f`. But do take note that doing this will remove all your changes prior. To save your changes, just ask me or search for `git stash`.

#### Add DELETE and PUT method.

As you may notice, a RESTful webservice conforms to CRUD functionality popular with databases.
```
(C)reate          = POST
(R)ead/(R)etrieve = GET
(U)pdate          = PUT
(D)elete          = DELETE
```

Try implementing **PUT** and **DELETE** functionality which will perform editing of user details and removing user details respectively.

NOTE: You may opt to add proper error handling for unexpected cases like performing **DELETE** but id is not provided. However the main goal only covers the implementation of ideal cases. :)

#### New Route

Implement a new route, anything that you can think of (say `/books`, `/dogs`, etc), that will have the **CRUD** functionalities. Copy-pasting (from users) is not illegal :P but ensure that you understand each stuff that you copy-paste. :) Play around your code and try to elaborate its functionality more (adding more error handling, adding more logic, etc).


## References

* [Git](https://www.atlassian.com/git/tutorials)
** Git Commands [Cheat Sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)
* [Flask](http://flask.pocoo.org/docs/1.0/)
