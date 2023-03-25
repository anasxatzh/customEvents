from . import commands
from .lib import fusion360utils as futil
import threading
import adsk.core, adsk.fusion, traceback


local_handlers = []

stopFlag, customEvent = None, None
eventId_ = "startupId"

app = adsk.core.Application.get()
ui = app.userInterface




class MyThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        global ui, app
        onStartupCompleted = StartupCompletedHandler() # onStartupCompleted --> ApplicationEventHandler
        app.startupCompleted.add(onStartupCompleted) # app.startupCompleted --> ApplicationEvent
        local_handlers.append(onStartupCompleted)
        isInitialized = app._get_isStartupComplete()
        app.fireCustomEvent(eventId_, str(isInitialized))





class ThreadEventHandler(adsk.core.CustomEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        try:
            global ui, app
            if ui.activeCommand != 'SelectCommand':
                ui.commandDefinitions.itemById('SelectCommand').execute()

            isInitialized = args._get_additionalInfo()
            ui.messageBox(str(isInitialized))
            if isInitialized == "True":pass
            else:stop(ui)
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))







class StartupCompletedHandler(adsk.core.ApplicationEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        global ui
        try:
           ui.messageBox("Startup completed")
        #    run(ui)
        #    ui.messageBox(str(args._get_firingEvent()._get_name()))
           global local_handlers
           if len(local_handlers) > 0 : del local_handlers[-1]

        except:
            ui.messageBox("NOT COMPLETED")
            app.log('Startup completed event failed: {}'.format(traceback.format_exc()))




def run(context):
    try:
        # This will run the start function in each of your commands as defined in commands/__init__.py
        commands.start()

  
        global customEvent, eventId_, stopFlag, app, ui
    
        customEvent = app.registerCustomEvent(eventId_)
        onThreadEvent = ThreadEventHandler()
        customEvent.add(onThreadEvent)
        local_handlers.append(onThreadEvent)

        stopFlag = threading.Event()
        myThread = MyThread(stopFlag)
        myThread.start()

    except:
        futil.handle_error('run')


        
        
