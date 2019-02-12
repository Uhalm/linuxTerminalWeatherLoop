#import time and os
import os;
import time;


location = 'holder';
zip = 'holder';


#define main menu
def main():
    os.system('clear');
    print('1. Weather loop');
    print('2. Graphical');
    print('3. Text');
    print('4. Setup (Run this on first use)');
    userIn = input('Type the number you want to do : ');
    if userIn == '1':
        wlSetup();
    if userIn == '2':
        graphSetup();
    if userIn == '3':
        textSetup();
    if userIn == '4':
        setup();
    else:
        error();
#define Weather Loop setup
def wlSetup():
    global zip
    global location
    zip = input('What is your zip code? : ');
    location = input('what city are you in? : ');
    weatherLoop();

#defie Graphical setup
def graphSetup():
    global zip;
    zip = input('What is your zip code? : ');
    graphical();

def textSetup():
    global zip;
    global location;
    location = input('What city are you in');
    zip = input('What is your zip code? : ');
    text();
#define Weather Loop
def weatherLoop():
    global location
    global zip
    os.system('clear');
    os.system('curl wttr.in/' + zip);
    time.sleep(40);
    os.system('clear');
    os.system('weather -f ' + zip);
    time.sleep(60);
    os.system('clear');
    os.system('weather -a ' + zip);
    time.sleep(40);
    os.system('clear');
    os.system('ansiweather -l ' +  location + ' -u impirial');
    os.system('ansiweather -l ' + location + ' -u impirial -f4');
    time.sleep(30);
    os.system('clear')
    weatherLoop();


#define Graphical
def graphical():
    global zip;
    os.system('clear');
    os.system('curl wttr.in/' + zip);
    time.sleep(10);
    graphical();


#define text
def text():
    global zip;
    global location;
    os.system('clear');
    os.system('weather -f',  zip);
    time.sleep(40);
    os.system('clear');
    os.system('weather -a', zip);
    time.sleep(10);
    os.system('clear');
    os.system('ansiweather -l ' + location + ' -u impirial');
    os.system('ansiweather -l ' + location + ' -u impirial -f4');
    time.sleep(20);
    text();

#define setup
def setup():
    print('Starting Install of Dependencies...');
    os.system('sudo apt-get install weather-util');
    os.system('sudo apt-get install ansiweather');
    print('done');
    time.sleep(3);
    main();


main();
