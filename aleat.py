#!/usr/bin/python

import random
import webapp

class aleatServ(webapp. webApp):

    def process(self, parsedRequest):
        randNum = (int(random.randrange(1,1001)) + int
        (random.randrange(1,1001))) * 1000000
        resp = "<html><body><h1>Hola</h1> <a href= http:" + str(randNum) + ">Dame otra</a> </body></html>" + "\r\n"
        return ("200 OK", resp)
               
if __name__ == "__main__":
    serv = aleatServ("localhost", 1234)
