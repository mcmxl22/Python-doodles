#!/usr/bin/env python3
"""
score_keeper version 1
Python 3.7
"""


def keep_score():
    """keep score."""

    score1 = 0
    score2 = 0
    
    while True:
        
        try:
            team1 = int(input("Enter team 1 score."))
            team2 = int(input("Enter team 2 score."))

        except ValueError:
            print("You must enter a number.")
        
        else:
            score1 += team1
            score2 += team2
            
            total1 = score1
            total2 = score2
            
            print(f"Team 1: {total1}")
            print(f"Team 2: {total2}")


if __name__ == "__maint__":
    keep_score() 
