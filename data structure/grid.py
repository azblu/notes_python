from array import Array

class Grid(object):

    def __init__(self, rows, columns, fill_value = None):
        """Represent a two-dimensional array"""
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)
    
    def get_number_rows(self):
        """Return the number of rows"""
        return len(self.data)

    def get_number_columns(self):
        """Return the number of columns"""
        return len(self.data[0])
    
    def __getitem__(self, index, col):
        """[row][cols]"""
        return self.data[index][col]

    def __setitem__(self, index, col, value):
        self.data[index][col] = value

    def __str__(self):
        """Returns a string representation of the grid"""
        result = ''
        for row in range(self.get_number_rows()):
            for col in range(self.get_number_columns()):
                result = f'{result} {self.data[row][col]}'
            result = f'{result} \n'
        return str(result)
