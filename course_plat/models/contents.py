"""The different kinds of content a Module can contain are defined here.

This content can be:
    -Resourse:
        -Links to other websites
        -Files like presentations or articles
        -Sections written in markdown

    -Assessments
        -Online Questions
        -Upload Submission
"""
from course_plat.exceptions import InvalidUrlError
from enum import Enum
from urllib.parse import urlsplit

class Resources:
    def __init__(self):
        self._resources = []

    def add(self, resource):
        self._resources.append(resource)

    @property
    def resources(self):
        return tuple(self._resources)

    def remove(self, resource):
        self._resources.remove(resource)

class Link:
    def __init__(self, text, url):
        self.text = text
        self.url = self._validate_url(url)

    def _validate_url(url):
        url_split = urlsplit(url)

        if url_split.scheme not in ("http", "https"):
            raise InvalidUrlError("Only http or https links are allowed")

        if not url_split.netloc:
            raise InvalidUrlError("URL must contain a host")

class File:
    def __init__(self, filename, path):
        self.filename = filename
        self.path = path

class Section:
    def __init__(self, title=None, body=None):
        self._title = "" 
        self._body = ""

        if body:
            self.add_body(body)
        if title:
            self.add_title(title)

    @property
    def title(self):
        a = self._title
        return a

    @property
    def body(self):
        a = self._body
        return a

    def add_body(self, body):
        self._body += body

    def add_title(self, title):
        self._title += title

    def edit_title(self, new_title):
        self._title = new_title

    def edit_body(self, new_body):
        self._body = new_body


#-------------+
# Assessments |
#-------------+

class Assessments:
    def __init__(self):
        self._assessments = []

    @property
    def assessments(self):
        return tuple(self._assessments)

    def add(self, assessment):
        self._assessments.append(assessment)

    def remove(self, assessment):
        self._assessments.remove(assessment)

class OnlineAssessment:
    def __init__(self):
        self._questions = []

    @property
    def questions(self):
        return tuple(self._questions)

    def add(self, question):
        self._questions.append(question)

    def remove(self, question):
        self._questions.remove(question)



