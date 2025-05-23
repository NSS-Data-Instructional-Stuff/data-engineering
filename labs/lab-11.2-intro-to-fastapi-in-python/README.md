## Lab 11.2

### Introduction

In this lab you will be creating a local api using fast api in python to test a callback from Stripe. 

### Part 1
Create a stripe account. www.stripe.com 

### Part 2
Create an API using fast api as you have done in previous lessons. You have have two endpoints. 
GET /   should return 'I am root'   -- This is just an easy proof of life endpoint
POST /callback should return a 204 and no content in the message. 

Use Postman to test the API. 

### Part 3
Configure a dev tunnel. https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/get-started?tabs=macos

Do not start the devtunnel server only start the host. Make sure it is started to listen on the same port that your api is on. 

### Part 4
Create a call back in stripe and simulate the webhook.  You can find out how to do this in the stripe documentation. Print the call back to the terminal to verify that you are recieving it locally. 

