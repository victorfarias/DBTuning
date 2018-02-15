import os

from DBTuning.MemSQL.api import MemSQLAdmin
from DBTuning.OLTPBenchmark.api import OLTPBenchmark


def run():

    mem_admin = MemSQLAdmin()
    oltp = OLTPBenchmark()

    # oltp.load("wikipedia", os.path.abspath("./DBTuning/OLTPBenchmark/config/memsql_wikipedia_config.xml"))
    
    # print mem_admin.set_param("lock_wait_timeout", "60")    
    # print mem_admin.set_param("load_data_read_size", "1000")    
    # oltp.run("wikipedia", os.path.abspath("./DBTuning/OLTPBenchmark/config/memsql_wikipedia_config.xml"))    
    # print mem_admin.set_param("load_data_read_size", "100")
    # oltp.run("wikipedia", os.path.abspath("./DBTuning/OLTPBenchmark/config/memsql_wikipedia_config.xml"))    

    # print oltp.load("tpcc", os.path.abspath("/home/victor/DBTuning/DBTuning/OLTPBenchmark/config/memsql_tpcc_config.xml"))        

    # print mem_admin.set_param("load_data_read_size", "25600")        
    print oltp.run("tpcc", os.path.abspath("/home/victor/DBTuning/DBTuning/OLTPBenchmark/config/memsql_tpcc_config.xml"))        

def restart():
    mem_admin = MemSQLAdmin()
    print mem_admin.set_param("query_parallelism", "8000")    
    # print mem_admin.set_param("transaction_buffer", "100000000")    
    print mem_admin.set_param("load_data_read_size", "10000000")            
    print mem_admin.set_param("load_data_write_size", "8000")                
    print mem_admin.set_param("multi_insert_tuple_count", "400000")  
    print mem_admin.set_param("max_prepared_stmt_count", "1000000")  
    print mem_admin.set_param("plan_expiration_minutes", "2000")  
        
    mem_admin.stop()
    mem_admin.start()

def load():
    oltp = OLTPBenchmark()    
    print oltp.load("tpcc", os.path.abspath("/home/victor/DBTuning/DBTuning/OLTPBenchmark/config/memsql_tpcc_config.xml"))        

def stop():
    mem_admin = MemSQLAdmin()
    mem_admin.stop()  
    

if __name__ == "__main__":
    # stop()
    # load()
    # restart()
    run() 
