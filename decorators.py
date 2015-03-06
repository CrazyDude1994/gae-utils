def html(file_name):
    def html_decorator(func):
        def func_wrapper(*args, **kwargs):
            self = args[0]
            with open(file_name, 'r') as f:
                text = f.read()
                self.response.write(text)
            func(*args, **kwargs)
        return func_wrapper
    return html_decorator