import os;
import random;

#Game settings
varGuessAllowed = 10;
varEndNumber = 1000;
varStartNumber = 1;
varRestartGame = True;
varEnableProgress = False;
varEnableHelp = False;

#Game start values
varCorrectGuessCount = 0;
varGameCount = 0;
varUserInput = 0;
varMaxUserGuess = 0;
varMinUserGuess = 0;

#Functions
def ActivateProgress():
    global varEnableProgress;
    
    varInput = input("Vil du aktivere process? [J/N] ");
    if(varInput == "J" or varInput == "j"):
        varEnableProgress = True;      

def ActivateHelp():
    global varEnableHelp;
    varInput = input("Vil du aktivere hjælp? [J/N] ");
    if(varInput == "J" or varInput == "j"):
        varEnableHelp = True;

def ShowHelp():
    varInputHelp = input("Vil du have vist intro hjælpen? [J/N] ");
    if(varInputHelp == "J" or varInputHelp == "j"):
        GameHelp();
        
def UserInput():
    global varUserInput;
    try:
        varUserInput = int(input("Indtast et tal: "));
    except ValueError:
        print("Du skal indtaste et tal.");
        UserInput();
        
def GameIntro():
    print("");
    print("Velkommen til Gæt et tal!");
    print("Spillet arbejder med halvering og sandsynlighed.");
    print("Du har " + str(varGuessAllowed) + " forsøg.");
    print("Dit mål er at gætte et tilfældigt tal mellem " + str(varStartNumber) + " og " + str(varEndNumber));
    print("------------------------------------------------------")
    print("");
    
def GameIntroRetry():
    print("");
    print("Prøv om du kan gætte tallet igen.");
    print("Du har " + str(varGuessAllowed) + " forsøg.");
    print("Dit mål er at gætte et tilfældigt tal mellem " + str(varStartNumber) + " og " + str(varEndNumber));
    print("------------------------------------------------------")
    print("");
    
def GameHelp():
    print('''
            Dit mål er at gætte tallet som computeren har udvalgt.
            du kan gætte løs, eller du kan bruge halvering.
            Med halvering burde du kunne gætte tallet med mellem 6 og 10 forsøg.
            \n
            === Strategi: ===
            Start med et tal i midten af største og mindste - hvis midste er 1 og største er 1000
            skal du starte med 500.
            \n
            Du får nu at vide om tallet er større eller mindre.
            \n
            Resultatet kan se ud som her:
            Prøv igen med et mindre nummer...
            0 <== 500? ==> 500
            \n
            Du ved nu at tallet du leder efter er mellem 0 og 500
            Prøv så at halvere her er det fx. 250 der er midt i mellem 0 og 500
            
            Resultatet kan se ud som her:
            Prøv igen med et større nummer...
            250 <== 250? ==> 500
            \n
            Du ved nu at tallet du leder efter er mellem 250 og 500
            Prøv så at halvere her er det fx. 375 der er midt i mellem 250 og 500
            \n
            Resultatet kan se ud som her:
            Prøv igen med et mindre nummer...
            250 <== 375? ==> 375
            
            På den måde fortsætter du til du rammer det rigtige tal.
            
            Når du gætter rigtigt vil det se sådan her ud:
            
            546<== 550! ==>554
            Du vandt! Du brugte 8 gæt. Flot!

            === Hjælp slået til ===
            
            Hvis du har hjælp slået til vil computeren komme med et forslag til næste tal
            og også fortælle hvor mange muligheder der er tilbage:

            0<== 500 mulige - prøv evt. 250 ==>500

            === Sådan halverer du: ===

            Mindste tal + største tal / 2
            fx 200 + 300 / 2 = 250
            altså bør de næste gæt være 250
    ''');
    
def UserGuessProgress(varInput):
    global varMaxUserGuess;
    global varMinUserGuess;
    global varEnableHelp;
    global varEndNumber;
    
    if(varMinUserGuess < varMaxUserGuess):
        if(varMaxUserGuess < varMinUserGuess):
            varPossible = varEndNumber - varMinUserGuess;
        else:
            varPossible = varMaxUserGuess - varMinUserGuess
    else:
        if(varMaxUserGuess < varMinUserGuess):
            varPossible = varEndNumber - varMinUserGuess;
        else:
            varPossible = varMinUserGuess - varMaxUserGuess;
        
    if (varMaxUserGuess < varMinUserGuess):
        varBestGuess = (varEndNumber + varMinUserGuess)/2;
    else:
        varBestGuess = (varMaxUserGuess + varMinUserGuess)/2;
    if(varEnableHelp):
        print(str(varMinUserGuess) + "<== "+str(varPossible)+" mulige - prøv evt. "+str(int(varBestGuess))+" ==>" + str(varMaxUserGuess));
    else:
        print(str(varMinUserGuess) + "<== ? ==>" + str(varMaxUserGuess));

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear');

#Start game
try:
    ActivateProgress();
    ActivateHelp();
    
    while(varRestartGame):
        varEndGame = False;
        varGuessNumber = random.randint(varStartNumber,varEndNumber)
        varGuessCount = 1;
        varGameCount = varGameCount +1;
        varMaxUserGuess = 0;
        varMinUserGuess = 0;
        
        clearConsole();
        
        if(varGameCount <= 1):
            GameIntro();
            ShowHelp();
        else:
            GameIntroRetry();
        
        while varEndGame == False:
            UserInput();
            clearConsole();
            if(varUserInput in range(varStartNumber,varEndNumber)):
                if(varUserInput == varGuessNumber):
                    print(str(varMinUserGuess) + "<== "+str(varGuessNumber)+"! ==>" + str(varMaxUserGuess));  
                    print("Du vandt! Du brugte " + str(varGuessCount) + " gæt. Flot!");
                    varCorrectGuessCount = varCorrectGuessCount +1;
                    varEndGame = True;
                elif(varGuessCount == varGuessAllowed):
                    print("Du gættede ikke tallet, tallet var: " + str(varGuessNumber));
                    varEndGame = True;
                else:
                    if(varUserInput > varGuessNumber):
                        print("Du tastede: " + str(varUserInput));
                        print("Prøv igen med et mindre nummer...");
                        varMaxUserGuess = varUserInput;
                    elif(varUserInput < varGuessNumber):
                        print("Du tastede: " + str(varUserInput));
                        print("Prøv igen med et større nummer...");
                        varMinUserGuess = varUserInput;
                    UserGuessProgress(varUserInput) if varEnableProgress else "";
                    varGuessCount = varGuessCount+1;
            else:
                print("Hov! Det nummer er alt for stort!");
                print("Dit gæt tæller ikke med i antallet af gæt, så prøv igen.");
        
        varAnswer = input("Vil du prøve igen? [J/N] ");
        if(varAnswer == "N" or varAnswer == "n"):
            print("");
            print("Du spillede " + str(varGameCount) + " spil og vandt " + str(varCorrectGuessCount) + " spil. Det giver " + str((varCorrectGuessCount/varGameCount)*100) + "% rigtige.");
            varRestartGame = False;

except KeyboardInterrupt:
    print("");
    print("Du afsluttede spillet med CTRL+C - Tak for at du spillede 'Gæt et tal'");
    if(varGameCount > 1):
        print("Du spillede " + str(varGameCount) + " spil og vandt " + str(varCorrectGuessCount) + " spil. Det giver " + str((varCorrectGuessCount/varGameCount)*100) + "% rigtige.");
    exit();
