import sys

import ptsl
from ptsl import open_engine, CommandError
# from ptsl.PTSL_pb2 import PT_NoOpenedSession
# import ptsl.PTSL_pb2 as pt

with open_engine(application_name=sys.argv[0],
                 company_name=ptsl.__name__) as engine:

    pass
    
    
    

