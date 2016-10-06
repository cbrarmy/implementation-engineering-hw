select u.id,u.username,u.email
from users as u left join user_actions as ua on u.id=ua.user_id
where ua.user_id is null
