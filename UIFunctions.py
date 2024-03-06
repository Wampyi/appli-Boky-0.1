from main import*


class UIFunctions(MainWindow):
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # set ui
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 0

            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # animation
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

