#!/usr/bin/env python
#
# SQL weak-password checking for
# Project My Shodan (PMS) - |m|
#
# @_bike_maker_
import MySQLdb

class Brute:
    user = 'root'

    def __init__(self, host, password, port, timeout, success):
        self.host = host
        self.password = password
        self.port = port
        self.timeout = timeout
        self.success = success

    def check(self):
        try:
            db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, port=self.port, connect_timeout=self.timeout)
        except MySQLdb.Error, e:
            #print "[ERROR] [%d] - %s" % (e.args[0], e.args[1])
            return 0

        try:
            cursor = db.cursor()
            cursor.execute("SELECT VERSION()")
            results = cursor.fetchone()
            if results:
                return results
            else:
                return 0
        except MySQLdb.Error, e:
            #print "[ERROR] [%d] - %s\n" % (e.args[0], e.args[1])
            return 0

def testsql():
    print "Testing MySQL weak passwords."
    pwords = ['root', '']
    thost = '127.0.0.1'
    tport = 3306

    for pw in pwords:
        dcon = Brute(thost, pw, tport, 15, 0)
        test = dcon.check()
        if test:
            if pw:
                print "Success! User root has password: %s" % pw
                print "MySQL Version is: %s" % test
                success = 1
                break
            else:
                print "Success! User root has NULL password!"
                print "MySQL Version is: %s" % test
                success = 1
                break
        else:
            success = 0
            continue

    if success:
        exit
    else:
        print "Failed to find open password. Exiting."
        exit

if __name__=="__main__":
    testsql()
