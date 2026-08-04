# SQL_more_queries

This project covers more advanced MySQL topics: creating users, granting and
revoking privileges, using subqueries, and other more advanced SQL query
techniques.

## Requirements

- All scripts are run on Ubuntu 20.04 LTS with MySQL 8.0 (version 8.0.25).
- Every SQL file starts with a comment describing the task, and every SQL
  query is preceded by a comment.
- All SQL keywords are written in uppercase.

## Tasks

### 0. My privileges!

`0-privileges.sql` lists all the privileges of the MySQL users `user_0d_1`
and `user_0d_2` on `localhost`, using `SHOW GRANTS`.

Run it like this:

```
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
```

If `user_0d_2` does not exist yet, MySQL will raise an error for that part
of the script (`ERROR 1141 (42000)`), which is expected -- the script still
correctly reports the grants for `user_0d_1`.
