# LAR - Webscraping

### How to set the service up
In order to start all the services, you've got to run the following command: 

`sudo docker-compose up`

After a couple minutes, the server is gonna be running at port 3333. Now, you must set up the 
nginx server to work serve your json file through http.

First, install vim and bash inside nginx container: 

```bash
sudo docker-compose exec nginx apk add vim bash
```

Then, open up the nginx container: 

```bash
sudo docker-compose exec nginx bash
```

Now, all you have to do is opening the nginx configuration file using vim: 

```bash
vim etc/nginx/conf.d/default.conf
```

Then, put the following configuration into the file: 

```bash
server {
    listen       80;
    listen  [::]:80;
    server_name  localhost;

    location / {
        root   /usr/share/lar-data;
        index  tht.json;
    }

    # redirect server error pages to the static page /50x.html
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
```

Furthermore, make sure you haven't messed up anything in the configuration file by running the command: 
```bash
nginx -t
```

Finally, still inside the container, you can restart the nginx server, so that the changes are gonna be applied: 

```bash
nginx -s reload
```

Well done! Now you're server is supposed to be setted up and running at port 3333. Check it out by running:

> http://localhost:3333
