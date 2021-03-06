# Installing and Running the front end
## Installation

### Installing Node
* The first step in installing node is going to https://nodejs.org/en/download/current/ and finding the correct installer for your system. We are using the Current version with the latest features.  
    * Mac & Windows
        * Download the installer and follow the prompts.  
        * Open up your terminal window on your machine and run ```node -v``` to ensure that it is installed.
        * Doing this should also have installed NPM which can be checked with the ```npm -v``` command.  
    * Linux
        * Will add at a later date. 

### Installing Angular
* Installing Angular is very simple once you have NPM installed. 
    * Run the command ``` npm install -g @angular/cli ```
    * Once this is done to check that angular was installed run ```ng v```
    * Here is the link to Angular's setup page incase something goes wrong.  https://angular.io/guide/setup-local

* Other installations.
    * Run ```npm install bootstrap```
## Running the Angular Application
* To run the the angular application you will need to clone or download our repository from https://github.com/Asetka/Stocko 
* Once you have it downloaded to your machine open your terminal and navigate to the directory.  
* Once in the the directory all you have to do is run ```ng serve```
    * If it does not run on the first try use ```npm update``` 
* After this if everything workes you should be able to open up your ```localhost:4200``` in your browser,  which is the default listening port for Angular, and you should see the interface.  


# Installing and running the backend

* Will add at a later date. 
* Backend dependencies - 'pip install -r requirements.txt' in the root directory (Stocko)
* Can be installed using
* Dependencies:
* Werkzeug==2.0.1
* requests==2.25.1
* yfinance==0.1.63
* Flask==2.0.1
* Flask_Cors==3.0.10
* pymongo[srv]==3.12.0
* gunicorn==20.1.0

# Page Descriptions
* Stock Page - Provides the usercompany information, data, and price chart for stocks
* Postions Page - Allows user to add, edit, and delete postions from their investment portfolio
* Evaluations Page - Allows the user to search a stock and evaluate the stock based on a number of predetermined pillars to gauge the intrinsic value of the stock vs its current trading price
* Forecast Page - Allows the user to view previous performance metrics of a stock and enter assumptions to forecast a future stock price prediction
* NLP Page - Sprint 3 Feature
* Back Testing - Sprint 3 Feature
