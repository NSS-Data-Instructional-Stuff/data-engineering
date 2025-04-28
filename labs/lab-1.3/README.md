## Lab 1.3

### Introduction
The purpose of this lab is to learn how to authenticate to a REST api. You will authenticate using Postman as your api client. 

### Part 1 
In this first step you need to get a token. You will configure your Postman client with a POST to `/api/auth` and the body as raw json.    

```
{
    "username": "admin",
    "password": "password123"
}
```

If done correctly you should see a response that is similar to: 

```
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzQ0NjYwOTQzfQ.MtvSz9cUeXMX-HmHgE92XnUjWXGYKgjIsm0Q2jYzFbM",
    "expires_at": "2025-04-14T20:02:23.789588Z"
}
```

You will need to paste the token that you get into an online decoder. https://jwt.io/ is a good resource. This will let you see what is being passed in the token. 

### Part 2
Next, set up Postman for authentication. Go to your collection and choose the authorization tab. Set **Auth Type** as **Bearer Token**, then paste the token that you received above in for token. 

Then you will need to create a GET to `/people`.  
If you have done this correctly you will see results similar to: 
```
{"offset": 0, "limit": 10, "total_items": 50, "data": [{"first_name": "Tammy", "last_name": "Alexander", "email": "davissherri@example.net", "address": "53000 Wong Orchard\nHernandezburgh, VT 15497"}, {"first_name": "Warren", "last_name": "Anderson", "email": "denise09@example.com", "address": "6653 Smith Island Suite 189\nPort Jefferyshire, OR 48919"}, {"first_name": "Claudia", "last_name": "Andrews", "email": "bjackson@example.net", "address": "8796 Hudson Green\nWest David, UT 87420"}, {"first_name": "Kelly", "last_name": "Barnes", "email": "austinmills@example.com", "address": "4785 John Pines\nSouth Marialand, PW 93367"}, {"first_name": "George", "last_name": "Barnett", "email": "littlekatherine@example.org", "address": "PSC 0665, Box 3648\nAPO AP 40416"}, {"first_name": "Robert", "last_name": "Bates", "email": "thompsoneric@example.org", "address": "96575 Alvarez Tunnel Suite 927\nPhillipsville, WI 24830"}, {"first_name": "Vicki", "last_name": "Black", "email": "ekerr@example.com", "address": "358 Denise Valleys Apt. 959\nEast Timothy, TX 89075"}, {"first_name": "Robert", "last_name": "Boyle", "email": "dbanks@example.net", "address": "3516 Diaz Hill Suite 644\nSouth Ashley, ID 67141"}, {"first_name": "William", "last_name": "Brady", "email": "fergusoncarrie@example.com", "address": "4189 Madison Glens Suite 206\nLake Vickiborough, TN 20792"}, {"first_name": "Aaron", "last_name": "Castillo", "email": "roy72@example.com", "address": "9595 Gary Port\nLarafort, TN 04209"}]}
```
