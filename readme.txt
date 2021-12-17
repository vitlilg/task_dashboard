TODO task dashboard API v1

User's section:
Create user (allow for any users):
POST /api/v1/tasks/user/create/
List of users (allow for authenticated users):
GET /api/v1/tasks/user/list/
Update/delete user (allow for admin users with token)
GET, PUT, DELETE /api/v1/tasks/user/detail/<id>/

Task's section:
Create task (allow for authenticated users):
POST /api/v1/tasks/tasks/task/create/
List of tasks (allow for authenticated users):
GET /api/v1/tasks/task/list/
Read task (allow for authenticated users) and update/delete task (allow for author of task)
GET, PUT, DELETE /api/v1/tasks/task/detail/<id>/

Group's section:
Create group (allow for admin users):
POST /api/v1/tasks/user_group/create/
List of groups (allow for admin users):
GET /api/v1/tasks/user_group/list/
Update/delete group (allow for admin users with token):
GET, PUT, DELETE /api/v1/tasks/user_group/detail/<id>/

Token's section:
Create user token:
POST /api/v1/auth_token/token/login/
Delete user token:
POST /api/v1/auth_token/token/logout/

