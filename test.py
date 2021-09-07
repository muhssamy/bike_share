import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
week_days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']

def get_filters():


    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    while True :

        city = input("Please choose your target city like (chicago, new york city, washington): \n").lower()
        if city in CITY_DATA.keys():
            break
        else:
            print ("THIS IS INVALID INPUT : ")
    while True :
        month = input("Please enter full month name you need to filter with like (january, february, ...): \n ").lower()
        if month in months:
            break
        else :
            print ("THIS IS INVALID INPUT : ")
    while True :
        day = input("Please enter full day name you need to filter with like (saturday, sunday, ...) : \n ").lower()
        if day in week_days:
            break
        else:
            print ("THIS IS INVALID INPUT : ")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    most_common_month = df['month'].mode()[0]
    most_common_day = df['day_of_week'].mode()[0]
    popular_hour = df['Start Time'].dt.hour.mode()[0]


    # TO DO: display the most common month

    print("MOST POPULAR MONTH PEOPLE RIDE BIKES IS : {} \n".format(most_common_month))
    print("MOST POPULAR Day PEOPLE RIDE BIKES IS : {} \n".format(most_common_day))
    print("MOST POPULAR hour PEOPLE RIDE BIKES IS : {} \n".format(popular_hour))


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_popular_start_station = df['Start Station'].mode()[0]
    most_popular_end_station = df['End Station'].mode()[0]
    most_frequent_combination = df['Start Station'].max()
    #(df['Start Time'].value_counts.max()) + (df['End Time'].value_counts.max())


    # TO DO: display most commonly used end station
    print("MOST POPULAR START STATION PEOPLE RIDE BIKES IS : {} \n".format(most_popular_start_station))
    print("MOST POPULAR END STATION PEOPLE RIDE BIKES IS : {} \n".format(most_popular_end_station))
    print("MOST Frequent Station PEOPLE RIDE BIKES IS : {} \n".format(most_frequent_combination))

    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_travel_time = df['Trip Duration'].sum()
    avg_travel_time = df['Trip Duration'].mean()
    print ("Total travel Time = : {}".format(total_travel_time))
    print ("average travel Time = : {}".format(avg_travel_time))


    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_type = df['User Type'].value_counts()
    print (user_type)
    while True:
        if 'Gender' in df.columns:
            gender_type = df['Gender'].value_counts()
            print("gender type as following : {}\n \n ".format(gender_type))
            break
        else:
            print("NO Gender Data")
            break
    while True:
        if 'Birth Year' in df.columns:
            earliest_users = df['Birth Year'].min()
            most_recent_users = df['Birth Year'].max()
            most_common_year = df['Birth Year'].mode()

            print("user types according to age oldest as following : {}\n \n ".format(earliest_users))
            print("user types according to age youngest as following : {}\n \n ".format(most_recent_users))
            print("user types according to most common age as following : {}\n \n ".format(most_common_year))


            break
        else:
            print("NO Age Data")
            break

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#def display_raw_data(df):
   # data = 0


  #  while True:
      #  answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
       # if answer.lower() == 'yes':
        #    print(df[data : data+5])
          #  data += 5


       # else:
        #    break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
       # display_raw_data(df)
        see_data = input('would you like to see some of data? Enter yes or no.\n')

        for i in range(5 , df.shape[0]):
            if see_data.lower() == 'yes':
                print(df.head(i))
                see_data = input('would you like to see some of data? Enter yes or no.\n')
                if see_data.lower() == 'yes':
                    i += 5
                    print(df.head(i))
                else:
                    break
            else:
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
