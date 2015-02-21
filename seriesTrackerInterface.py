#!/usr/bin/env python2   
   
import seriesTracker
from textwrap import fill

def user_search():
    search_term = raw_input('Series: ')
    series = seriesTracker.search_series(search_term)
    show_number = 1
    for result in series:
        printshow = []
        for index in result:
            printshow.append(''.join(index).encode("utf-8"))
            
        print ( '{0}. {1}: \n    {2} \n   {3}'.format( show_number,printshow[0], printshow[3], printshow[2] ))
        show_number += 1
    show = int(raw_input('Which series: ')) -1
    episode_list = seriesTracker.get_episodes(series[show])
    
    for episode in episode_list:
        printep = []
        for index in episode:
            printep.append(''.join(index).encode("utf-8"))
        if seriesTracker.SYNOPSIS:
            print ('{0}: {1} ({2}):').format( printep[0], printep[1], printep[3])
            print (fill(printep[4], width=80, initial_indent = ' '*4, subsequent_indent=' '*4))
        else:
            print ('{0}: {1} ({2})').format( printep[0], printep[1], printep[3] )
    main()
            
def main():
    print ( '''1. Search for series \n2. Check for series updates \n3. Generate input file to track shows 
4. Change synopsis setting \n5. Exit''' )
    decision = raw_input('#: ')

    if decision == '1':
        user_search()   
    
    elif decision == '4':
        print ('Program shows synopsis: {}'.format(SYNOPSIS))
        synopsis_choice = raw_input("Toggle setting? (Y/n): ")
        if synopsis_choice.upper() == 'Y':
            if seriesTracker.SYNOPSIS == True:
                seriesTracker.SYNOPSIS = False
            else:
                seriesTracker.SYNOPSIS = True
        elif synopsis_choice.upper() != 'N':
            print ('Error: invalid input.')
            
    elif decision == '5':
        pass
        
if __name__ == '__main__':
    main()