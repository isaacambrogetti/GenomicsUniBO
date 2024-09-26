x<- rnorm(1000)
y<- x + rnorm(1000)

plot(y)

eurovision <- c(3, 12, 15, 20)
mean(eurovision)
sd(eurovision)
log10(eurovision)

summary(eurovision)
boxplot(eurovision)

# clear the environment
rm(list=ls())


