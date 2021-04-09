from PyQt5 import QtWidgets, QtGui, QtCore


class RobotGraphicsItem(QtWidgets.QGraphicsPolygonItem):
    """
    The class RobotGraphicsItem extends QGraphicsPolygonItem to link it together to the physical
    representation of a Robot. The QGraphicsPolygonItem handles the drawing, while the
    Robot knows its own location and status.

    NOTE: unfortunately the PyQt5 uses different naming conventions than the rest
    of this project. We are also overriding the mousePressEvent()-method, whose
    name cannot be changed. Therefore, this class has a different style of naming the
    method names. (for example: updatePosition() vs update_position())
    """

    def __init__(self, robot, square_size):
        # Call init of the parent object
        super(RobotGraphicsItem, self).__init__()

        # Do other stuff
        self.robot = robot
        self.square_size = square_size
        brush = QtGui.QBrush(1) # 1 for even fill
        self.setBrush(brush)
        self.constructTriangleVertices()
        self.updateAll()


    def constructTriangleVertices(self):
        """
        This method sets the shape of this item into a triangle.

        The QGraphicsPolygonItem can be in the shape of any polygon.
        We use triangles to represent robots, as it makes it easy to
        show the current facing of the robot.
        """
        # Create a new QPolygon object
        triangle = QtGui.QPolygonF()

        # Add the corners of a triangle to the the polygon object
        triangle.append(QtCore.QPointF(self.square_size/2, 0)) # Tip
        triangle.append(QtCore.QPointF(0, self.square_size)) # Bottom-left
        triangle.append(QtCore.QPointF(self.square_size, self.square_size)) # Bottom-right
        triangle.append(QtCore.QPointF(self.square_size/2, 0)) # Tip

        # Set this newly created polygon as this Item's polygon.
        self.setPolygon(triangle)

        # Set the origin of transformations to the center of the triangle.
        # This makes it easier to rotate this Item.
        self.setTransformOriginPoint(self.square_size/2, self.square_size/2)


    def updateAll(self):
        """
        Updates the visual representation to correctly resemble the current
        location, direction and status of the parent robot.
        """
        self.updatePosition()
        self.updateRotation()
        self.updateColor()


    def updatePosition(self):
        """
        Implement me!

        Update the coordinates of this item to match the attached robot.
        Remember to take in to account the size of the squares.

        A robot in the first (0, 0) square should be drawn at (0, 0).

        See: For setting the position of this GraphicsItem, see
        QGraphicsPolygonItem at http://doc.qt.io/qt-5/qgraphicspolygonitem.html
        and its parent class QGraphicsItem at http://doc.qt.io/qt-5/qgraphicsitem.html

        For getting the location of the parent robot, look at the Robot-class
        in robot.py.
        """
        location = self.robot.get_location()
        self.setPos(location.get_x()*self.square_size, location.get_y()*self.square_size)


    def updateRotation(self):
        """
        Implement me!

        Rotates this item to match the rotation of parent robot.
        A method for rotating can be found from QGraphicsItem at http://doc.qt.io/qt-5/qgraphicsitem.html

        """
        facing = self.robot.get_facing()
        if facing == (0, -1):
            self.setRotation(0)
        elif facing == (0, 1):
            self.setRotation(180)
        elif facing == (1, 0):
            self.setRotation(90)
        elif facing == (-1, 0):
            self.setRotation(270)


    def updateColor(self):
        """
        Implement me!

        Draw broken robots in red, stuck robots in yellow and working robots in green.

        The rgb values of the colors must be the following:
        - red: (255, 0, 0)
        - yellow: (255, 255, 0)
        - green: (0, 255, 0)

        See: setBrush() at http://doc.qt.io/qt-5/qabstractgraphicsshapeitem.html
        and QBrush at http://doc.qt.io/qt-5/qbrush.html
        and QColor at http://doc.qt.io/qt-5/qcolor.html

        Look at robot.py for checking the status of the robot.
        """
        red_brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        yellow_brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        green_brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        if self.robot.is_broken():
            self.setBrush(red_brush)
        elif self.robot.is_stuck():
            self.setBrush(yellow_brush)
        else:
            self.setBrush(green_brush)



    def mousePressEvent(self, *args, **kwargs):
        """
        Implement me!

        If the clicked robot is broken, fix it.
        This function is called everytime this object is clicked on the scene.

        Hint: You don't need to do anything with the *args or **kwargs. One line solution should be sufficient.
        """
        self.robot.fix()
