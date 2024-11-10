library(ggplot2)

data <- read.table(file("stdin"), header = FALSE, sep = "\t", col.names = c("X", "Y", "Category"))
# print(head(data))
args <- commandArgs(trailingOnly = TRUE)
output_file <- args[1]            
x_label <- args[2]                 
y_label <- args[3]                 
plot_title <- args[4]             
#print(output_file)
plot <- ggplot(data, aes(x = X, y = Y, color = Category)) +
  geom_line() +
  labs(title = plot_title, x = x_label, y = y_label)

ggsave(output_file, plot, width = 8, height = 6)

