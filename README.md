# Python Shopping System
![Static Badge](https://img.shields.io/badge/python-3.12-blue)

A simple shopping system built with Python
## Tabel of content
- [Features](#features)
- [Project structure](#project-structure)
- [Requirment](#requirment)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Usage](#usage)
- [Example Output](#example-output)
- [screenshot](#screenshot)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)


## Features


- Product System
  - Displays a list of available products
  - Shows the price of each product
  - Allows the user to choose a product
  - Asks for the quantity
  - Calculates the total price

- Sales Storage
  - Saves sales information in `sales.txt`
  - Stores the customer name, product, quantity, and total price

- Admin Mode
  - Asks if the user wants to open admin mode
  - Asks for the admin password
  - Checks if the password is correct
  - Keeps the password outside the main Python file
  - Loads the password from `.env`

- Product Management
  - Keeps product names and prices in a separate `products.py` file

## Project structure

```text
mini_shop2/
│   main.py
│   products.py
|   requirments.txt
│   .env.example
│   .gitignore
│   README.md
│  
│
├───gifs
│       quiz.gif
│
├───pictures
│       num1.png
│       num2.png
├───    num3.png

```

### File Description

| file | Description |
| --- | --- |
| `main.py` | main file used to run the shopping system |
| `products.py` | stores product names and prices|
| `requirments.txt` | list the python packages needed for the project |
| `.env` | stores the admin password securely|
| `.gitignore` | tells Git which files and folders should not be tracked|
| `sales.txt` | stores the sales information|
 `README.md` | contains the project documentation |
| `pictures/` | stors project scrinshots |
| `pictures/num1.png` | scrinshots start shopping |
| `pictures/num2.png` | scrinshots quiz shopping |
| `pictures/num3.png` | scrinshots final shopping |
| `gifs/` | stors demo gif file |
| `gifs/quiz.gif` | shows the project|

## Requirment
Before running the project, make sure you have:
- `python 3`
- `python-dotenv`
- 


## Installation
1. open a terminal in the project folder.
2. check that python is installed:
```bash
python --version
```
3. install the python packages:
```bash
pip instal -r requirments.txt
``` 
## Environment Setup
1. creat a `.env` file from `.env.example`
```bash
cp .env.example .env
```
2. open the new `.env` file
3. replace the example value with your own password 
```txt
QUIZ_ADMIN_PASSWORD=your_password_here
```
4. save the file
> do not commit your `.env` file because it may contain privat information

## Usage
1. open a terminal in the project folder
2. run the quiz game
```bash
python main.py
```
3. choose `yes` or `no` for admin mode
4. if you choose `yes` , enter the password from your `.env` file 
5. enter your name 
6. answer the questions 
7. see your final score and message 
8. your result is saved in `sales.txt`
## Example Output
```txt
do u want to open admin mode? yes/no: no

what is your name ?alex
hi alex

Product List
milk : 30 $
apple : 20 $
bread : 10 $

Enter the product name:bread

How many do you want? 4

total Price: 40
```
## screenshot

### start shopping
![start game ](pictures\num1.png)

### quiz
![quiz](pictures\num2.png)

### final 
![final ](pictures\num1.png)

## Demo
![QUIZ SHOP DEMO ](gifs\quiz.gif)
## Roadmap
- [x] add multiple quiz questions
- [x] calculate the final score
- [x] save results to a file
- [ ] add admine mode 
- [ ] add more quiz questions

## Contributing

## License

## Author
create by [reyhaneh bashiri](https://github.com/yildizbashiri)
