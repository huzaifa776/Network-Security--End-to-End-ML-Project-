import sys
import logging
from networksecurity.logging import logger


class NetworkSecurityException(Exception):
	def __init__(self, error_message, error_details):
		self.error_message = error_message
		self.error_details = error_details
		exc_type, exc_value, exc_tb = error_details
		self.lineno = exc_tb.tb_lineno
		self.file_name = exc_tb.tb_frame.f_code.co_filename

	def __str__(self):
		return f"Error occured in python script name [{self.file_name}] line number [{self.lineno}] error message [{str(self.error_message)}]"

