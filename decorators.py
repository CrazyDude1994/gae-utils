def html(file_name):
	"""Loads and outputs file directrly to response stream

	Args:
		file_name (str): File's filename to read

	Returns:
		func: Decorated function

	Raises:
		IOError: If file does not exist
	"""
    def html_decorator(func):
        def func_wrapper(*args, **kwargs):
            self = args[0]
            with open(file_name, 'r') as f:
                text = f.read()
                self.response.write(text)
            func(*args, **kwargs)
        return func_wrapper
    return html_decorator