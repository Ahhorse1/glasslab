# getMotifCount( peakFile, genome, motifFile, outputDirectory (Optional) )
This function provides the count of each motif in each peak.
## Paramters:
### peakFile
File path to peak file 
### genome
Genome that peak file is from 
### motifFile
.motif file containing all the motifs
### outputDirectory
The output directory you would like the function to output to, this is an optional parameter, if not specified it will output in the directory where this code is run.
Include the /, in your input, for example if the directory is glasslab/data, input it as glasslab/data/
## Output
The program will output the counts to a csv file named motifCounts.csv in the following format. 
The csv file is separated by tabs and has a header and index. 
You can read it in pandas like this pd.read_table('motifCounts.csv', sep='\t', header=0, index_col=0)

| File            | peak1 | peak2  |  ...  | peakX  |
| --------------- | ----- | ------ | ----- | ------ |
| Count of Motif1 |   a1  |   b1   |  ...  |   x1   |
| Count of Motif2 |   a2  |   b2   |  ...  |   x2   |
|  ...            |  ...  |   ...  |  ...  |  ...   |
| Count of MotifY |   aY  |   bY   |  ...  |   xy   |


# getMotifLocation( peakFile, genome, motifFile, outputDirectory (Optional), motifCount (Optional))
This function provides the starting location of motifs in each peak, if there is more than one motif in a peak, it will provide the starting location of the first motif.
## Paramters:
### peakFile
File path to peak file 
### genome
Genome that peak file is from 
### motifFile
.motif file containing all the motifs
### outputDirectory
The output directory you would like the function to output to, this is an optional parameter, if not specified it will output in the directory where this code is run.
Include the /, in your input, for example if the directory is glasslab/data, input it as glasslab/data/
### motifCounts
csv file containing the counts of motif, only the format outputted by getMotifCounts will work. This is an optional parameter

## Output
The program will output the coordinates to a csv file named motifCoordinates.csv in the following format. 
The csv file is separated by tabs and has a header and index. 
You can read it in pandas like this pd.read_table('motifCoordinates.csv', sep='\t', header=0, index_col=0)

| File            | peak1 | peak2  |  ...  | peakX  |
| --------------- | ----- | ------ | ----- | ------ |
| Starting Coordinate of Motif1 for Corresponding Peak: |   a1  |   b1   |  ...  |   x1   |
| Starting Coordinate of Motif2 for Corresponding Peak: |   a2  |   b2   |  ...  |   x2   |
|  ...            |  ...  |   ...  |  ...  |  ...   |
| Starting Coordinate of MotifY for Corresponding Peak: |   aY  |   bY   |  ...  |   xy   |