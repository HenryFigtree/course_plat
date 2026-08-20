## Member

## Responsibility
Assigns a user id with a specific `Role` in a classroom

# Members

## Responsibility
Manages the collection of members belonging to a classroom

## Methods
`add(self, member)`
`remove(self, member)`
`with_role(self, role)`
`contains(self, member)`

## Role

## Responsibility

Establishes the available roles that can be assigned to members

Enum:
- OWNER
- TEACHER
- STUDENT
