"""Classroom model.
A Classroom is the central entity of the application. Any user can create a classroom and start inviting other users.
A Classroom has:
    - a name
    - an owner
    - members
    - modules

Modules organize the Classroom educational content such as resources and assessments
"""
from enum import Enum
from course_plat.exceptions import OwnershipError

class Classroom:
    def __init__(self, name, owner_id):
        self.name = name
        self.owner = Member(owner_id, Role.OWNER)
        self.members = Members() 
        self.modules = Modules()

        self.members.add(self.owner)

    def transfer_ownership(self, new_owner):
        if not self.members.contains(new_owner):
            raise OwnershipError("New owner must be a classroom member")
        if new_owner is self.owner:
            raise OwnershipError("This member is already the owner")
        if new_owner.role != Role.TEACHER:
            raise OwnershipError("Only teachers can become owners.")
        old_owner = self.owner

        old_owner.role = Role.TEACHER
        new_owner.role = Role.OWNER

        self.owner = new_owner

#Members
class Member:
"""Manage the role of a user"""
    def __init__(self, user_id, role):
        self.user_id = user_id
        self.role = role

class Members:
"""Contains a dictionary with members"""
    def __init__(self):
        self._members = {}

    @property
    def members(self):
        return tuple(self._members.keys())

    def add(self, member):
        self._members.update({member.user_id: member})

    def remove(self, member):
        if member.role == Role.OWNER:
            raise OwnershipError("The owner cannot be removed")
        del self._members[member.user_id]

    def with_role(self, role):
        return tuple(
                member
                for member in self._members.items()
                if member.role == role
        )

    def contains(self, member):
        return member.user_id in members._members

#Roles
class Role(Enum):
    OWNER = "owner"
    TEACHER = "teacher"
    STUDENT = "student"

#Modules
class Module:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.resources = Resources 
        self.assesments = Assessments
        """content is a resource or an assessment"""

    def add(self, content):
        # import content and use Resources, Assessments
        self.content.append(content)

class Modules:
    def __init__(self):
        self._modules = [] 

    @property
    def modules(self):
        return tuple(self._modules)

    def create(self, name, description):
        module = Module(name, description)
        self._modules.append(module)

    def remove(self, module):
        self._modules.remove(module)
