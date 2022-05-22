# Cookie-Clicker-Bot
plays cookie clicker, a clicking based web game

Hi! Using Selenium, this bot plays the version of Cookie Clicker found at http://orteil.dashnet.org/experiments/cookie/ . 

The bot opens the webpage to start a game, clicks relentlessly on the cookie for 5 minutes, while periodically trading cookies for upgrades. No user input is required to play once the program is started. At the end of the 5 minutes, the game closes and number of cookies produced and highest cookie/second stats are revealed in the console. 

A bit of optimizing was done to get the highest cookie/second output, namely increasing the length of time between upgrades. The bot speed seems to be heavily affected by CPU load, or at least on my old computer it was. Max cookie/second output was 100.5 at 5 minutes.

This project is day 48 of udemy.com's 100 Days of Code: The Complete Python Pro Bootcamp for 2022
