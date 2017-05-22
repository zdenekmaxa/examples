class ServiceShutdownBySignal(Exception):
    """
    Exception-based signal to terminate the service daemon.
    
    """
    pass


class TimeoutException(Exception):
    """
    SIGALARM was sent to the process, interrupt current action.
    
    """
    pass
