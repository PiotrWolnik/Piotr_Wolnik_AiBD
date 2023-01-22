# Zadanie 1 PIPES
# install.packages("magrittr")
library(magrittr)
library(dplyr)

lista = 1:10

lista %<>% log2()  %>% sin() %>% sum() %>% sqrt()
print(lista)

data(iris)
print(head(iris))
aggregated_iris <- iris %>% aggregate(. ~Species, ., mean)


# Zadanie 2 PLOT
# install.packages("ggplot2 ")
library(ggplot2)
my_plot <- ggplot(data = iris, aes(x = Petal.Width)) + geom_histogram(aes(fill=Species, color=Species), bins = 18) + geom_vline(data=aggregated_iris, aes(xintercept=Petal.Width, color=Species), linetype="dashed") + labs(x='x', y='y', title='Petal')
ggsave("~/Desktop/AiBD/Piotr_Wolnik_AiBD/Lab14/plot1.jpg", plot = my_plot)

library("GGally")
my_plot_2 <- ggpairs(data = iris, aes(color=Species))
ggsave("~/Desktop/AiBD/Piotr_Wolnik_AiBD/Lab14/plot2.jpg", plot=my_plot_2)


# Zadanie 3
library(cluster)
x <- iris[,1:4]
y <- iris[, 5]

# Here via c() function we create vector
sum_sqr <- c()

for (i in 1:10){
    kmeans_res = kmeans(x, i)
    sum_sqr <- append(sum_sqr, kmeans_res$tot.withinss) # where tot. withinss : Total within-cluster sum of squares
}

my_plot3 = ggplot(data.frame(iteration=1:length(sum_sqr), value=sum_sqr), aes(x=iteration, y=sum_sqr)) + geom_line()
ggsave("~/Desktop/AiBD/Piotr_Wolnik_AiBD/Lab14/plot3.jpg", plot=my_plot3)

kmeans_res <- kmeans(x, 3)
my_plot4 <- ggplot(iris, aes(x = Sepal.Width, y = Petal.Width, color=kmeans_res$cluster)) + geom_point()
ggsave("~/Desktop/AiBD/Piotr_Wolnik_AiBD/Lab14/plot4.jpg", plot=my_plot4)