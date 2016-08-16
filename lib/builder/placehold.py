# -*- coding: utf-8 -*-
import os


class Placehold:

    """ URL Builder class for 'https://placehold.jp'
    """

    ENDPOINT = 'https://placehold.jp'

    @classmethod
    def build_url(cls, opts):
        directory = cls.__directory(opts)
        file_name = cls.__file_name(opts)
        path = os.path.join(cls.ENDPOINT, directory, file_name)

        query_string = cls.__query_string(opts)

        return path + query_string

    @staticmethod
    def __directory(opts):
        parts = [
            opts.get('text_size', None),
            opts.get('bg_color', None),
            opts.get('text_color', None)
        ]
        necessary = [part for part in parts if part is not None]

        return '/'.join(necessary)

    @staticmethod
    def __file_name(opts):
        width = opts.get('width', 150)
        height = opts.get('height', 150)
        format = opts.get('format', 'png')

        return "%dx%d.%s" % (width, height, format)

    @staticmethod
    def __query_string(opts):
        text = opts.get('text', None)

        if text is not None:
            query_string = "?text=%s" % text
        else:
            query_string = ''

        return query_string
