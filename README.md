# Finance App
This is an app made by Pratyush Bindal & Sonya Lee for [St Christophers School of Bahrain](https://st-chris.net) to help aid the students in their learning of how to work with money and good financial practicies.

## Development side
### Frameworks
Backend written in django using integrated database and fronted written in HTML & CSS via Bootstrap
### Running the application
Create python environment:

    python -m venv env
Enter environment:

Windows:

    env\scripts\activate

Linux / MacOS:

    source env/bin/activate

Download requirements:

    pip install -r requirements.txt

Enter project directory (Same for MacOS / Linux & Windows):

    cd Learning Finace

Run app:

MacOS / Linux:

    python3 manage.py runserver 0.0.0.0:8000

Windows:

    python manage.py runserver 0.0.0.0:8000

Then, go to [This Link](http://localhost:8000/FinanceApp/) to view your app locally on your machines

## Key for different redirect codes (Custom)
### Login/Signup Codes
    Code 1 - Login/Signup went perfectly
    Code 2 - User is not logged in, redirecting to login page
    Code 3 - Login details were entered incorrectly, redirecting back to login page