"""
The application implementation.

"""

import time
import signal

from errors import TimeoutException
from errors import ServiceShutdownBySignal


class Application(object):
    """
    Service implementation that is wrapped as a daemon.

    """
    
    _name = None
    
    def __init__(self, config, logger):
        self._name = self.__class__.__name__
        self.config = config
        self.logger = logger
        self.logger.debug("Creating instance of %s ..." % self._name)

        # multiple signals may be used later for stop, stop-force, etc
        signal.signal(signal.SIGHUP, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
        signal.signal(signal.SIGALRM, self._signal_handler)

        self.logger.info("%s application initialised." % self._name)


    def start(self):
        """
        Serving entry point of the service.
        Some serve_forever / request loop is put here and
        blocks here.

        """
        self.logger.info("%s waiting for requests ... " % self._name)
        # TO BE IMPLEMENTED BY THE TARGET APPLICATION
        while True:
            time.sleep(0.5)
            1 + 1

    
    def shutdown(self):
        """
        Shutdown sequence of the service, e.g. threads stopping,
        cleaning up, etc.
        
        """
        self.logger.warn("Shutting down %s ..." % self._name)
        # TO BE IMPLEMENTED BY THE TARGET APPLICATION

            
    def _signal_handler(self, signum, frame):
        """
        SIGHUP - conditional shutdown e.g. do not shutdown the if there
        is some work currently in progress.
        SIGTERM - shut the application down regardless.

        """
        if signum == signal.SIGALRM:
            self.logger.warn("SIGALRM signal %s caught, raising "
                             "exception." % signum)
            raise TimeoutException("Timeout exception.")
        if signum == signal.SIGHUP:
            # SIGHUP: the service goes down conditionally ...
            condition = False
            self.logger.warn("SIGHUP signal %s caught, checking for ..." %
                              signum)
            # TO BE IMPLEMENTED BY THE TARGET APPLICATION
            if not contition:
                m = ("SIGHUP signal %s ... condition ... shutdown." % signum)
                raise ServiceShutdownBySignal(m)
            else:
                self.logger.warn("SIGHUP signal %s - work in progress, "
                                 "ignored." % signum)
        if signum == signal.SIGTERM:
            m = "SIGTERM signal %s caught, shutting down (forced) ..." % signum
            raise ServiceShutdownBySignal(m)
