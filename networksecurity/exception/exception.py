import sys
import logging
from networksecurity.logging import logger


class NetworkSecurityException(Exception):
	def __init__(self, error_message, error_details=None):
		super().__init__(error_message)
		self.error_message = error_message
		self.error_details = error_details

		# Accept either sys.exc_info() tuples or objects exposing exc_info.
		if error_details is None:
			exc_tb = sys.exc_info()[2]
		elif hasattr(error_details, "exc_info"):
			exc_tb = error_details.exc_info()[2]
		elif isinstance(error_details, tuple) and len(error_details) == 3:
			exc_tb = error_details[2]
		else:
			exc_tb = sys.exc_info()[2]

		self.lineno = exc_tb.tb_lineno if exc_tb else None
		self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else None

	def __str__(self):
		return f"Error occured in python script name [{self.file_name}] line number [{self.lineno}] error message [{str(self.error_message)}]"

