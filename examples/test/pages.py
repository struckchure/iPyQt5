from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot, QPoint, QUrl
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QSizePolicy, QHBoxLayout
from PyQt5.QtGui import QQuaternion, QVector3D
from PyQt5.Qt3DExtras import (
    QTorusMesh,
    QPhongMaterial,
    Qt3DWindow,
    QOrbitCameraController
)
from PyQt5.Qt3DCore import (
    QEntity,
    QTransform
)
from PyQt5.Qt3DRender import QMesh

from iPyQt5.base.viewsBase import ViewBase as Page
from iPyQt5.base.widgetsBase import Button, Label
from css import engine as CSS
import cv2
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
form = CSS.getClasses(
    objectName=['QLineEdit', 'QPushButton', 'QLabel'],
    classNames=[
        'bg-gray-800',
        'p-3',
        'text-white',
        'border-none',
    ]
)

pseduos = CSS.getPsuedoClasses(
    objectName=['QPushButton'],
    psuedoClass={
        'hover': [
            'bg-gray-700'
        ]
    }
)
form += pseduos


class Index(Page):

    def __init__(self, *args, **kwargs):
        super(Index, self).__init__(*args, **kwargs)

        self.setWindowTitle("iPyQt5 | Index")
        self.setStyleSheet(
            CSS.getClasses(
                objectName=self.OBJECT_TYPE,
                classNames=[
                    'bg-gray-900',
                    'border-none',
                    'p-0'
                ]
            )
        )

        FORM_WIDTH = 300

        self.pageTitle = Label('Welcome to iPyQt5')
        self.pageTitle.setMaximumSize(FORM_WIDTH, 60)
        self.pageTitle.setStyleSheet(form)
        self.addWidget(self.pageTitle)

        self.home_button = Button('Home')
        self.home_button.setStyleSheet(
            form + CSS.getPsuedoClasses(
                objectName=['QPushButton'],
                psuedoClass={
                    'hover': [
                        'text-9xl'
                    ]
                }
            )
        )
        self.home_button.setMaximumSize(FORM_WIDTH, 60)
        self.home_button.onClick(self.routeToHome)

        self.addWidget(self.home_button)

        self.button_to_3d = Button('3D Render')
        self.button_to_3d.setStyleSheet(
            form + CSS.getPsuedoClasses(
                objectName=['QPushButton'],
                psuedoClass={
                    'hover': [
                        'text-9xl'
                    ]
                }
            )
        )
        self.button_to_3d.setMaximumSize(FORM_WIDTH, 60)
        self.button_to_3d.onClick(self.routeToRender3D)

        self.addWidget(self.button_to_3d)

    def routeToHome(self):
        self.goToRoute('Home')

    def routeToRender3D(self):
        self.goToRoute('Render3D')

    def goToRoute(self, name):
        from routes import router

        router.goToRoute(name)


class Thread(QThread):

    changePixmap = pyqtSignal(list)

    def run(self):
        cap = cv2.VideoCapture(0)

        # handa.xml hand fingers up
        # handb.xml hand fingers left to right
        # hands.xml hand fingers left to right

        # cascade_file = str(CURRENT_DIR.joinpath('handa.xml')) # fingers up
        # cascade_file = str(CURRENT_DIR.joinpath('handb.xml')) # left to right
        cascade_file = str(CURRENT_DIR.joinpath('hands.xml')) # left to right

        hand_cascade = face = cv2.CascadeClassifier(cascade_file)

        while True:
            ret, frame =  cap.read()
            frame = cv2.flip(frame, 1)

            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

                hands = hand_cascade.detectMultiScale(
                    gray,
                    scaleFactor=1.2,
                    minNeighbors=5,
                    minSize=(30, 30)
                )

                for x, y, w, h in hands:
                    cv2.rectangle(
                        frame,
                        (x, y),
                        (x + w, y + h),
                        (255, 255, 0),
                        2
                    )

                self.changePixmap.emit([frame, len(hands), hands])


