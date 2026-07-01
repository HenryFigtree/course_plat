# Refactor around classrooms

## Summary

WIP this refactor changes the application from course centered template to a classroom centered learning platform.

The initial project served as a template and proof of concept. This refactor marks the transition to a complete web application, introducing a domain model centered around classrooms, teachers, modules, resources and assessments.

## Database

- Added `classrooms` as the central entity
- Added `classroom_members` with support for different roles
- Refactored modules into organizational containers with unique positions
- Separated learning resources from assessments
- Assessments support multiple submission methods (upload methods is a wip, currently just online methods)

- Added support for different question types

## Architectural changes

- Simplified relationships and clarified responsibilities across the data model
- Established a foundation for future features

## Upcoming work

- Teacher classroom creation management
- Classroom member invites and roles
- Module creation and organization
- Resource creation and management
- Online assessment creation and management
