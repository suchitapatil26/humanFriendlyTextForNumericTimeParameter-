import inflect
import sys
class TalkingClock(object):
    def __init__(self):  # validating and initializing the instance variable
        self.hh = None
        self.mm = None


    #Validating minutes and hours and represent in to integer format by using instance variable hh and mm
    def validate(self, timeInString):
        timeinlist = timeInString.split(':')
        if len(timeinlist) == 2:  # checking for valid input and if valid cretate instance variable by seperate hh and mm
            try:
                hh = int(timeinlist[0])
                mm = int(timeinlist[1])
                if hh > 23 or mm > 59:
                    raise Exception("invalid input.(hh should be in range 0-23 and mm should ne 0-59)")
                else:
                    self.hh = hh
                    self.mm = mm
                    return True
            except ValueError:
                print("invalid input.")

            except Exception as e:
                print(e)
        else:
            return False

    # Human readable format of clock display function
    def humanFriendlyText(self,timeInString):
      if self.validate(timeInString):
        if self.mm==0:  # for case 1: 1:00 One o'clock
            string = self.time2WordConvert(self.hh)
            readAs='O\'clock'
            minute=""
            return(hour + ' ' + readAs)
        elif self.mm<=30: # for case 2: 13:05 Five past one
            if self.mm==30: # for case 2.1:	13:30 Half past one
                minute='Half'
            else:
                minute=self.time2WordConvert(self.mm) #conerting minute to word format
            readAs='past'
            hour=self.time2WordConvert(self.hh%12)  #converting hour to 12 hour clock  word format
        else:      # for case 3: 13:35 Twenty five to two
            minute = self.time2WordConvert(60-self.mm) # remaining minutes calculation in word format
            readAs = 'to'
            hour = self.time2WordConvert((self.hh % 12)+1) #converting hour to 12 hour clock word format
        return(minute + ' '+readAs+' '+hour)
      else:
          return('invalid input')


# time2WordConvert function for converting number format to word format.
    def time2WordConvert(self,number):
        numtowordconverter=inflect.engine() #Create an inflect engine
        wordform=numtowordconverter.number_to_words(number) #convert number to Word format represent - for connecting words
        wordform=wordform.replace('-', ' ').capitalize() #replace - with space and capitaliz first letter of string
        return(wordform)




if __name__ == '__main__':
    #humanclock = TalkingClock("13:12")
    if len(sys.argv) < 2:
        print('input missing!!!')
    else:
       clock = TalkingClock()
       print(clock.humanFriendlyText(sys.argv[1]))


