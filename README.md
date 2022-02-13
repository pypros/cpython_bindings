Before run and building cpython module.

```bash
$ ls -al
total 18
drwxr-xr-x 1 user 197609    0 Feb 13 11:39 .
drwxr-xr-x 1 user 197609    0 Feb 12 22:11 ..
-rw-r--r-- 1 user 197609  370 Feb 13 11:38 docker-compose.yml    
-rw-r--r-- 1 user 197609  344 Feb 13 10:22 Dockerfile
-rw-r--r-- 1 user 197609    0 Feb 13 11:38 README.md
-rw-r--r-- 1 user 197609  822 Feb 13 09:36 setup.py
-rw-r--r-- 1 user 197609 2281 Feb 13 09:36 spammodule.c
```

Run and build

```bash
$ docker-compose up 
WARNING: The http_proxy variable is not set. Defaulting to a blank string.
WARNING: The https_proxy variable is not set. Defaulting to a blank string.
WARNING: Found orphan containers (cpython_bindings_c) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up.
Recreating cpython_bindings ... done
Attaching to cpython_bindings
cpython_bindings   | running build_ext
cpython_bindings   | building 'spam' extension
cpython_bindings   | copying build/lib.linux-x86_64-3.8/spam.so ->

cpython_bindings exited with code 0
```

Check is spam.so in folder
```bash
$ ls -al
total 62
drwxr-xr-x 1 user 197609     0 Feb 13 11:38 .
drwxr-xr-x 1 user 197609     0 Feb 12 22:11 ..
drwxr-xr-x 1 user 197609     0 Feb 13 11:38 build
-rw-r--r-- 1 user 197609   370 Feb 13 11:38 docker-compose.yml   
-rw-r--r-- 1 user 197609   344 Feb 13 10:22 Dockerfile
-rw-r--r-- 1 user 197609     0 Feb 13 11:38 README.md
-rw-r--r-- 1 user 197609   822 Feb 13 09:36 setup.py
-rw-r--r-- 1 user 197609 41816 Feb 13 11:38 spam.so
-rw-r--r-- 1 user 197609  2281 Feb 13 09:36 spammodule.c
```

Next run python and try to play with a new Python module written in C
```bash
$ python3
Python 3.8.10 (default, Nov 26 2021, 20:14:08)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import spam
>>> spam.system("ls -al")
total 56
drwxrwxrwx 1 user user  4096 Feb 13 11:58 .
drwxrwxrwx 1 user user  4096 Feb 12 22:11 ..
-rwxrwxrwx 1 user user   344 Feb 13 10:22 Dockerfile
-rwxrwxrwx 1 user user  1703 Feb 13 11:42 README.md
drwxr-xr-x 1 root  root   4096 Feb 13 11:58 build
-rwxrwxrwx 1 user user   372 Feb 13 11:59 docker-compose.yml
-rwxrwxrwx 1 user user   822 Feb 13 09:36 setup.py
-rwxr-xr-x 1 root  root  41816 Feb 13 11:58 spam.so
-rwxrwxrwx 1 user user  2281 Feb 13 09:36 spammodule.c
0
>>>
