Install Redis on Windows
Use Redis on Windows for development

Redis is not officially supported on Windows. However, you can install Redis on Windows for development by following the instructions below.

To install Redis on Windows, you'll first need to enable WSL2 (Windows Subsystem for Linux). WSL2 lets you run Linux binaries natively on Windows. For this method to work, you'll need to be running Windows 10 version 2004 and higher or Windows 11.

Install or enable WSL2
Microsoft provides detailed instructions for installing WSL. Follow these instructions, and take note of the default Linux distribution it installs. This guide assumes Ubuntu.

Install Redis
Once you're running Ubuntu on Windows, you can follow the steps detailed at Install on Ubuntu/Debian to install recent stable versions of Redis from the official packages.redis.io APT repository. Add the repository to the apt index, update it, and then install:

>>> curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

>>> echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

>>> sudo apt-get update
>>> sudo apt-get install redis
Lastly, start the Redis server like so:

>>> sudo service redis-server start
Connect to Redis
Once Redis is running, you can test it by running redis-cli:

>>> redis-cli
Test the connection with the ping command:

127.0.0.1:6379> ping
PONG
You can also test that your Redis server is running using Redis Insight.