# HOW TO DEPLOY A DJANGO APP IN HOSTINGER VPS

### How to Point Domain and Host Django Project on Apache Web Server VPS Hosting
- Login to Your Domain Provider Website
- Navigate to Manage DNS
- Add Following Records:

| Type | Host/Name | Value |
| :---: | :---: | :--- |
| A     | Your Subdomain Name | Your Remote Server IP |
| AAAA  | Your Subdomain Name | Your Remote Server IPv6 |

- On Local Windows Machine, Goto Your Project Folder then follow below instruction:
- Open Terminal
- Activate Your virtual Env
- Create requirements.txt File, by either using this:
```sh
pip freeze > requirements.txt
```
- or by this:
```
$ pipreqs /home/project/location
```

> *Note: Pipreqs is generally recommended, but if you don't have it installed in the sysmte, do so by using:*```pip install pipreqs```
- Deactivate Virtual Env
- On Local Windows Machine Make Your Project Folder a Zip File using any of the software e.g. winzip
- Open Command Prompt
- Copy Zip File from Local Windows Machine to Linux Remote Server
```sh
Syntax:- scp -P Port_number Source_File_Path Destination_Path
Example:- scp -P 22 dynamic.zip root@62.72.29.52:
```
- Copied Successfully

- Get Access to Remote Server via SSH
```sh
Syntax:- ssh -p PORT USERNAME@HOSTIP
Example:- ssh -p 22 root@62.72.29.52
```
> Note:- Run Below Commands on Your Remote Server Linux Machine or VPS, Not on Your Local Windows Machine

- Verify that all required softwares are installed
```sh
  apache2 -v
  python --version
  apache2ctl -M
  pip --version
```
- If Required Softwares and Modules are not Installed then Install them:
```sh
sudo apt install apache2
sudo apt install python
sudo apt install libapache2-mod-wsgi-py3
sudo apt install python3-pip
```
- Install virtualenv
```sh
pip list
sudo pip install virtualenv
```
- Verify Apache2 is Active and Running
```sh
sudo service apache2 status
```
- Verify Web Server Ports are Open and Allowed through Firewall
```sh
sudo ufw status verbose
```
- Run ls command to verify that the zip file is present
```sh
ls
```
- Unzip the Copied Zip File
```sh
Syntax:- unzip zip_file_name
Example:- unzip dynamic.zip
```
- Move Project Folder from User Home to Web Server Public Directory
```sh
Syntax:- sudo mv project_folder_name Destination_Path
Example:- sudo mv dynamic /var/www
```
- Go to Your Project Directory
```sh
Syntax:- cd /var/www/project_folder_name
Example:- cd /var/www/dynamic
```

---

#### Creating a virtual environment
- Install virtualenv
```sh
pip install virtualenv
```

- Go where you want to put your virtual env and then run the command below to create one
```sh
virtual env NAME
```

- A new directory is created with the name you gave, that's your virtualenv folder
- Activate virtualenv using the below command
```sh
source NAME/bin/activate
```

- If you want to deactivate, run the below command
```sh
deactivate
```
---

- Go to your project folder and install Dependencies
```sh
pip install -r requirements.txt
```
- Create Virtual Host File
```sh
sudo nano /etc/apache2/sites-available/your_domain_name.conf
```
- Add Following Code in Virtual Host File
```sh
<VirtualHost *:80>
    ServerName www.example.com
    ServerAdmin contact@example.com
    DocumentRoot /var/www/project_folder_name
    
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
    
    Alias /static /var/www/project_folder_name/static
    <Directory /var/www/project_folder_name/static>
        Require all granted
    </Directory>
    
    Alias /media /var/www/project_folder_name/media
    <Directory /var/www/project_folder_name/media>
        Require all granted
    </Directory>
    
    <Directory /var/www/project_folder_name/Inner_project_folder_name>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
    
    WSGIDaemonProcess any_name python-home=/var/www/project_folder_name/myprojectenv python-path=/var/www/project_folder_name
    WSGIProcessGroup any_name
    WSGIScriptAlias /  /var/www/project_folder_name/inner_project_folder_name/wsgi.py
</VirtualHost>
```
- Check Configuration is correct or not
```sh
sudo apache2ctl configtest
```
- Enable Virtual Host
```sh
cd /etc/apache2/sites-available/
sudo a2ensite your_domain.conf
```
- Restart Apache2
```sh
sudo service apache2 restart
```
- Open Django Project settings.py
```sh
cd /var/www/dynamic/dynamic
sudo nano settings.py
```
- Make below changes
```sh
ALLOWED_HOST = ["your_domain"]
DEBUG = False
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```
- Restart Apache2
```sh
sudo service apache2 restart
```