class Home(Page):

    def __init__(self, *args, **kwargs):
        super(Home, self).__init__(*args, **kwargs)

        self.setWindowTitle('Home')
        self.setStyleSheet(
            CSS.getClasses(
                objectName=self.OBJECT_TYPE,
                classNames=[
                    'bg-gray-900',
                    'p-10',
                    'border-none'
                ]
            )
        )

        self.top_nav_bar = QHBoxLayout()
        self.top_nav_bar.setContentsMargins(0, 0, 0, 0)
        self.addLayout(self.top_nav_bar)

        self.goToIndexButton = Button('<-')
        self.goToIndexButton.setMaximumWidth(200)
        self.goToIndexButton.setStyleSheet(form)
        self.goToIndexButton.onClick(self.routeToIndex)
        self.top_nav_bar.addWidget(self.goToIndexButton)

        self.recordButton = Button('Start Recording')
        self.recordButton.setStyleSheet(form)
        self.recordButton.onClick(self.startRecording)
        self.top_nav_bar.addWidget(self.recordButton)

        self.stopRecordButton = Button('Stop Recording')
        self.stopRecordButton.setStyleSheet(form)
        self.stopRecordButton.onClick(self.stopRecording)
        self.top_nav_bar.addWidget(self.stopRecordButton)

        self.pixmap_thread = Thread()
        self.pixmap_thread.changePixmap.connect(self.setImage)

        self.image = Label()
        self.image.setStyleSheet(form)
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setMaximumSize(2000, 700)
        self.image.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        self.addWidget(self.image)

        self.image_text = Label()
        self.image_text.setStyleSheet(form)
        self.image_text.setAlignment(Qt.AlignCenter)
        self.addWidget(self.image_text)

    @pyqtSlot(list)
    def setImage(self, image):
        hands = image[2]
        count = image[1]
        image = image[0]

        for x, y, _, _ in hands:
            self.updateCursorPos(x, y)

        self.image_text.setText(f'{count} object(s)')

        h, w, ch = image.shape
        bytesPerLine = ch * w
        convertToQtFormat = QImage(
            image.data,
            w,
            h,
            bytesPerLine,
            QImage.Format_RGB888
        )
        image = convertToQtFormat.scaled(
            self.image.width(),
            self.image.height(),
            Qt.KeepAspectRatio
        )

        self.image.setPixmap(QPixmap.fromImage(image))

    def updateCursorPos(self, x, y):
        # current_x_pos = self.cursor().pos().x()
        # current_y_pos = self.cursor().pos().y()

        # max_x_pos = 1366
        # max_y_pos = 768

        new_pos = QPoint(x, y)

        self.cursor().setPos(new_pos)

    def startRecording(self):
        self.pixmap_thread.start()

    def stopRecording(self):
        if self.pixmap_thread.isRunning():
            self.pixmap_thread.terminate()

    def routeToIndex(self):
        from routes import router

        router.goToRoute('Index')


class Render3D(Page):

    def __init__(self, *args, **kwargs):
        super(Render3D, self).__init__(*args, **kwargs)

        self.setWindowTitle('Home')
        self.setStyleSheet(
            CSS.getClasses(
                objectName=self.OBJECT_TYPE,
                classNames=[
                    'bg-gray-900',
                    'p-4',
                    'border-none'
                ]
            )
        )

        self.back_to_index = Button('<- Index')
        self.back_to_index.setStyleSheet(form)
        self.back_to_index.onClick(self.goToIndex)
        self.addWidget(self.back_to_index)

        self.createView()
        self.scene = self.createScene()
        self.createCamera()

    def goToIndex(self):
        self.goToRoute('Index')

    def goToRoute(self, name):
        from routes import router

        router.goToRoute(name)

    def createView(self):
        self.view = Qt3DWindow()

        self.container = self.createWindowContainer(self.view)
        self.container.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        self.container.setMaximumSize(1500, 1500)

        self.addWidget(self.container)

    def createScene(self):
        self.rootEntity = QEntity()
        self.material = QPhongMaterial(self.rootEntity)

        self.importMeshEntity = QEntity(self.rootEntity)
        self.importMesh = QMesh()
        self.importMesh.setSource(QUrl(str(CURRENT_DIR.joinpath('monkey.obj'))))

        self.importMeshTransform = QTransform()
        self.importMeshTransform.setScale3D(QVector3D(5, 5, 5))
        self.importMeshTransform.setRotation(
            QQuaternion.fromAxisAndAngle(
                QVector3D(1.0, 0.0, 0.0),
                120.0
            )
        )

        self.importMeshEntity.addComponent(self.importMesh)
        self.importMeshEntity.addComponent(self.importMeshTransform)
        # self.importMeshEntity.addComponent(self.material)

        # self.torusEntity = QEntity(self.rootEntity)
        # self.torusMesh = QTorusMesh()
        # self.torusMesh.setRadius(5)
        # self.torusMesh.setMinorRadius(3)
        # self.torusMesh.setRings(100)
        # self.torusMesh.setSlices(500)

        # self.torusTransform = QTransform()
        # self.torusTransform.setScale3D(QVector3D(1.5, 1.5, 1.5))
        # self.torusTransform.setRotation(
        #     QQuaternion.fromAxisAndAngle(
        #         QVector3D(1.0, 0.0, 0.0),
        #         120.0
        #     )
        # )

        # self.torusEntity.addComponent(self.torusMesh)
        # self.torusEntity.addComponent(self.torusTransform)
        # self.torusEntity.addComponent(self.material)

        return self.rootEntity

    def createCamera(self):
        # Camera.
        self.camera = self.view.camera()
        self.camera.lens().setPerspectiveProjection(
            45.0,
            16.0 / 9.0,
            0.1,
            1000.0
        )
        self.camera.setPosition(QVector3D(0.0, 0.0, 40.0))
        self.camera.setViewCenter(QVector3D(0.0, 0.0, 0.0))

        # For camera controls.
        self.camController = QOrbitCameraController(self.scene)
        self.camController.setLinearSpeed(50.0)
        self.camController.setLookSpeed(180.0)
        self.camController.setCamera(self.camera)

        self.view.setRootEntity(self.scene)

    def routeToIndex(self):
        from routes import router

        router.goToRoute('Index')
