<h1>To Do App</h1>

Welcome to the repository of our To Do App, built using Python, Django, and Bootstrap.

This README provides detailed instructions on how to get this project up and running on your local machine for development and testing purposes.

<h1>Prerequisites</h1>

The following software needs to be installed in your system:

Python 3.9 or newer [(https://www.python.org/downloads/)](url)

Git [(https://git-scm.com/downloads)](url)



<h1>Steps to Setup</h1>

<h3>1. Clone the repository</h3>

First, you will need to clone the repository using Git. Open your terminal and run the following command:

```
git clone https://github.com/yourusername/todo-app.git
```

<h3>2. Create a virtual environment</h3>

If you are on MacOs always use <code>pip3</code> and <code>python3</code> to make sure that commands always work.

It is a good practice to create a virtual environment for your Python projects. This keeps dependencies required by different projects separate.


Navigate to the project directory:
```
cd todo-app
```

Create a virtual environment:
```
python3 -m venv env
```
Activate the virtual environment:

On macOS and Linux:
```
source env/bin/activate
```

On Windows:
```
.\env\Scripts\activate
```

<h3>3. Install dependencies</h3>

Next, install the project dependencies, which are listed in the requirements.txt file. In your terminal, run:
```
pip install -r requirements.txt
```

<h3>4. Apply the migrations</h3>

Django uses a database to store application data. So, before you can use the application, you need to create the database structure. This is done by running the following command:
```
python manage.py migrate
```
<h3>5. Run the server</h3>

Finally, you're ready to start the development server:
```
python manage.py runserver
```

This will start the server at [http://127.0.0.1:8000](url). Open this URL in your browser.



Thank you for downloading this project. Enjoy coding!
