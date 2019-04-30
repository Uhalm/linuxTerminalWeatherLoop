#import time and os
import os;
import time;


location = 'holder';
zip = 'holder';
userIn = 'holder';

#define main menu
def main():
    global userIn;
    os.system('clear');
    print('1. Weather loop');
    print('2. Graphical');
    print('3. Text');
    print('4. Radar')
    print('5. Setup (Run this on first use)');
    userIn = input('Type the number you want to do : ');
    if userIn == '1':
        wlSetup();
    if userIn == '2':
        graphSetup();
    if userIn == '3':
        textSetup();
    if userIn == '4':
        radar();
    if userIn == '5':
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
    os.system('clear');
    radar();
    weatherLoop();


#define Graphical
def graphical():
    global zip;
    os.system('clear');
    os.system('curl wttr.in/' + zip);
    radar();
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


def radar():
    os.system('columns=324');
    global userIn
    imgRad = 'INSERT_URL_HERE'#Replace INSERT_URL_HERE with the URL for the map you want it to display recomendation is wunderground
    downDir = './temp/radar/'
    os.system('rm /*.gif');
    os.system('rm /*.png');
    os.system('rm /*,jpg');
    os.system('wget ' + imgRad + ' -O ' + 'map.gif');
    os.system('convert map.gif map.jpg'); #says that there is something wrong with this fix this line
    os.system('clear');
    os.system('jp2a --width=324 --colors -f map.jpg');
    time.sleep(5);
    os.system('columns=162');
    if userIn == '4':
        radar();
    else:
        time.sleep(10);


#define setup
def setup():
    print('Starting Install of Dependencies...');
    os.system('sudo apt-get install weather-util');
    os.system('sudo apt-get install ansiweather');
    os.system('sudo apt-get install wget');
    os.system('sudo apt-get install jp2a');
    os.system('sudo apt-get install imagemagick');
    os.system('mkdir ./temp/')
    os.system('mkdir ./temp/radar');
    print('done');
    time.sleep(3);
    main();


main();
