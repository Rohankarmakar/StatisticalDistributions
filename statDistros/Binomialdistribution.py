import math
import matplotlib.pyplot as plt
from .GeneralDistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials
    
    
    TODO: Fill out all TODOs in the functions below
            
    """       
    
    def __init__(self, prob=.5, size=20):
        
        # TODO: store the probability of the distribution in an instance variable p
        self.p = prob
        # TODO: store the size of the distribution in an instance variable n
        self.n = size
        
        mean = self.calculate_mean()
        std = self.calculate_stdev()
        
        Distribution.__init__(self, mean, std)
    

    def calculate_mean(self):
    
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
                
        self.mean = self.n * self.p

        return self.mean


    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """

        self.stdev = math.sqrt(self.n * (1- self.p) * self.p)

        return self.stdev
        
        
        
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """        

        self.n = len(self.data)

        positive_trials = 0
        for i in self.data:
            if i > 0:
                positive_trials += 1

        self.p = positive_trials/self.n

        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n

        
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """

        plt.bar(self.data) 
        plt.title("Binomial Distribution")       
        plt.xlabel('Outcomes')
        plt.ylabel('Frequencies')
        plt.show()


    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        prob_of_k = (math.factorial(self.n)/(math.factorial(k) * math.factorial(self.n - k))) * pow(self.p, k) * pow(1 - self.p, self.n-k)

        return prob_of_k


    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
    
        x = self.data
        y = [self.pdf(k) for k in range(self.n + 1)]

        plt.bar(x, data = y, color='royalblue', alpha=0.7)
        plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
        plt.title('PDF of Binomial Distribution')
        plt.xlabel('Data')
        plt.ylabel('Probability')
        plt.show()

        return x, y

                
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
                
        result = Binomial(0.5, 1)
        result.p = self.p
        result.n = self.n + other.n
        result.mean = result.calculate_mean()
        result.stdev = result.calculate_stdev()

        return result
        
        
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial Distribution
        
        """
    
        return f'mean {self.mean}, standard deviation {self.stdev}, p {self.p}, n {self.n}'
