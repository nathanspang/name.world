class User(db.model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.column(db.Text)
    username = db.Column(db.Text)
    about_me = db.Column(db.Text)


    messages = db.relationship('Message', backref='user', lazy='dynamic')

    def __init__(self, first_name, last_name, username, about_me):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.about_me = about_me

    def __repr__(self):
        return f'First Name: {self.first_name} Last Name: {self.last_name} Username: {self.username}'
    
    def num_posts(self):
        print(f'The User: {self.username} has sent {len(self.messages)} messages.')

class Message(db.model):

    __tablename__ = 'messages'
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    time_created = db.Column(db.DateTime)
    user_id = db.column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, body, time_created, user_id):
        self.title = title
        self.body = body
        self.time_created = time_created
        self.user_id = user_id

    
class Group(db.model):

    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    users = db.relationship('User', backref='groups', lazy='dynamic' order_by=name)
    

