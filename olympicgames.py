#Name: Eliyas Philip
#Email: eliyas.philip84@myhunter.cuny.edu

def worldRecord(gender, event):
     """
     Write a function worldRecord(), that takes two parameters: gender (string) and the event type (int). 
     The function should return a float for the Olympic world record for the event. 
     
     Men's Standard, event type 100 meters: record is 9.63 seconds.
     Men's Standard, event type 200 meters: record is 19.30 seconds.
     Men's Standard, event type 400 meters: record is 43.03 seconds.
     Women's Standard, event type 100 meters: record is 10.62 seconds.
     Women's Standard, event type 200 meters: record is 21.34 seconds.
     Women's Standard, event type 400 meters: record is 48.25 seconds.
     Return -1 for any other value
     """
     
     
     if gender == "men":
        if event == 100:
            return float(9.63)
        elif event == 200:
            return float(19.30)
        elif event == 400:
            return float(43.03)
        else:
            return -1

     elif gender == "women":
        if event == 100:
            return float(10.62)
        elif event == 200:
            return float(21.34)
        elif event == 400:
            return float(48.25)
        else:
            return -1
    
     else:
        return -1

     

def main():
     z = input('Enter the gender: ').lower()
     t = int(input('Enter the event distance: '))
     record = worldRecord(z,t)
     print("The record for "+z+"'s "+ str(t) + " meters is", record)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
