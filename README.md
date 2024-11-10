# bec-513-coding-questions

## clone the repository 
```
git clone https://github.com/manojmahan/bec-513-coding-questions.git
```
 
## Q1: Selecting lines from stdin (Python Code + Linux Command)
Python code gets the data using stdin iterates through each row and checks if that row has any of the patterns
if it row has a pattern it will write the row to the output the file

run the following code to get the desired lines
```
zcat data/q1_data.tsv.gz | awk 'NR==1||/ENSG/'  | python question1.py data/to_select.tsv  > outputs/q1.tsv
```

## Q2: Plotting a group of lines ( R + Linux Command)
Rscript will plot the lines based on the different clusters
It will read the data form stdin and plot by using ggplot
```
cat data/q2_data.tsv | Rscript question2.R "outputs/different_clusters.png" "Relative from center [bp]" "Enrichment over Mean" "MNase fragment profile" 
```

## Q3 Merge multiple files (R + Linux Command)
Code will read all the input files and perform the inner join based on the 1st column( we assume that 1st column will be the primary key to perform join)
Except for 1st column, other column names were random and 1st column name was set to "key" so that we could perform join on a key.
here we are performing inner join means output data will have the common keys value(intersection of all the files)
code requirement is that every file must have key as the 1st column.
```
Rscript join_list_of_files.R data/list_q3.tsv outputs/join_output.tsv
```

## Q4: Label with quantiles (Python)

python code will split the data based on the number of quantiles and assign the quantile with its range to each number in the input(first_hundred_numbers.tsv)
it wll get the quantile range with the help of qcut fromm pandas library
```
cat data/first_hundred_numbers.tsv | python group_in_quantiles.py 4 > outputs/question4.tsv
```

## Q5: Plotting big matrix (Linux + Gnuplot)
### download the big_data.tsv.gz
```
cd data
wget https://figshare.com/ndownloader/files/49000657?private_link=9f1324117c2f6e734f2b -O big_data.tsv.gz
cd ..
```
### get the matrix by removing 1st column as 1st column is id(string)
```
zcat data/big_data.tsv.gz | cut --complement -f1 > data/full_data.tsv
```

### install gnuplot 
```
sudo apt install gnuplot
```
### run the gnuplot script 
```
gnuplot -e "output='outputs/big_matrix.eps' ; input='data/full_data.tsv' "  gnuplot.gp
```

### install ghostscript to use ps2pdf 
```
sudo apt install ghostscript
```
### convert big_matrix.eps to pdf
```
ps2pdf outputs/big_matrix.eps outputs/big_matrix.pdf
```

In my case gnuplot is taking more memory so i have implemented this code with matplotlib as well
run the python code
```
python plot.py 'data/full_data.tsv'
```

