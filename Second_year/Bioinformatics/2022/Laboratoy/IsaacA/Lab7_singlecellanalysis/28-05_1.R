# single cell file reduced to get an easy download

install.packages("Seurat")
library("Seurat")

# set directory and create an object of the document
setwd("C:/Users/Isaac/Desktop/Genomics/SecondYear/Bioinformatics/LABORATORY/Lab6_singlecellanalysis")
rawcounts<-read.delim("rawcounts.txt")
# alternative
#rawcounts <- read.delim("https://www.dropbox.com/s/3uz6txc5bs4kwlb/rawcounts.txt?dl=1")


# always first command for loading a matrix (table)
dim(rawcounts)

head(rawcounts) # not good for wide matrices

rawcounts[1:5,1:3]  # splicing

# DEBUGGING ONLY
is.numeric(rawcounts) # False, because whenever you load a big file, it forms a dataframe which can contain a mixture of numbers, and strings
is.data.frame(rawcounts)

# embed the object into a Seurat object (for the same reason of the dataset thing we saw)
seuset <- CreateSeuratObject(counts = rawcounts)

rawcounts

seuset

str(seuset)

# as we can see, the count data is now a Sparse matrix
seuset@assays$RNA@counts  # dots became 0, it is more useful for compress it and easier to use for calculation

seuset@assays$RNA@counts@Dimnames[1]


# slide 45
# Normalize and Scale the gene expression raw count data
seuset <- NormalizeData(seuset) # normalization is necessary for most if not all downstream operations
seuset <- ScaleData(seuset)

seuset
str(seuset)

# Extract the normalized data
expmat<-seuset@assays$RNA@scale.data
expmat[1:5,1:3]     # expmat is the name used by USA for normalized and scaled data

seuset@meta.data

# Principal Component Analysis
# we start with expmat
?prcomp
ppp <- prcomp(t(expmat)) # t() is the transpose function.
# ... si that PCA is done for visualizing cells, nor genes

ppp
str(ppp)

# we can get the first two components
# components are the orientations giving the most variance
# the first two components by definition are those capturing the 
x <- ppp$x[,1]
y <- ppp$x[,2]

plot(x,y, main = "single cell RNA-Seq - PCA projection")

x[1:3]
y[1:3]
