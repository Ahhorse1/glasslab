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
    motifString = ""
    numOfMotif = motifs.size
    for i in motifs:
        motifString = motifString + i + " "
        
    ## Output File
    motifCount = outputDirectory + "motifCount.txt"
    
    ## Call HOMER annotatePeaks to get motif counts
    print('annotatePeaks.pl ' + peakFile + " " + genome + ' -m ' + motifString[0] + '-nmotifs > '+ motifCount)
    os.system('annotatePeaks.pl ' + peakFile + " " + genome + ' -m ' + motifString[0] + ' -nmotifs > '+ motifCount)
    
    # Read in HOMER output
    motifCountTable = pd.read_table(motifCount, sep="\t")
    os.system('rm ' + motifCount)
    
    # Reformat HOMER output
    output = outputDirectory + 'motifCounts.csv'
    formattedTable = motifCountTable[ motifCountTable.columns[-numOfMotif:] ]
    formattedTable = formattedTable.transpose()
    formattedTable.columns = motifCountTable.loc[:,motifCountTable.columns[0]]
    formattedTable.columns.name = 'PeakID'
    formattedTable.to_csv(output,header=True, index=True, sep='\t')
    
    print("Motif counts of the sequence have been placed in " + output)