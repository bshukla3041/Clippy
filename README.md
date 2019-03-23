# Clippy
A URL shortening service developed using django framework, integrataed with Bootstrap4. It generates a shortened url of the form ```HOST_URL_CONF/shortcode``` where shortcode is 6 character length code unique for each url.

## Getting Started

### Installing
* Create a virtual environment with python3 and pip3 (recommended)
* Change to project root directory (with manage.py file)
  ```
    cd src
  ```
* Install required python dependencies 
  ```
    pip3 install -r requirements.txt
  ```
* Run the local server from project root directory
  ```
    python3 manage.py runserver
  ```
* Access the website in your browser at ```http://localhost:8000```