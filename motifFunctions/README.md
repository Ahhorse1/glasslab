# Motif Methods
- [getMotifCount](#getMotifCount)
- [getMotifLocation](#getMotifLocation)
- [getMotifCoordDiff](#getMotifCoordDiff)

>:warning: These methods rely on having [HOMER](http://homer.ucsd.edu/homer/) and the genomes you wish to use installed. You can learn more about [HOMER here](http://homer.ucsd.edu/homer/).

# getMotifCount
getMotifCount( peakFile, genome, motifFile, outputDirectory (Optional) )

This function provides the count of each motif in each peak.
## Paramters:
**peakFile** - File path to peak file 

**genome** - Genome that peak file is from 

**motifFile** - .motif file containing all the motifs

**outputDirectory** - The output directory you would like the function to output to, this is an optional parameter, if not specified it will output in the directory where this code is run.
Include the / in your input, for example if the directory is glasslab/data, input it as glasslab/data/

## Output:
The program will output the counts to a csv file named motifCounts.csv in the following format. 
The csv file is separated by tabs and has a header and index. 
You can read it in pandas like this pd.read_table('motifCounts.csv', sep='\t', header=0, index_col=0)

| File            | peak1 | peak2  |  ...  | peakX  |
| --------------- | ----- | ------ | ----- | ------ |
| Count of Motif1 |   a1  |   b1   |  ...  |   x1   |
| Count of Motif2 |   a2  |   b2   |  ...  |   x2   |
|  ...            |  ...  |   ...  |  ...  |  ...   |
| Count of MotifY |   aY  |   bY   |  ...  |   xy   |

## Example Usage:
Will produce motifCount.csv in the same directory where program is run

` getMotifCount ("peaks_categ1.csv","mm10","combinedMotifs.motif") `

Will produce motifCount.csv in the directory /user/test/

` getMotifCount ("peaks_categ1.csv","mm10","combinedMotifs.motif","/user/test/") `


# getMotifLocation

getMotifLocation( peakFile, genome, motifFile, outputDirectory (Optional), motifCount (Optional))

This function provides the starting location of motifs in each peak, if there is more than one motif in a peak, it will only provide the starting location of the first motif.
## Paramters:
**peakFile** - File path to peak file 

**genome** - Genome that peak file is from 

**motifFile** - .motif file containing all the motifs

**outputDirectory** - The output directory you would like the function to output to, this is an optional parameter, if not specified it will output in the directory where this code is run.
Include the / in your input, for example if the directory is glasslab/data, input it as glasslab/data/

**motifCounts** - csv file containing the counts of motif, only the format outputted by getMotifCounts will work. This is an optional parameter

## Output:
The program will output the coordinates to a csv file named motifCoordinates.csv in the following format. 
The csv file is separated by tabs and has a header and index. 
You can read it in pandas like this pd.read_table('motifCoordinates.csv', sep='\t', header=0, index_col=0)

| File            | peak1 | peak2  |  ...  | peakX  |
| --------------- | ----- | ------ | ----- | ------ |
| Starting Coordinate of Motif1 for Corresponding Peak: |   a1  |   b1   |  ...  |   x1   |
| Starting Coordinate of Motif2 for Corresponding Peak: |   a2  |   b2   |  ...  |   x2   |
|  ...            |  ...  |   ...  |  ...  |  ...   |
| Starting Coordinate of MotifY for Corresponding Peak: |   aY  |   bY   |  ...  |   xy   |

## Example Usage:

Will produce motifCoordinates.csv in the same directory program is run, and assumes motifCounts.csv is in the same directory

`getMotifLocation("peaks_categ1.csv","mm10","combinedMotifs.motif","","motifCounts.csv")`


Will produce motifCoordinates.csv and motifCounts.csv file in the same directory the program is run

`getMotifLocation("peaks_categ1.csv","mm10","combinedMotifs.motif","","")`

Will produce motifCoordinates.csv and motifCounts.csv in the directory /user/test/

`getMotifLocation("peaks_categ1.csv","mm10","combinedMotifs.motif","/user/test/","")`

# getMotifCoordDiff
getMotifCoordDiff( motifCoordinatesFile, outputDirectory (optional) )

The function provides a N by M matrix containing the differences between the location of motifs on each peak given a motif coordinates file provided by the getMotifLocation function. N is the number of peaks and M is the number of motifs of interest.
## Parameters:
**motifCoordinatesFile** - Filepath to the csv file containing the motif coordinates. This is provided by getMotifLocation function

**outputDirectory** - The output directory you would like the function to output to, this is an optional parameter, if not specified it will output in the directory where this code is run. Include the / in your input, for example if the directory is glasslab/data, input it as glasslab/data/

## Output
The program will output the coordinates to a csv file named coordinateDifference.csv in the following format. 
The csv file is separated by tabs and has a header and index. 
You can read it in pandas like this pd.read_table('motifCoordinates.csv', sep='\t', header=0, index_col=0)

| File            | peak1 | peak2  |  ...  | peakN  |
| --------------- | ----- | ------ | ----- | ------ |
| (Motif1_Coordinate)-(Motif2_Coordinate) |   a1  |   b1   |  ...  |   x1   |
| (Motif1_Coordinate)-(Motif3_Coordinate) |   a2  |   b2   |  ...  |   x2   |
|  ...            |  ...  |   ...  |  ...  |  ...   |
| (MotifM-2_Coordinate)-(MotifM-1_Coordinate) |   aY  |   bY   |  ...  |   xy   |

N is the number of peaks and M is the number of motifs
## Example Usage:

Will produce coordinateDifference.csv in the same directory the program is run

`getMotifCoordDiff("motifCoordinates.csv")`

Will produce coordinateDifference.csv in the the directory /user/test/

`getMotifLocation("motifCoordinates.csv","/user/test/","")`
