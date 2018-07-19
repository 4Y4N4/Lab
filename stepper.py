class Controller:
    

    # Read wait time and diraction from command line
    def revolutionSetting(self,arg1):
        if float(arg1)>1: 
            WaitT = float(arg1)/float(1000)
            StepD = 1
        elif float(arg1)<-1:
            WaitT = -float(arg1)/float(1000)
            StepD = -1
        elif (float(arg1)>=-1)and(float(arg1)<0):
            WaitT = -float(arg1)/float(1000)
            StepD = -1
        else:
            WaitT = float(arg1)/float(1000)
            StepD = 1
        return [WaitT, StepD]
 



        
    def seqSetting(self,arg2):
        
        seq1 = [[1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1],
                [1,0,0,1]]

        seq2 = [[1,0,0,0],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1]]

        seq3 = [[1,0,0,1],
                [1,1,0,0],
                [0,1,1,0],
                [0,0,1,1]]

        tempSeq = [seq1, seq2, seq3]
        return tempSeq[arg2]






"""
    def mainLoof(self, Seq, waitT, Dir):
        count = 0
        StepCounter = 0
        while True:
            if pin >= len(seq):
                pi= 0
            print (StepCounter)
            print (Seq[StepCounter])
            for pin in range(0, 4):
                xpin = StepPins[pin]
                if Seq[StepCounter][pin]!=0:
                    print ("Enable GPIO %i" %(xpin)
                    GPIO.output(xpin, True)
                else:
                GPIO.output(xpin, False)

                StepCounter += StepDir

            # If we reach the end of the sequence
            # start again
            if (StepCounter>=StepCount):
                StepCounter = 0
            if (StepCounter<0):
                StepCounter = StepCount+StepDir

            # Wait before moving on
            time.sleep(WaitTime)
            #time to break
            if False:
                break
"""