---

## If Django loads but with errors ofcourse

- Serve Static Files
```sh
cd /var/www/dynamic
python manage.py collectstatic
```
- Create Database Tables
```sh
python manage.py makemigrations
python manage.py migrate
```
- Create Superuser
```sh
python manage.py createsuperuser
```
- If Database File throws error Permission Denied then Set below permissions
- Make Webserver as owner for database file. Our Webserver is running as www-data and group is also www-data.
```sh
Syntax:- 
sudo chown -R www-data:www-data database_folder
sudo chmod 775 database_folder
sudo chmod 664 database_folder/database_file

Example:-
sudo chown -R www-data:www-data mbdb
sudo chmod 775 mbdb
sudo chmod 664 mbdb/db.sqlite3
```
- If Media Files (User Uploaded Files) throws error Permission Denied then Set below permissions
```sh
sudo chown -R www-data:www-data media
```
- You may face problem if you work with FTP so to fix this add your user to webserver user group following below instruction:
- Check Your User Group
```sh
sudo groups raj
```
- Add your User to webserver group
```sh
sudo usermod -a -G www-data raj
```
- Verify Your User is in Webserver Group
```sh
sudo groups raj
```
- If needed Deactivate Virtual env
```sh
deactivate
```

---

## Debugging 101

- You can check error logs If you get any error:
```sh
cd /var/log/apache2/
cat error.log
```
- Or
```sh
cat /var/log/apache2/error.log
```

- You can Clear Error Logs (Optional)
```sh
sudo bash -c 'echo > /var/log/apache2/error.log'
```

> If get Error mod_wsgi (pid=1234): Failed to proxy response from daemon then follow below instructions:
- Open apache2.conf
```sh
cd /etc/apache2
sudo nano apache2.conf
```
- Write below code in the bottom of apache2.conf file
```sh
WSGIApplicationGroup %{GLOBAL}
```
- To Know more about %{GLOBAL} follow this link: https://modwsgi.readthedocs.io/en/develop/configuration-directives/WSGIApplicationGroup.html

- Restart Apache2

```sh
sudo service apache2 restart
```

---

#### Fixing INTERNAL SERVER ERROR | WSGI errors

> If you see error.log containing WSGI errors, that probably mean you need to make migrations and static files.

- Go to your projectfile
```sh
cd /var/www/ProjectFileName
```
- Install mysqlclient (if you use mysql database)
- Create the database mentioned in your `ProjectFileName/InnerProjectFile/settings.py` 
- Run the below command
```sh
python manage.py collectstatic
```
- Make migrations
```sh
python manage.py makemigrations

python manage.py migrate
```
---

#### `Fixing DisallowedHost at` Error

- Go to settings.py inside your inner project file
```sh
cd /var/www/ProjectName/InnerProjectName/settings.py
```
- Inside the `ALLOWED_HOSTS = []` add your url
```
ALLOWED_HOSTS = ['successjobs.successscholar.in']
```

## SSL Certificate Installation

- Install SSL Certificate using `certbot`
```sh
sudo apt install certbot

certbot
```

> If you face error "Name duplicates previous WSGI daemon definition" while installing SSL Certificate for your domain then comment below code then try to install SSL Certificate again and after successful installation un-comment it 
```sh
cd /etc/apache2/sites-available/your_domain.conf

#WSGIDaemonProcess any_name python-home=/var/www/project_folder_name/myprojectenv python-path=/var/www/project_folder_name
#WSGIProcessGroup any_name
#WSGIScriptAlias /  /var/www/project_folder_name/inner_project_folder_name/wsgi.py
```
- A ssl config file will generate. Remember both ssl and non-ssl files can not have same WSGIDaemonProcess and WSGIProcessGroup name (mentioned above as any_name) so you may have to change the name manually in both the files.