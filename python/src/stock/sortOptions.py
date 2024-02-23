import warnings
from datetime import date, datetime,timedelta
from yahoo_fin import options
from yahoo_fin.stock_info import get_live_price
#import yfinance as yf
import pandas as pd
#import numpy as np
import configparser
import os
import requests
import logging
import time

warnings.filterwarnings('ignore')

global asklimit, bidlimit, askbidratio, lowestbid

symbolList = []
#symbolList = ["ASML","BUD"]
dataValue = {}

def read_file_contents(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8-sig') as file:
            contents = file.read()
            file.close
            return contents
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        logging.info("File %s not found!", file_name)
        return None
    except Exception as e:
        print(f"Error: {e}")
        logging.info("Error: %s", e)
        return None

def get_calls_and_puts(symbol: str, date: str) -> tuple:
    try:
        calls = options.get_calls(symbol, date)
        puts = options.get_puts(symbol, date)

        # Replace '-' with 0
        calls = calls.replace("-", 0)
        puts = puts.replace("-", 0)
        
        # Extract the desired columns     
        new_calls = calls[["Contract Name", "Strike", "Last Price", "Bid", "Ask", "Volume"]]
        new_puts = puts[["Contract Name", "Strike", "Last Price", "Bid", "Ask", "Volume"]]
    except:
        new_calls = None
        new_puts = None

    return new_calls, new_puts

def filter_rows_by_price(df, given_price):
    # Get the 5 rows with strike price lower than the given price
    lower_rows = df[df["Strike"] < given_price].tail(5)
    # Get the 5 rows with strike price higher than the given price
    higher_rows = df[df["Strike"] > given_price].head(5)
    # Combine the two DataFrames
    result = pd.concat([lower_rows, higher_rows])
    # Reset the index and regenerate row number in the first column
    result = result.reset_index(drop=True)
    #result.index += 1
    return result

def validate(df):
    bid, ask = 0.0, 0.0    
   
    if (not df.empty):
        index = df.index[0]
        try:
            bid = float(df.at[index, "Bid"])
            ask = float(df.at[index, "Ask"])
        except:
            pass
    return bid, ask
    
def calculateCall(df, given_price):
    global asklimit, bidlimit, askbidratio, lowestbid   
    c = 0.0
    # Get the the last row with strike price higher than the given price
    higher_rows = df[df["Strike"] >= given_price].head(1)
    bid, ask = validate(higher_rows)
    if (bid < lowestbid):
        return 0.0
    if (bid> bidlimit and ask > asklimit) and ((ask-bid)/bid>askbidratio): 
        return 0.0
    cp = (bid + ask) / 2.0
    c = cp/given_price

    return c

def calculatePut(df, given_price):
    global asklimit, bidlimit, askbidratio, lowestbid
    p = 0.0  
    
    # Get the last row with strike price lower than the given price
    lower_rows = df[df["Strike"] <= given_price].tail(1)
    bid, ask = validate(lower_rows)
    if (bid < lowestbid):
        return 0.0
    if (bid> bidlimit and ask > asklimit) and ((ask-bid)/bid>askbidratio): 
        return 0.0
    pp = (bid + ask) / 2.0
    p = pp/given_price
   
    return p

def send_sms(phone_number, message):
    url = "https://textbelt.com/text"
    payload = {
        "phone": phone_number,
        "message": message,
        "key": "698c67cf236deb82c5d696e5b05142dc10f696e6flTuF0pX2j8LcR0bH4FVGOiuM", 
    }
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("SMS sent successfully to "+ phone_number)
            #logging.info("SMS sent successfully to %s", phone_number)
            return 0
        else:
            print(f"Failed to send SMS. Error: {response.text}")
            logging.info("Failed to send SMS. Error: %s", response.text)
            return 1
    except requests.RequestException as e:
        print(f"Error sending SMS: {e}")
        logging.info("Error sending SMS: %s", e)
        return 2

def sendNotification(sorted_dataValue, countrycode, phonenumbers):        
    # Concatenate name and value for each row into a single line separated by a comma
    count = 1
    output_line = ""
    for item in sorted_dataValue:
        output_line = output_line+item[0]+str(item[1])+","
        count = count + 1
        if (count >= 12):
            break
    #print(output_line)
    #print(len(output_line))
    logging.info(" ======== Notification =============")
    logging.info("%s",output_line)    
    logging.info("%d",len(output_line))
        
    #Send SMS notification messages
   
        # Split the string to obtain individual phone numbers
    numbers_list = [number.strip() for number in phonenumbers.split(',')] 
    
    for number in numbers_list:
        returncode = send_sms("+"+countrycode+number, output_line)
        if (returncode == 0):
            logging.info("SMS sent successfully to %s", number)
        else:
            logging.info("SMS sent failed to %s", number)
        time.sleep(2)
            
        
def main():   
    global asklimit, bidlimit, askbidratio,lowestbid
    
    # Get the absolute path to the script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Combine with the filename to get the full path
    config_file_path = os.path.join(script_directory, 'sortoptions.ini')

    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the INI file
    config.read(config_file_path)

    # Access values from the 'logging' section
    path = config.get('sortoptions','path')
    listfile = config.get('sortoptions', 'listfile')
    blacklist_file = path+listfile 
    asklimit = float(config.get('filters', 'asklimit'))
    bidlimit = float(config.get('filters', 'bidlimit'))
    askbidratio = float(config.get('filters', 'askbidratio'))
    lowestbid = float(config.get('filters', 'lowestbid'))
    logfile = config.get('logging', 'file')
    loglevel = config.get('logging', 'level')
    Switch = int(config.get('notification', 'switch'))
    notificationSwitch = bool(Switch)
    countrycode = config.get('notification','countrycode')
    phonenumbers = config.get('notification','phonenumbers')

    
    #path = "d:/chatpm/python/data/"
    today = date.today()
    print(f"Today's date is {today.strftime('%m-%d-%Y')}")
    next_friday = today + timedelta((4 - today.weekday()) % 7)
    next_friday_string = next_friday.strftime("%m/%d/%Y")
    #print("Next Friday is "+next_friday_string)

    now = datetime.now()
    currentDatetime = now.strftime("%Y%m%d-%H%M")
    print(f"Current date time is " + currentDatetime)
    
    fileName = path+"Options_sorted_"+currentDatetime+".txt"
    logfile = path+"log_"+currentDatetime+".log"
    # Configure logging
    #logging.basicConfig(filename=logfile, level=loglevel, 
    #                    format='%(asctime)s - %(levelname)s - %(message)s')
    logging.basicConfig(filename=logfile, level=loglevel, format='%(message)s')


    # If it's Friday and after 4PM (16:00), then jump to next Friday
    if now.weekday() == 4 and now.time() > datetime.time(datetime(1, 1, 1, 16, 0)):
        next_friday += timedelta(7)
        next_friday_string = next_friday.strftime("%m/%d/%Y")
        print("It's after 4 PM on Friday, so jumping to the following Friday: " + next_friday_string)
    #contractDate = "02/02/2024"
    contractDate = next_friday_string
    print("Contract date:"+contractDate)
    
    if blacklist_file:
        # Read the contents of the specified file
        #listFileName = path+file_to_read
        with open(blacklist_file, "r", encoding='utf-8-sig') as f:
            for line in f:
                symbolList.append(line.strip())
        f.close
    print(f"Symbol list: {symbolList}")

    for symbol in symbolList:
        print("\n================================================================\n")
        print("\nSymbol:"+symbol)
        
        try:    
            current_price = get_live_price(symbol)
            print(f"Current price for {symbol} is ${current_price:.2f}")
        
            # Get calls and puts for given stock at contract date
            calls, puts = get_calls_and_puts(symbol, contractDate)
            if( calls is None or puts is None):
                print("Nothing returns for it.")
                logging.info("============== Nothing returns for %s ==================",symbol)
                continue            
        
            filtered_calls = filter_rows_by_price(calls, current_price)
            filtered_puts = filter_rows_by_price(puts, current_price)

            #log same info
            logging.info("%s============== Filtered CALLS for $%.2f==================",symbol, current_price)
            logstr = filtered_calls.to_string()
            logging.info(logstr)
            logging.info("%s============== Filtered PUTS for $%.2f===================",symbol, current_price)
            logstr = filtered_puts.to_string()
            logging.info(logstr)
                        
            c = calculateCall(filtered_calls, current_price)
            p = calculatePut(filtered_puts, current_price)            
            r = (c+p)/2.0/current_price * 100000.0
            dataValue[symbol] = round(r,1)
            
        except ValueError:
            #code that handle the exception
            print("No tables found!")
            logging.info("***No table found for %s", symbol)
            dataValue[symbol] = -1.0    
    # end of symbol list loop

    """ print("\n=================== Data value pair =======================")   
    print(dataValue)   """  

    sorted_dataValue = sorted(dataValue.items(), key=lambda x:x[1], reverse=True )

    print("\n=================== Sorted Result =======================")  
    print("{:<10} {:<10}".format('Symbol', 'Value'))
    print("-" * 12)
    for item in sorted_dataValue:
        print("{:<10} {:.1f}".format(item[0], item[1]))
        #print("{:<10} {:.1f}".format(item[0], round(float(item[1]), 1)))

    # Write data into log file
    logging.info("=================== Sorted Result =======================")
    with open(fileName, 'w') as f:
        f.write("{:<6} {:<6}\n".format('Symbol', 'Value'))
        f.write("-" * 20 + "\n")

        for item in sorted_dataValue:
            #log_f.write("{:<6} {:.1f}\n".format(item[0], round(float(item[1]), 1)))
            f.write("{:<6} {:.1f}\n".format(item[0], item[1]))
            
            # Log each line written to the file
            logging.info(" %s %.1f", item[0], item[1])
    f.close()
    
    if(notificationSwitch):
         sendNotification(sorted_dataValue, countrycode, phonenumbers)    
        
if __name__ == "__main__":
    # Explicitly call the main() function
    main()