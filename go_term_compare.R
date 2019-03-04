eggnog <- read.delim("eggnogmap_results/diamond_annotations.tabular",
                     stringsAsFactors = FALSE,
                     header = FALSE)
library(stringr)
library(dplyr)
eggnog_gos <- unlist(str_split(eggnog$V6, ",")) %>% unique()

metagomics_gos <- read.delim("metaGOmics_results/go_compare_149_150.txt",
                             stringsAsFactors = FALSE,
                             comment.char = "#")$GO.acc %>% unique()

megan_gos <- read.delim("MEGAN_outputs/go_terms.txt", header = FALSE, stringsAsFactors = FALSE)$V1 %>% unique()

# unipept
unipept_results_NS <- paste('unipept_results/',
                               list.files("unipept_results/", pattern = "^737NS.*\\.csv"),
                               sep = "")
unipept_results_WS <- paste('unipept_results/',
                               list.files("unipept_results/", pattern = "^737WS.*\\.csv"),
                               sep = "")
unipeptNS <- lapply(unipept_results_NS, function(i) {
        read.delim(i, sep = ',', as.is = TRUE)}) %>%
    bind_rows() %>%
    select(-X) %>%
    rename(peptides = X.peptides)
unipeptWS <- lapply(unipept_results_WS, function(i) {
    read.delim(i, sep = ',', as.is = TRUE)}) %>%
    bind_rows() %>%
    select(-X) %>%
    rename(peptides = X.peptides)

unipept_all <- inner_join(unipeptNS, unipeptWS, by = c("GO.term", "Name")) %>%
    rename(countNS = peptides.x, countWS = peptides.y) %>%
    mutate(log2ratio = log(countWS/countNS))

unipept_gos <- unipept_all$GO.term %>% unique()

library(eulerr)

plot(euler(list(eggnog = eggnog_gos, metagomics = metagomics_gos, megan = megan_gos, unipept = unipept_gos)),
     quantities = TRUE)
