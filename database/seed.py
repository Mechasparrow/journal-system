from database.database import db_session
from database.models import Post

# Delete current
db_session.query(Post).delete()

# Seeding code


# End db code
db_session.remove()
