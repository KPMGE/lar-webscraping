# LAR - Webscraping

### How to set the service up
In order to start all the services, you've got to run the following command: 

```bash
sudo docker-compose up
```

After a couple minutes, the nginx server is gonna be running at port 3333. Now, you must set up the 
nginx server to serve your json file through http.

Well done! Now your server is supposed to be setted up and running at port 3333. 


Finally, you can access the tht and reservations are gonna be available at: 

#### Tht route
> http://localhost:3333/tht.json

#### Reservations route
> http://localhost:3333/reservations.json
