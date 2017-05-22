#!/usr/bin/env python

"""
__author__ = Zdenek Maxa

Daemon wrapper implementation.
    input arguments: log_file pid_file (turns into conf.log_file,
                                        conf.pid_file)

Logger class is not provided.
Configuration class is not provided.

"""


import os
import sys

from errors import ServiceShutdownBySignal
        


def daemonize(config, logger):
    """
    Store PID of the current process into pid_file file name and fork the
    daemon process.
    Daemonization recipe compiled from several sources, compared with
    a number of recipes available on the internet.
    
    """ 
    logger.info("Preparing for daemonization (parent process "
                "PID: %s) ..." % os.getpid())
    
    # check that there is a log defined, otherwise fail - need to
    # redirect stdout, stderr stream into this file
    if not logger.logFile:
        logger.fatal("No log file defined, necessary when running as "
                     "daemon, exit.")
        logger.close()
        sys.exit(1)
    # check if there is pid_file defined - necessary in daemon mode
    if not conf.get("pid_file"):
        logger.fatal("No PID file defined, necessary when running as "
                     "daemon, exit.")
        logger.close()
        sys.exit(1)
    
    pid_file = conf.get("pid_file")
    # try opening the file for append - if exists - fail: service might be
    # running or the file was left behind
    if os.path.isfile(pid_file):
        logger.fatal("File '%s' exists, can't start, remove it "
                     "first." % pid_file)
        logger.close()
        sys.exit(1)
        
    # check if the pid_file is writeable
    try:
        pid_file_desc = open(pid_file, 'w')
        pid_file_desc.close()
    except IOError, ex:
        logger.fatal("Can't access PID file '%s', reason: %s" % 
                     (pid_file, ex))
        logger.close()
        sys.exit(1)
    
    # daemonization forking ...
    if os.fork() != 0:
        # exit parent code
        sys.exit(0)
    
    # decouple from parent environment
    os.chdir("/")
    os.setsid()
    os.umask(0)
    # don't change current working directory (os.chdir("/"))

    # fork again so we are not a session leader
    if os.fork() != 0:
        sys.exit(0)

    # output streams redirection into the log file
    logger.debug("The process is daemonized, redirecting stdout, stderr, "
                 "stdin descriptors ...")
    for f in sys.stdout, sys.stderr:
         f.flush()
    log_file = file(logger.log_file, "a+", 0)  # buffering - 0 (False)
    dev_null = file("/dev/null", 'r')
    os.dup2(log_file.fileno(), sys.stdout.fileno())
    os.dup2(log_file.fileno(), sys.stderr.fileno())
    os.dup2(dev_null.fileno(), sys.stdin.fileno())
    
    logger.debug("Redirecting streams is over.")
    
    # finally - the daemon process code, first store it's PID into file
    pid = os.getpid()
    logger.info("Running as daemon process: PID: %s (forked), PID "
                "file: '%s'" % (pid, pid_file))
    pid_file_desc = open(pid_file, 'w')
    pid_file_desc.write(str(pid))
    pid_file_desc.close()
    
    logger.debug("Daemonization finished.")
    


def start_application(config, logger):
    """
    Takes care of runnign the Application.
    Regardless of whether this function is run interactively from the
    command line or running as a background daemon process.

    """
    service = None
    try:
        try:
            service = Application(config, logger)
            service.start()
        except KeyboardInterrupt:
            logger.fatal("Interrupted from keyboard ...")
        except ServiceShutdownBySignal, ex:
            logger.fatal(ex)
        except Exception as ex:
            logger.fatal("Exception was caught ('%s'), reason: %s"
                          % (ex.__class__.__name__, ex), traceback=True)
    finally:
        if service:
            try:
                service.shutdown()
            except Exception as exx:
                logger.fatal("Exception occurred during shutdown sequence, "
                             "reason: %s" % exx, traceback=True)
        try:
            # if daemonize, pid_file should have been created, delete it
            # now when shutting down
            if config.get("daemonize"):
                pid_file = config.get("pid_file")
                logger.info("Deleting the PID file '%s' ... " % pid_file)
                try:
                    os.remove(pid_file)
                    logger.debug("File '%s' removed." % pid_file)
                except OSError, ex:
                    logger.error("Could not remove PID file '%s', "
                                 "reason: %s" % (pid_file, ex))
        except Exception as exx:
            logger.fatal("Exception occurred during shutdown-cleanup, "
                         "reason: %s" % exx, traceback=True)                
        logger.close()


def main():
    # config
    # process configuration values (from a config file) and command line
    # arguments which modify config file returns config instance.

    # logger, create logger class instance

    # check 'daemonize' command line argument, otherwise runs on foreground
    if conf.get("daemonize"):
        daemonize(config, logger)
    else:
        logger.info("Starting the service on foreground ...")
        
    start_application(config, logger)
        

if __name__ == "__main__":
    main()
