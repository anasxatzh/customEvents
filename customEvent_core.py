
# MAIN EVENT
class CustomEvent(Event):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __deref__(self) -> "adsk::core::CustomEvent *":
        return _core.CustomEvent___deref__(self)

    def __eq__(self, rhs: "CustomEvent") -> "bool":

        if not isinstance(self, type(rhs)) :
           return False
      
        return _core.CustomEvent___eq__(self, rhs)


    def __ne__(self, 
               rhs: "CustomEvent"
              ) -> "bool":

        if not isinstance(self, type(rhs)):
           return True

        return _core.CustomEvent___ne__(self, rhs)


    @staticmethod
    def classType() -> "char const *":
        return _core.CustomEvent_classType()

    
    
    def add(self, 
            handler: "CustomEventHandler"
           ) -> "bool":

        return _core.CustomEvent_add(self, handler)

    def remove(self, 
               handler: "CustomEventHandler"
              ) -> "bool":

        return _core.CustomEvent_remove(self, handler)

    def _get_eventId(self) -> "std::string":

        return _core.CustomEvent__get_eventId(self)

    def _get_name(self) -> "std::string":

        return _core.CustomEvent__get_name(self)

    def _get_sender(self) -> "adsk::core::Ptr< adsk::core::Base >":

        return _core.CustomEvent__get_sender(self)

    def _get_objectType(self) -> "char const *":
        return _core.CustomEvent__get_objectType(self)

    def _get_isValid(self) -> "bool":
        return _core.CustomEvent__get_isValid(self)

_core.CustomEvent_swigregister(CustomEvent)

def CustomEvent_classType() -> "char const *":
    return _core.CustomEvent_classType()


CustomEvent.eventId = property(CustomEvent._get_eventId, doc="id")


CustomEvent.cast = lambda arg: arg if isinstance(arg, CustomEvent) else None





# INPUT ARGS

class CustomEventArgs(EventArgs):

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __deref__(self) -> "adsk::core::CustomEventArgs *":
        return _core.CustomEventArgs___deref__(self)

    def __eq__(self, 
               rhs: "CustomEventArgs"
              ) -> "bool":

        if not isinstance(self, type(rhs)) :
           return False


        return _core.CustomEventArgs___eq__(self, rhs)


    def __ne__(self, rhs: "CustomEventArgs") -> "bool":

        if not isinstance(self, type(rhs)):
           return True


        return _core.CustomEventArgs___ne__(self, rhs)


    
    
    @staticmethod
    def classType() -> "char const *":
        return _core.CustomEventArgs_classType()
    __swig_destroy__ = _core.delete_CustomEventArgs

    def _get_additionalInfo(self) -> "std::string":

        return _core.CustomEventArgs__get_additionalInfo(self)

    def _get_firingEvent(self) -> "adsk::core::Ptr< adsk::core::Event >":
        return _core.CustomEventArgs__get_firingEvent(self)

    def _get_objectType(self) -> "char const *":
        return _core.CustomEventArgs__get_objectType(self)

    def _get_isValid(self) -> "bool":
        return _core.CustomEventArgs__get_isValid(self)


_core.CustomEventArgs_swigregister(CustomEventArgs)

def CustomEventArgs_classType() -> "char const *":
    return _core.CustomEventArgs_classType()


CustomEventArgs.additionalInfo = property(CustomEventArgs._get_additionalInfo, doc="addInInfo


CustomEventArgs.cast = lambda arg: arg if isinstance(arg, CustomEventArgs) else None




# HANDLER

class CustomEventHandler(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="T")
    __repr__ = _swig_repr

    def notify(self, 
               eventArgs: "CustomEventArgs"
              ) -> "void":
        return _core.CustomEventHandler_notify(self, eventArgs)

    def __init__(self):
        if self.__class__ == CustomEventHandler:
            _self = None
        else:
            _self = self
        _core.CustomEventHandler_swiginit(self, 
                                          _core.new_CustomEventHandler(_self, )
                                         )
    __swig_destroy__ = _core.delete_CustomEventHandler
    def __disown__(self):
        self.this.disown()
        _core.disown_CustomEventHandler(self)
        return weakref.proxy(self)

_core.CustomEventHandler_swigregister(CustomEventHandler)


CustomEventHandler.cast = lambda arg: arg if isinstance(arg, CustomEventHandler) else None
