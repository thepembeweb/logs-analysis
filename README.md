# Logs Analysis

> "Logs Analysis" is an internal reporting tool running on Python and PostgreSQL that will use information from the database to discover what kind of articles the site's readers like.

![](https://upload.wikimedia.org/wikipedia/commons/f/f8/Python_logo_and_wordmark.svg) ![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/200px-Postgresql_elephant.svg.png)

![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)

The Logs Analysis report will answer the following questions:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top. 

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## Installation

### Requirements
The project uses VirtualBox, Vagrant, Python and PostgreSQL. 

* Install [Python 3](https://www.python.org/downloads/)
* Install [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* Install [Vagrant](https://www.vagrantup.com/downloads.html)

### Setup

* Clone the repo `git clone https://github.com/thepembeweb/logs-analysis.git`
* To setup the VM configuration unzip this file: FSND-Virtual-Machine.zip
* Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. 
* Change directory to the vagrant directory with `cd vagrant` 
* Start the virtual machine with `vagrant up`
* Log into the virtual machine with `vagrant ssh`
* Change directory with `cd /vagrant`
* Unzip this file: newsdata.zip to get the newsdata.sql datafile 
* Load the data with `psql -d news -f newsdata.sql`
* Move the files newsdb.py and report.py into the vagrant folder
* Run the reports with `python report.py`

## Output

Running reports ...


***************************** Report 1 *****************************


1. What are the most popular three articles of all time?

"Candidate is jerk, alleges rival" - 338647 Views.

"Bears love berries, alleges bear" - 253801 Views.

"Bad things gone, say good people" - 170098 Views.


***************************** Report 2 *****************************


2. Who are the most popular article authors of all time?

Ursula La Multa - 507594 Views.

Rudolf von Treppenwitz - 423457 Views.

Anonymous Contributor - 170098 Views.

Markoff Chaney - 84557 Views.


***************************** Report 3 *****************************


3. On which days did more than 1% of requests lead to errors?

Jul 17, 2016 - 2.3 % errors.


Reports completed!

## Built With

* [Python 3](https://www.python.org/) - The framework used
* [PostgreSQL](https://www.postgresql.org/) - The database used
* [VirtualBox](https://www.virtualbox.org/) - The virtualization software used
* [Vagrant](https://www.vagrantup.com) - The virtual machine environment manager used

## Authors

* **[Pemberai Sweto](https://github.com/thepembeweb)** - *Initial work* - [Logs Analysis](https://github.com/thepembeweb/logs-analysis)

## License

[![License](http://img.shields.io/:license-mit-green.svg?style=flat-square)](http://badges.mit-license.org)

- This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
- Copyright 2019 © [Pemberai Sweto](https://github.com/thepembeweb).

