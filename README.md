# STK Power Analysis (v5)

A python script to analyze STK simulations.

# Installation & How to Use

<!-- Creating a virtual environment is optional, but you might want to use one to make sure you're using the right packages for the script. If you're not, skip to step 3. -->

<!-- 1. Create a virtual environment (venv):
     ```
     python3 -m venv venv
     ```

2. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ``` -->

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Place the csv files from the STK simulation inside the `csv` folder. For now, you will have to separate each panel into its own csv file. It should look something like this:
   ```
   ├── main.py
   ├── requirements.txt
   └── csv/
       ├── Port.csv
       ├── Starboard.csv
       ├── Zenith.csv
       └── ...
   ```

3. Run the `main.py` script:
   ```
   python3 main.py
   ```

4. The generated plots and report will be output in a folder with the current date and time in UTC, like so:
   ```
    └── YYYYmmDD-HHMMSS/
        ├── plot1.csv
        ├── plot2.csv
        ├── plot3.csv
        └── report.txt
   ```


