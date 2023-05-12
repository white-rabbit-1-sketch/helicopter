import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pydispatch import dispatcher

from game.Event.PreLoadService import PreLoadService
from game.Service.System.ParameterService import ParameterService
from game.Service.System.Engine import Engine
from game.Service.System.ServiceLoader import ServiceLoader

PARAMETERS_FILE_PATH = "parameters.ini"

def main():
    serviceLoader = ServiceLoader(ParameterService(PARAMETERS_FILE_PATH))
    serviceLoader.loadRenderer()
    serviceLoader.openGLRenderer.renderBlackScreen("Loading...")

    def onPreLoadService(sender, **kwargs) -> None:
        data = kwargs.get('data', {})
        event: PreLoadService = data.get('event')

        serviceLoader.openGLRenderer.renderBlackScreen("Loading: [%s]" % event.name)

    dispatcher.connect(onPreLoadService, signal=PreLoadService.NAME)

    serviceLoader.loadCommon()

    engine = Engine(
        serviceLoader.parameterService,
        serviceLoader.openGLRenderer,
        serviceLoader.keyboardControllerService,
        serviceLoader.mainSceneGenerator,
        serviceLoader.mapLayerService
    )
    engine.run()

if __name__ == '__main__':
    main()


