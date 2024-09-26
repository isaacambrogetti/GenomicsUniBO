# TSNE  projection all variance on two dimensions

# install and load Rtsne
install.packages("Rtsne")
library(Rtsne)

# run the algorithm
set.seed(1) # it's not plaged because of the seed it's just because the algorithm is not deterministic
ttt <- Rtsne(t(expmat))

# extract coordinates of cells
x <- ttt$Y[,1]
y <- ttt$Y[,2]

# Plot coordinates of cells
plot(x, y, main="TSNE") #TSNE is not pure deterministic, so you need to set seed

x[1:3]
y[1:3]
