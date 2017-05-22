#!/bin/sh
#
# Start/stop daemon script for Red Hat/CentOS based systems.
#
# /etc/init.d/<app daemon name> - Start/stop the service
#
# The following two lines allow this script to be managed by the
# chkconfig program.
#
# chkconfig: - 80 30
# description: <add service desctiption>


# configuration
SERVICENAME=<addservicename> # e.g. fdtd
SERVICEUSER=<addusername> # account under which service runs
SERVICECONFIG=<addconfigfilepath> # e.g. /etc/sysconfig/serviced
PIDFILE=<addpidfilepath> # e.g. /var/run/serviced/serviced.pid
SERVICEBIN=<addservicebinpath> # e.g. /usr/bin/serviced
SERVICEOPTIONS=<addargumentstoservicebinfile>



# Source function library.
. /etc/rc.d/init.d/functions

if [ -e $SERVICECONFIG ] ; then
    . $SERVICECONFIG
fi

start() {
    echo -n "Starting the service: "
    daemon --user $SERVICEUSER --pid_file $PIDFILE $SERVICEBIN $SERVICEOPTIONS
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && touch /var/lock/subsys/$SERVICENAME
}

# A function to stop a program, conditional kill (SIGHUP: signal 1)
stop() {
    echo -n "Shutting down the service (conditional, check log): "
    killproc -p $PIDFILE $SERVICENAME -1
    RETVAL=$?
    rm -f /var/lock/subsys/$SERVICENAME
    return $RETVAL
}

# A function to stop a program, forced shutdown (SIGTERM: signal 15)
stopforce() {
    echo -n "Shutting down the service (forced): "
    killproc -p $PIDFILE $SERVICENAME -15
    RETVAL=$?
    echo
    rm -f /var/lock/subsys/$SERVICENAME
    return $RETVAL
}

restart() {
    stop
    start
    return $RETVAL
}

case $1 in 
'start')
    start
    ;;
'stop')
    stop
    ;;
'stopforce')
	stopforce
	;;
'status')
    status -p $PIDFILE $SERVICENAME
    ;;
'reload' | 'restart')
    restart
    ;;
'condrestart')
    [ -f /var/lock/subsys/$SERVICENAME ] && restart
    ;;

*)
    echo "usage: $0 {start|stop|stopforce|status|restart|condrestart}"
    ;;
esac

exit $?
