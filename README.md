# 2A-SHORTURL
## The 2a short URL project was developed to help short URL users to use the short URL service more conveniently and quickly, while also solving the problem of high concurrent visits to the website. When the URL is shortened, users can quickly access the original URL through the shortened URL or through the QR code. Statistics and data behind the URL.


# Overall project structure 
## The directory structure of the entire project is implemented using the MTV model. Different development languages ​​have different models for website development. However, using Python as the language for website development, we developed based on the  MTV model.
To further clarify on the MTV model, please refer as below:
M - Model is the data access layer. This layer covers access to data, how data is validated, relationships between data to objects and also how data is stored.
T - Templates are basically when the user sees (commonly referred to as the presentation layer) in this case it will be how information is displayed on the static and dynamically created HTML pages.
V - View is the logic layer which is the core part of the system. All data from the users input will be processed in this layer. The logic layer acts as a bridge between the model and template layers.
For our project final directory, please check the appendix one for reference.

# Development environment
## The project itself is developed based on the Python tornado framework, but on this basis, our project is still dependent on a number of Python libraries. As there are many Python enthusiasts who contribute to the Python library community, this is the main reason why we chose Python as the development language.
## Please refer the details of the libraries that were used below:

**SQLAlchemy==1.3.13
tornado==6.0.3
urllib3==1.25.8
Werkzeug==1.0.0
WTForms==2.2.1
PyMySQL==0.9.3
matplotlib==3.2.0
pyecharts==1.7.1
redis==3.4.1**

# Starting of services for development
## 1. Install requirement dependent package environments
   Command:
   **Pip3 install -r requirements.txt**

## 2.a. Start Redis and Mysql services(Unix)
   Command:
   **1. sudo systemctl start redis**
   **2. sudo systemctl enable redis**
   **3. sudo systemctl start mysqld**

## 2.b. Start Redis and Mysql services(Windows)
   Command:
   **1. redis-server.exe redis.windows.conf** 
   **2. net start mysql** 

## 3. Start the server executable
   Command:
   **Python3 server.py**
   
# Features
## Business Use
<figure class="third">
    <img src="http://2a.nz/static/images/b2b.png?v=d49a1a0b2d72d39a03367bd1d786d63c">
    <img src="http://2a.nz/static/images/extension.gif?v=57fc53ea80aa83b8aedc7d8214756e0a">
    <img src="http://2a.nz/static/images/b2b2.png?v=029250a3ce60c0f3b1949847c4659896">
</figure>
  
  
 ## Social Media
 <figure class="third">
    <img src="http://2a.nz/static/images/sc1.png?v=9028e8b649d11e7bbdd4e2af26ba998f">
    <img src="http://2a.nz/static/images/sc2.png?v=edbd49d881bb01451026fb70fd6e94c7">
    <img src="http://2a.nz/static/images/meassger.gif?v=6c3845a487ac02946570b7c254762dd6">
</figure>
  
  


