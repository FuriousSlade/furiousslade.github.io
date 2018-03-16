Title:Crontab bad hour error

Date:2018-03-07

Modified:2018-03-16

Category:笔记

Tags: crontab


```
crontab -e
```
```
# bug
*/10 23-06 * * * echo hello

# right
*/10 23,00-06 * * * echo hello
```
