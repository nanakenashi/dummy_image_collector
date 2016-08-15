from urllib import request
from builder.placehold import Placehold


class Collector:

    # TODO: assign dynamically builder class
    def __init__(self, builder_name='placehold'):
        self.builder = Placehold

    def collect(self, opts, output_path):
        url = self.builder.build_url(opts)
        self.__save_content(url, output_path)

    def __save_content(self, url, output_path):
        with request.urlopen(url) as response:
            content = response.read()

            with open(output_path, 'wb') as file:
                file.write(content)
