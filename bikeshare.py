from calendar import day_name
import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let\'s explore some US bikeshare data!")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        
        city = input('\nPlease enter choose a city from (chicago, new york city, washington)\n').lower()
        if city not in CITY_DATA:
            print('please enter a valid entry')
        else:
            break
        
    while True:
        month = input('\nplease choose a month from january to june, or type all\n').lower()
        months = ['january','february','march','april','may','june','all']
        if month != 'all' and month not in months:
            print('incorrect enrty please renter a valid month')
        else:
            break
    while True:
        day = input('\nplease choose a day\n').lower()
        days= ['monday','tuesday','wednesday','thursday','friday','all']
        if day != 'all' and day not in days:
            print('\nplease enter a correct day name\n')
        else:
            break
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

#asking the user if they want to display raw data
def display_raw_data(city):
    display_raw = input('\nWould you like to see the raw data? Enter yes or no.\n')
        
    
    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city],chunksize=5):
                print(chunk)
                break
            display_raw = input('\nWould you like to see another 5 rows of the raw data? Enter yes or no.\n')
            if display_raw != 'yes':
                print('Thank You')
                # here we get out of the for loop on the chunks
            break
        except KeyboardInterrupt:
             print('Thank you')
             
def time_stats(df):     
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("The most frequent month is: " , common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("the most frequent day is: " + common_day)

    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most frequent start hour is: "+ str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most frequent start station is: " + common_start_station)
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most frequent end station is: " + common_end_station)

    # display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time from the given data is: " + str(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time from the given data is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types is: \n" + str(user_types))
    return df
    # Display counts of gender
def user_stats_gender(df):
    """Displays statistics of analysis based on the gender of bikeshare users."""

    # Display counts of gender

    if ((city == 'chicago.csv') , (city == 'new_york_city.csv')):
        gender = str(df['Gender'].value_counts())
        print("The count of user gender is: \n" + gender)
    return df

    # Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].min()
    most_recent_birth = df['Birth Year'].max()
    most_common_birth = df['Birth Year'].mode()[0]
    print('Earliest birth is: {}\n'.format(earliest_birth))
    print('Most recent birth is: {}\n'.format(most_recent_birth))
    print('Most common birth is: {}\n'.format(most_common_birth) )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def main():
    while True:
        city, month, day = get_filters()
        #df = get_filters()
        print(city, month, day)
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()