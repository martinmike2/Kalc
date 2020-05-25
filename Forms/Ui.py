from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    connection = None
    def __init__(self, krpc):
        self.krpc = krpc
        super(Ui, self).__init__()
        uic.loadUi('Forms/main.ui', self)

        self.connect_button = self.findChild(QtWidgets.QPushButton, 'btnKrpcConnect')
        self.connect_button.clicked.connect(self.krpc_connect)
        self.hohmann_button = self.findChild(QtWidgets.QPushButton, 'btnHohmannCalculate')
        self.hohmann_button.clicked.connect(self.calc_hohmann)
        self.show()

    def krpc_connect(self):
        if self.connection is None:
            self.connection = self.krpc.connect(
                self.findChild(QtWidgets.QLineEdit, "txtConnName").text(),
                self.findChild(QtWidgets.QLineEdit, 'txtConnHost').text(),
                int(self.findChild(QtWidgets.QLineEdit, 'txtConnRpc').text()),
                int(self.findChild(QtWidgets.QLineEdit, 'txtConnStream').text())
            )
            self.findChild(QtWidgets.QLabel, 'lblConnected').setText("YES")
            self.connect_button.setVisible(False)

    def calc_hohmann(self):
        from Maths.Orbits import OrbitMaths
        omath = OrbitMaths(self.connection)
        from Structs.Orbit import Orbit
        parking = Orbit(
            self.connection.space_center.active_vessel.orbit.periapsis,
            self.connection.space_center.active_vessel.orbit.apoapsis
        )
        r = self.connection.space_center.active_vessel.orbit.body.equatorial_radius
        target = Orbit(
            int(self.findChild(QtWidgets.QLineEdit, 'txtTargetPE').text()) + r,
            int(self.findChild(QtWidgets.QLineEdit, 'txtTargetAP').text()) + r
        )

        burns = omath.hohmann(parking, target)

        self.findChild(QtWidgets.QLabel, 'lblInjectionPrograde').setText(str(burns[0].prograde))
        self.findChild(QtWidgets.QLabel, 'lblInjectionNormal').setText(str(burns[0].normal))
        self.findChild(QtWidgets.QLabel, 'lblInjectionRadial').setText(str(burns[0].radial))

        self.findChild(QtWidgets.QLabel, 'lblCircPrograde').setText(str(burns[1].prograde))
        self.findChild(QtWidgets.QLabel, 'lblCircNormal').setText(str(burns[1].normal))
        self.findChild(QtWidgets.QLabel, 'lblCircRadial').setText(str(burns[1].radial))

