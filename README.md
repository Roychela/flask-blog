## TITLE
FlaskBlog

## AUTHOR
Roy Chela

## DESCRIPTION
A blog application that allows users to share their opinions on various topics.

## DATE
04/07/2019

## BEHAVIOUR DRIVEN DEVELOPMENT(BDD)

| Behaviour | Input                     | Output                    |
| --------- | ------------------------- | ------------------------- |
| Signing in     | Email ,username ,password | User Signed in            |
| Logging in    | Email adress,password     | User Logged in            |
| Write comment    | submit comment for particular blog post   | comment for the particulsr blog post is displayed |
| Update blog  | Click on update button       | Edited blog |
| Delete  | Click on delete button        | Selected blog is deleted |


## SETUP
### Requirements
* Ubuntu
* Flask framework
* Heroku hosting site
### Installation
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `chmod a+x start.py`
* On your terminal run `./start.py`
* Access the live site using the local host provided

### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)
#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/JamesMutahi/flask-blog.git
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='<Secret_key>'
DEBUG=True
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py makemigrations && python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:5000](http://127.0.0.1:5000/)


## LIVE SITE
https://flaskblog2030.herokuapp.com/
## KNOWN BUGS
None

## TECHNOLOGIES
* Python3.6
* Flask framework

## LICENSE
[MIT](https://github.com/Roychela/flask-blog/blob/master/LICENSE)
