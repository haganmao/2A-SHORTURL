# 2A-SHORTURL

![svg](https://github.com/haganmao/2A-SHORTURL/blob/master/static/images/2a.nz.svg)

<br>
<br>

The 2a short URL project was developed to help short URL users to use the short URL service more conveniently and quickly, while also solving the problem of high concurrent visits to the website. When the URL is shortened, users can quickly access the original URL through the shortened URL or through the QR code. Statistics and data behind the URL.
<br>
<br>

# Overall project structure 
The directory structure of the entire project is implemented using the MTV model. Different development languages ​​have different models for website development. However, using Python as the language for website development, we developed based on the  MTV model.
To further clarify on the MTV model, please refer as below:
<br>
<br>
* M - Model is the data access layer. This layer covers access to data, how data is validated, relationships between data to objects and also how data is stored.
* T - Templates are basically when the user sees (commonly referred to as the presentation layer) in this case it will be how information is displayed on the static and dynamically created HTML pages.
* V - View is the logic layer which is the core part of the system. All data from the users input will be processed in this layer. The logic layer acts as a bridge between the model and template layers.

<br>

# Development environment
The project itself is developed based on the Python tornado framework, but on this basis, our project is still dependent on a number of Python libraries. As there are many Python enthusiasts who contribute to the Python library community, this is the main reason why we chose Python as the development language. Please refer the details of the libraries that were used below:

* SQLAlchemy==1.3.13
* tornado==6.0.3
* urllib3==1.25.8
* Werkzeug==1.0.0
* WTForms==2.2.1
* PyMySQL==0.9.3
* matplotlib==3.2.0
* pyecharts==1.7.1
* redis==3.4.1**

## Starting of services for development
<br>

+ Install requirement dependent package environments
  1. pip3 install -r requirements.txt 
   
+ Start Redis and Mysql services(Unix)
 
  1. sudo systemctl start redis 
  2. sudo systemctl enable redis 
  3. sudo systemctl start mysqld 

+ Start Redis and Mysql services(Windows)

  1. redis-server.exe redis.windows.conf 
  2. net start mysql 

+ Start the server executable
  1. Python3 server.py 
<br>
<br>

# Features

+ Browser Extension
We have developed a browser extension that when clicked, copies the URL of the webpage you are currently on, then takes you to 2a.nz where you can paste in your long URL for even faster shortening.
<br>
<video src="https://github.com/haganmao/2A-SHORTURL/blob/master/static/images/4.%20Person2%20using%20short%20URL.mp4" controls="controls" width="500" height="300"></video>





