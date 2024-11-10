#cat data/first_hundred_numbers.tsv | python group_in_quantiles.py 4 > outputs/question4.tsv
import sys
import pandas as pd

numbers = [int(line.strip()) for line in sys.stdin]
#print(numbers)
num_quantiles = int(sys.argv[1])

quantiles, bins = pd.qcut(numbers, num_quantiles, labels=[f'q{i+1}' for i in range(num_quantiles)], retbins=True)

#print(quantiles,bins)
#print(quantiles.categories)
for number, quantile in zip(numbers, quantiles):
    # bin interval
    bin_start = bins[quantiles.categories.get_loc(quantile)]
    bin_end = bins[quantiles.categories.get_loc(quantile) + 1]
    print(f'{number}\t{quantile}\t{quantile} ({bin_start}, {bin_end}]')


