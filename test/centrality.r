# Calculate centrality script
# author: Rafael Leano
# last-update: Apr 21, 2015

contents <- read.csv('adjMatrix.csv', header=T)
m <- as.matrix(contents)
rownames(m) <- colnames(m) <- colnames(contents)

library(igraph)
g <- graph.adjacency(m)
evcent <- evcent(g)$vector
plot(evcent)
