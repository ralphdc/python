#!/usr/bin/env python3

from . import Base
from config import Config
import os
import re

class University(Base):

    def __init__(self):
        super(University, self).__init__()

        self.config_file = Config.UNIVERSITY_FILE or None

        if not os.path.isfile(self.config_file):
            raise Exception("[Error] %s is not found!" % self.config_file)


        self.pattern = '/li/'

    def run(self):

        with open(self.config_file, mode='r', encoding='UTF-8') as f:
            for line in f:
                print(re.search('<li(.*?)</li>', line))