# OpenSpace Organizer
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 🏢 Description

Your company moved to a new office at the Gent Zuiderport. Its an openspace with 6 tables of 4 seats. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues. 

This script runs everyday to re-assign everybody to a new seat.

![coworking_img](https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDd8fGRpdmVyc2UlMjB0ZWFtfGVufDB8fDB8fHwy)

## 📦 Repo structure

```
.
├── utils/
│   ├── openspace.py
│   ├── table.py
│   └── file_utils.py
├── .gitignore
├── main.py
├── new_colleagues.csv
├── output.xlsx
└── README.md
```

## 🛎️ Usage

1. Clone the repository to your local machine.

2 .To run the script, you can execute the `main.py` file from your command line:

    ```
    python main.py
    ```

3. The script reads your input file, and organizes your colleagues (up to 35) to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "output.xlsx" file in your root directory.

```python
input_filepath = "new_colleagues.csv"
output_filename = "output.xlsx"

# Creates a list that contains all the colleagues names
names = pd.read_csv(input_filepath, header=None)

# create an OpenSpace()
open_space = OpenSpace()

# assign a colleague randomly to a table
open_space.organize(names)

# save the seat assigments to a new file
open_space.store(output_filename)

# display assignments in the terminal
open_space.display()
```
4. If there aren't enough seats available, it will ask you to input 'S', 'T', 'N' or 'B':
    'T': add one table, 
    'S': add one seat for each table, 
    'B': add one table or add one seat to each table, 
    'N': do nothing

## ⏱️ Timeline

This project took two days for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](www.linkedin.com/in/zelimkhan-jachichanov-54b9231a7).