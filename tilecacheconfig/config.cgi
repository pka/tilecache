#!/usr/bin/python

from web_request.handlers import cgi 

from tilecacheconfig.Server import run

def run_app(*args, **kwargs):
    return run("/home/user/tilecache/tilecache.cfg", additional_metadata=['title', 'description', 'date'], *args, **kwargs) 

if __name__ == "__main__":
   cgi(run_app) 
