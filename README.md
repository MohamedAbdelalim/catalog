#How do to run the program?

1. Downlaod and Install.
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads), VirtualBox6.0.10
* [Vagrant](https://www.vagrantup.com/downloads.html), Vagrant 2.2.5
* [Sqlite](https://www.sqlite.org/download.html), sqlite
* [Python](https://www.python.org/downloads/), python2.
2. Preparing  the application
* Open the terminal in the database folder and run these commands $ git clone https://github.com/AboSalaah/fullstack-nanodegree-vm.git
* then vagrant up (it takes some time to run)
* then vagrant ssh (to log into the machine) then cd /vagrant/catalog(to access the shared folder)  
3. Run the program
* Run on the terminal these commands python database_setup.py, python database_content.py then python application.py then open localhost:8000 on your browser.
4. For API  endpoints
* write in you browser https://localhost:8000/catalog/<category_name>/json and replace category_name whith your chossen category, https://localhost:8000/catalog/<category_name>/<item_name>/json and replace category_name whith your chossen category and item_name with your chossen item.
