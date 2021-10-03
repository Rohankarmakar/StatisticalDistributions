# **statDistros**

statDistros is a Python library for dealing with various statistical distributions. Now it provides various statistical calculations for Gaussian and Binomial Distributions only. Users can also plot Probability Density Functions with it.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install statDistros
```

## Usage

```python
import statDistros

# returns a Gaussian Distribution Object
*Gaussian class takes two positional arguements - mean, standard deviation of the distribution*
gaussian_1 = statDistros.Gaussian(25, 4)

# read data
gaussian_1.read_data_file(filename)
*reads data from a text file containing a data in each line*

#calculate mean and S.D of the new data
gaussian_1.calculate_mean()
gaussian_1.calculate_stdev(sample=False) #if the data is a sample or not
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
