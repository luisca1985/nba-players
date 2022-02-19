# Project

The application downloads the raw data from https://mach-eight.uc.r.appspot.com and print a list of all pairs of players whose height in inches adds up to the integer USER_INPUT to the application. 
```bash
python main.py USER_INPUT
```
If no matches are found, the application prints "No matches found".

Sample output is as follows:
```bash
python3 main.py 139
```
```bash
- Nate Robinson          Brevin Knight
- Nate Robinson          Mike Wilks
```

The algorithm to find the pairs is `O(n log n)` and is divided in:
- A sorted list of players, whose complexity is `O(n log n)`
- A binary search, whose complexity is `O(log n)`. Since binary search is inside a for loop, the worst case is `O(n log n)`.


`O(n log n)` complexity is faster than `O(n^2)`.

## Installation
### Clone the Project
````bash
git clone https://github.com/luisca1985/nba-players.git
````
````
cd nba-players
````

### Virtual Environment
````
python3 -m venv venv
````
````
source venv/bin/activate

````
### Modules Installation
````
pip3 install -r requirements.txt
````
### Run the App
````
python3 main.py USER_INPUT
````
