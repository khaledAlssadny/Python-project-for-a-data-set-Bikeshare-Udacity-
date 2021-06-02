import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
"""
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
"""              




def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    Cities = ['chicago', 'new york city', 'washington']

    Months = ['january', 'february', 'march', 'april', 'may', 'june','all']

    Days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ,'all']
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city do you want to explore ? \n Choose from these choises (Chicago, New york city or Washington? \n> ').lower()
        # lower() it a function to convert the user input to lower case 
        if city in Cities:
            break
        else:
            print("This is invalid input. Please enter a valid input")
          
              

   # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("if you want the details for a certain month \n Choose from these choises \n ('january', 'february', 'march', 'april', 'may', 'june'), type all to display all months : ").lower()
        # lower() it a function to convert the user input to lower case 
        if month in Months:
            break
        else:
            print("invalid input. Please enter a full valid month input")
                        
   # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("if you want the details for a certain month \n Choose from these choises \n ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'), type all to display all months : ").lower()
        # lower() it a function to convert the user input to lower case 
        if day in Days:
             break  
        else:
            print("invalid input. Please enter a full valid day input")
            
            
    print('-'*40)
    return city, month, day 
  
    
def load_data(city, month, day):
    Months = ['january', 'february', 'march', 'april', 'may', 'june']
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name() # In version 1 of pandas , weekday_name was replaced with day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = Months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
       # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()] # we add .title() function to convert the first letter to the capital letter to match the day is writen in the sentance

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
   
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

     # display the most common month
    print("The most common month is ", df['month'].mode()[0], "\n")# we use mode() to get the most repeated value in the data

     # display the most common day of week
    print("The most common day of week  is ", df['day_of_week'].mode()[0], "\n")

     # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    # we use mode() function to get the most repeated value in data
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is ", df['Start Station'].mode()[0], "\n")

    # display most commonly used end station
    print("The most commonly used end station is ", df['End Station'].mode()[0], "\n")

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    

    # TO DO: display total travel time
    # Here we divided by 3600 to convert the time from seconds to hours
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel,"seconds ,or" , total_travel/3600 ,"hours")

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel ,"seconds ,or" ,mean_travel/3600 ,"hours")
    
    # display max travel time
    max_travel = df['Trip Duration'].max()
    print("Max travel time :", max_travel ,"seconds ,or" ,max_travel/3600 ,"hours")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    Counts_of_users = df['User Type'].value_counts()
    print('\nCounts_of_users:\n',Counts_of_users)
    # we use try python exception here with try to avoid the invalid value from the user 
    try:
        # Display counts of gender
        Counts_of_genders = df['Gender'].value_counts()
        print('\nCounts_of_genders: \n', Counts_of_genders)

        # Display earliest, most recent, and most common year of birth
        # year_of_birth = yob
        earliest_yob = df['Birth Year'].min()
        most_recent_yob = df['Birth Year'].max()
        most_common_yob = df['Birth Year'].mode()[0]
        print('\n Earliest birth year :  ',earliest_yob)
        print('\n Most recent birth year :  ',most_recent_yob)
        print('\n Most common birth year :  ',most_common_yob)

    except KeyError:
        print('\n\nSorry, there\'s no gender or birth year data for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    # to dispaly the raw data if the user want this 
    x = 1
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break
    
   
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()