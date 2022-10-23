class Point:
    """A distance from a relative origin (0, 0).
    The responsibility of Point is to hold and provide information about itself. Point has a few 
    convenience methods for adding, scaling, and comparing them.
    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.
    """
    
    def __init__(self, x, y):
        """Constructs a new Point using the specified x and y values.
        
        Args:
            x (int): The specified x value.
            y (int): The specified y value.
        """
        self._x = x
        self._y = y

    def add(self, other):
        """Gets a new point that is the sum of this and the given one.
        Args:
            other (Point): The Point to add.
        Returns:
            Point: A new Point that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        """Whether or not this Point is equal to the given one.
        Args:
            other (Point): The Point to compare.
        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        colission = False
        if (abs(self._x - other.get_x()) < 20) and (abs(self._y - other.get_y()) < 20):
            colission = True
        return colission

    def get_x(self):
        """Gets the horizontal distance.
        
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.
        
        Returns:
            integer: The vertical distance.
        """
        return self._y