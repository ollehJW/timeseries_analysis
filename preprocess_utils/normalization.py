from sklearn.preprocessing import MinMaxScaler, StandardScaler

class Normalize(object):

    """
    Data Nomalization Module
    method: (min-max, z-norm)
    Your input should contain only numeric type variables.
    """

    def __init__(self, data, numeric_variable, method = 'min-max'):
        self.data = data
        self.numeric_variable = numeric_variable
        self.method = method
        if self.method == 'min-max':
            self.data[self.numeric_variable] = self.min_max_norm()
        elif self.method == 'z-norm':
            self.data[self.numeric_variable] = self.z_norm()
        else:
            raise Exception("Choose normalization method in [min-max, z-norm]")

    def min_max_norm(self):
        scaler = MinMaxScaler()
        normed_data = scaler.fit_transform(self.data[self.numeric_variable])
        return normed_data
    
    def z_norm(self):
        scaler = StandardScaler()
        normed_data = scaler.fit_transform(self.data[self.numeric_variable])
        return normed_data