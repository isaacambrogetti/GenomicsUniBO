# generate random data
x<-runif(10)  # do ?unif

uniform<-runif(10000)
gauss <- rnorm(10000)

mean(uniform)
mean(gauss)

summary(uniform)
summary(gauss)

# a better way to visualize data (a little more complex)
plot(density(gauss), ylim=c(0,1.5), col="red", lwd=4)
lines(density(uniform), col="blue", lwd=4)

plot(density(gauss))
plot(gauss)

hist(gauss, breaks=100, col="hotpink4")

# RGB coloring convention
# 00 Red  00 Green  00 Blue
# Hexadecimal base
# NUmbers range from 00 to FF
hist(gauss, breaks=100, col="#000000")  # 000000 -> black
hist(gauss, breaks=100, col="#FF0000")  # FF gives the max value 
hist(gauss, breaks=100, col="#FA8872")  # salmon

# brutal way to color
hist(gauss, breaks=100, col="7") 

plot(density(gauss), lwd=10, col="seagreen")


gauss1 <- rnorm(1000, mean=1, sd=0.5)
gauss2 <- rnorm(1000, mean=2, sd=1)

sd(gauss1)
sd(gauss2)

summary(gauss1)
summary(gauss2)

# best way to assess differences between distributions is plotting

plot(density(gauss1))
lines(density(gauss2))  # lines plots only lines data
points(c(2,0.4), pch="*")
text(0,0.5, labels = "Eurovision was an inside job")
