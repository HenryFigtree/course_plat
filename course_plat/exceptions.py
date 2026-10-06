class DomainError(Exception):
    """Base class for all domain exceptions"""
    pass

class ClassroomError(DomainError):
    """Base class for classroom related errors"""
    pass

class LinkError(DomainError):
    """Base class for link related errors"""
    pass


#---------------------------------------------------------


class InvalidUrlError(LinkError):
    """Raised when a url syntax is invalid"""
    pass

class OwnershipError(ClassroomError):
    """Raised when there are ownership errors like trying to delete an owner"""
    pass

class InvalidFileTypeError(Exception):
    pass

class CourseAlreadyExists(Exception):
    pass
