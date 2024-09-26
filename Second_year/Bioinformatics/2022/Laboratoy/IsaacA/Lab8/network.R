library(igraph)

g <- make_empty_graph(5, directed = FALSE)
g #igraph obj

g <- add_edges(g, edges = c(1,2, 2,3, 2,5, 2,4, 4,5, 1,4, 1,5))
plot(g)

# create a node sequence with all nodes of the network
V(g)
E(g)  


# generate networks from scratch
# set node attributes
g <- set_vertex_attr(g, "name", value = LETTERS[1:5])
# or
vertex_attr(g, "name") <- LETTERS[1:5]

# add a note to the network g
g <- add_vertices(g, 1, name = LETTERS[6])
plot(g)

neighbors(g, 1)
adjacent_vertices(g, 1)
# query the adjacent nodes for multiple nodes at once
adjacent_vertices(g, c(1,2))

### CREATE SPECIAL GRAPHS ###
## Simple star graph
st <- make_star(20, mode = "out", center = 1)
#set node attribute name
V(st)$name <- c("Dumbledore", rep("D.Army", 19))
plot(st, vertex.size = 10, vertex.color = "skyblue")

## Erdos-Renyi random graph model
# n is number of nodes, m is the number of edges
er <- sample_gnm(n = 100, m = 40)
plot(er, vertex.size = 10, vertex.label = NA)

## Generate a network from a list of links
hp <- graph( c("Harry", "Ron", "Ron", "Hermione", "Ron", "Hermione", "Harry", "Hermione", "Draco", "Piton"), isolates = c("Raptor", "Voldemort"), directed = F)
# in named graphs, we can specify isolates by providing a list of their names
plot(hp, vertex.color = "skyblue", vertex.size = 15, vertex.frame.color = "blue", vertex.color.label = "black", vertex.label.cex = 0.8, edge.curved = 0.2)
# list names of vertices attributes
V(hp)$name
V(hp)$soul <- c("hero", "hero", "hero", "villain", "hero", "villain", "villain")
# list names of links attributes
edge_attr_names(hp) # 0
E(hp)$type <- "friendship"
E(hp)$weight <- 10
# Examine attributes
edge_attr(hp)
vertex_attr(hp)
# Plot according to node attribute soul
plot(hp, vertex.label.color = "black", vertex.label.dist = 2, vertex.color = c ("pink", "skyblue")[1+(V(hp)$soul=="hero")])
# Simplify the network
hps <- simplify(hp, remove.multiple = T, edge.attr.comb = c(weight="sum", type="ignore"))
E(hps)$weight
plot(hps, vertex.label.dist=2)

### EXERCISE 1  ###
JUN <- make_star(21, mode = "undirected", center = 1)
V(JUN)$name <- c("JUN", "ARHGEF2", "MOV10", "PLK3", "NECAP2","TNFRSF14",
                 "NAV1","GBAP1", "PPOX","CROCCP3", "TMEM200B",
                 "PERM1","TPM3","TBX15","TMEM201","SYNC",
                 "DCAF6","FABP3","C1orf21","MYOM3","DHCR24")
   
plot(JUN, vertex.size = 10, vertex.color = c("yellow1", rep("indianred2", 10), rep("royalblue2", 10)),
     vertex.label.color = "black", vertex.label.dist = 2)

JUN
ARHGEF2   0.5773276
MOV10     0.5638909
PLK3      0.5617062
NECAP2    0.5587605
TNFRSF14  0.5393239
NAV1      0.5267166
GBAP1     0.5247581
PPOX      0.5219732
CROCCP3   0.5181625
TMEM200B  0.5107476
PERM1    -0.2948076
TPM3     -0.2760985
TBX15    -0.2547711
TMEM201  -0.2547608
SYNC     -0.2449694
DCAF6    -0.2407771
FABP3    -0.2406114
C1orf21  -0.2402021
MYOM3    -0.2375846
DHCR24   -0.2356979



# Emilia
emi <- graph(c("Emi","Biglietto", "Emi","Solitario", "Emi","GoT", "Emi","Lezione", "Emi","Drummino", "Solitario","Pubblicità", "Drummino","Chiacchiere", "Emi","Chiacchiere"), directed = F)
plot(emi, vertex.color = "Green", vertex.color.label = "Bluesky")
emi <- set_edge_attr(emi, "weight", value = c(0.1, 0.1, 0.01, 0.5, 0.1, 0.1, 0.1, 0.1))


# exercise 2
g <- make_empty_graph(6, directed = FALSE)
g <- add.edges(g, edges = c(1,2, 1,3, 1,4, 1,5, 1,6, 2,3, 3,4, 3,5, 4,5))
plot(g)
as_adjacency_matrix(g)
as_adj_list(g)
as_edgelist(g)


JUN <- make_star(21, mode = "undirected", center = 1)
V(JUN)$name <- c("JUN", "ARHGEF2", "MOV10", "PLK3", "NECAP2","TNFRSF14",
                 "NAV1","GBAP1", "PPOX","CROCCP3", "TMEM200B",
                 "PERM1","TPM3","TBX15","TMEM201","SYNC",
                 "DCAF6","FABP3","C1orf21","MYOM3","DHCR24")

plot(JUN, vertex.size = 10, vertex.color = c("yellow1", rep("indianred2", 10), rep("royalblue2", 10)),
     vertex.label.color = "black", vertex.label.dist = 2)
JUN_adjmat <- as_adjacency_matrix(JUN)
JUN_adjlist <- as_adj_list(JUN)
JUN_edgelist <- as_edgelist(JUN)

JUN_mat <- as.matrix(JUN_edgelist)
colnames(JUN_mat) <- c("source","target")
write.csv(JUN_mat, "JUN_edgelist.csv")
