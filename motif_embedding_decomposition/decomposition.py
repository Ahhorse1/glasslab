import os
import pandas as pd
import numpy as np

import os
import pandas as pd
import numpy as np

def getMotifCount(peakFile, genome, motifFile, outputDirectory=""):
    
    if not os.path.exists(peakFile):
        print('Path to peak file is incorrect or does not exist\n')
        return 1

    if not os.path.exists(motifFile):
        print('Path to motifs is incorrect or does not exist\n')
        return 1
    
    ## Read in motifFile containing path to .motif files
    motifs = pd.read_table(motifFile, sep="\n", header=None)
    motifs = motifs.to_numpy()
    
    ## Create a string combinining all the .motif paths
#     motifString = ""
#     numOfMotif = motifs.size
#     for i in motifs:
#         motifString = motifString + i[0] + " "
        
    ## Output File
    motifCount = outputDirectory + "motifCount.txt"
    
    ## Call HOMER annotatePeaks to get motif counts
    print('annotatePeaks.pl ' + peakFile + " " + genome + ' -m ' + motifFile + '-nmotifs > '+ motifCount)
    os.system('annotatePeaks.pl ' + peakFile + " " + genome + ' -m ' + motifFile + ' -nmotifs > '+ motifCount)
    
    # Read in HOMER output
    motifCountTable = pd.read_table(motifCount, sep="\t")
    os.system('rm ' + motifCount)
    
    # Reformat HOMER output
    output = outputDirectory + 'motifCounts.csv'
    formattedTable = motifCountTable[ motifCountTable.columns[21:] ]
    formattedTable = formattedTable.transpose()
    formattedTable.columns = motifCountTable.loc[:,motifCountTable.columns[0]]
    formattedTable.columns.name = 'PeakID'
    formattedTable.to_csv(output,header=True, index=True, sep='\t')
    
def getMotifLocation(peakFile, genome, motifFile, outputDirectory="", motifCountFile=""):
    
    if not os.path.exists(peakFile):
        print('Path to peak file is incorrect or does not exist\n')
        return 1

    if not os.path.exists(motifFile):
        print('Path to motifs is incorrect or does not exist\n')
        return 1
    
    ## Read in motifFile containing path to .motif files
    motifs = pd.read_table(motifFile, sep="\n", header=None)
    motifs = motifs.to_numpy()
    
    ## Create a string combinining all the .motif paths
#     motifString = ""
#     numOfMotif = motifs.size
#     for i in motifs:
#         motifString = motifString + i[0] + " "
        
    ## Output File
    homerOutput = outputDirectory + "motifLocations.txt"
    
    # Get Motif Counts
    motifCounts = None
    if motifCountFile == "":
        getMotifCount(peakFile, genome, motifFile, outputDirectory)
        motifCounts = pd.read_table(str(outputDirectory + "motifCounts.csv"), sep="\t", header=0, index_col=0)
    else:
        motifCounts = pd.read_table(motifCountFile, sep="\t", index_col=0)
    
    ## Call HOMER annotatePeaks to get motif positions
    print('annotatePeaks.pl ' + peakFile + ' ' + genome + ' -m ' + motifFile + ' > '+ homerOutput)
    os.system('annotatePeaks.pl ' + peakFile + ' ' + genome + ' -m ' + motifFile + ' > '+ homerOutput)
    
    motifLocations = pd.read_table(homerOutput)
    
    # Set up Columns
    columnNames = motifLocations.columns[21:]
    columnNames = columnNames.insert(0, motifLocations.columns[0])
    columnNames = columnNames.insert(1, motifLocations.columns[1])
    columnNames = columnNames.insert(2, 'Start')
    columnNames = columnNames.insert(3, 'End')
    
    # Set up position Table
    positionTable = motifLocations[ columnNames ]
    positionTable.to_csv('positionTable.csv',header=True, index=True, sep='\t')
    positionTable = positionTable.transpose()
    positionTable.columns = motifLocations[motifLocations.columns[0]]
    positionTable.columns.name = "PeakID"
    
    # Starting X and Ending X for Peak
    peakStart = positionTable.iloc[2]
    peakEnd = positionTable.iloc[3]
    peakMid = (peakEnd-peakStart)/2+peakStart
    
    #
    finalMotifCoords = []
    for i in range(positionTable.columns.size):
        peakMotifCoord = []
        peakID = positionTable.columns[i]
        motifCountsForPeak = motifCounts[positionTable.columns[i]]
        for j in range(motifCountsForPeak.shape[0]):
            peakMotifCount = motifCountsForPeak[j]
            if peakMotifCount == 0:
                peakMotifCoord.append(0)
            else:
                motifCoords = positionTable.loc[motifCounts.index[j]][peakID].split(" ")
                # Coordinate Format = Offset(Sequence,-/+,Score)
                for k in motifCoords:
                    motifFormat = k.split("(")
                    offset = int(motifFormat[0])
                    if k == motifCoords[0]:
                        peakMotifCoord.append(int(peakMid[peakID])+int(offset))
        finalMotifCoords.append(peakMotifCoord)

    finalMotifCoords = pd.DataFrame(finalMotifCoords)
    finalMotifCoords.columns = [motifCounts.index]
    finalMotifCoords.index = [positionTable.columns]
    finalMotifCoords = finalMotifCoords.transpose()
    
    output = outputDirectory + 'motifCoordinates.csv'
    finalMotifCoords.to_csv(output,header=True, index=True, sep='\t')
    
    print("Motif Coordinates of the peak file have been placed in " + output)