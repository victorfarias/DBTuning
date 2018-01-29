from DBTuning.MemSQL.api import MemSQLAdmin

def run():

    mem_admin = MemSQLAdmin()
    mem_admin.start()

def stop():
    mem_admin = MemSQLAdmin()
    mem_admin.stop()

if __name__ == "__main__":
    run()
    # stop


