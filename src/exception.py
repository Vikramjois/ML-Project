import sys

def error_message_detail(error,error_detail:sys):
    #exc_tb will provide info like on which file and line the exception has occured
    #exc_info will provide 3 imp info and first 2 info is not imp and only interested in last info
    _,_,exc_tb=error_detail.exc_info() 
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message
    
class customException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)    
        self.error_message=error_message_detail(error_message,error_detail = error_detail)

    def __str__(self):
        return self.error_message    

